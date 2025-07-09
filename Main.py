import base64
import socket
import threading
import time
import tkinter as tk
from functools import partial
import os
from PIL import Image, ImageTk
import json

USER_FILE = "users.json"
LAST_USER_FILE = "last_user.txt"
SAVE_FILE = "progress.json"

player_name = "Player"
leaderboard_data = []

ICON_PATHS = {
1: (r"C:\Users\abell\PycharmProjects\PythonTCPProject\images\Emoji's\Demon.png", 1200),
2: (r"C:\Users\abell\PycharmProjects\PythonTCPProject\images\Emoji's\Sunglasses.png", 1100),
3: (r"C:\Users\abell\PycharmProjects\PythonTCPProject\images\Emoji's\Happy.png", 1000),
}

RESIZED_ICONS = {}

def load_users():

    if os.path.exists(USER_FILE) and os.path.getsize(USER_FILE) > 0:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

def get_last_user():
    if os.path.exists(LAST_USER_FILE):
        with open(LAST_USER_FILE, "r") as f:
            return f.read().strip()
    return None

def set_last_user(user):
    with open(LAST_USER_FILE, "w") as f:
        f.write(user)

def load_scores():
    global leaderboard_data
    if os.path.exists(SAVE_FILE) and os.path.getsize(SAVE_FILE) > 0:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            leaderboard_data = list(data.items())
    else:
        leaderboard_data = [
            ("Bob", 2000),
            ("Aleks", 1100),
            ("Archangel", 1000),
            ("Daisy", 550),
            ("Ethan", 500),
            ("Ella", 350),
            ("Martin", 250),
            ("Josh", 150),
        ]

def save_scores():
    with open(SAVE_FILE, "w") as f:
        json.dump({name: score for name, score in leaderboard_data}, f)

def load_resized_icons(master):
    for idx, (path, _) in ICON_PATHS.items():
        if os.path.isfile(path):
            img = Image.open(path)
            img.thumbnail((80, 50))
            RESIZED_ICONS[idx] = ImageTk.PhotoImage(img, master=master)
        else:
            RESIZED_ICONS[idx] = None

def send_leaderboard():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("127.0.0.1", 12345))
            leaderboard_str = "\n".join(f"{name}:{score}" for name, score in leaderboard_data)
            encoded_data = base64.b64encode(leaderboard_str.encode())
            sock.sendall(encoded_data)
            sock.close()
            print("Leaderboard sent to server.")
        except Exception as e:
                print("Error sending leaderboard:", e)
                time.sleep(5)




def open_clicker_window(player: str):
    global leaderboard_data
    click_count = 1
    load_scores()

    if not any(name == player for name, _ in leaderboard_data):
        leaderboard_data.append((player, 0))

    clicker = tk.Tk()
    clicker.title("Clicker Leaderboard")
    clicker.geometry("360x580")
    clicker.configure(bg="#f0f0f0")

    load_resized_icons(clicker)

    # Start leaderboard sending in the background
    threading.Thread(target=send_leaderboard, daemon=True).start()

    title_label = tk.Label(clicker, text=f"Clicks: {click_count}", font=("Arial", 14), fg="blue", bg="#f0f0f0")
    title_label.pack(pady=10)

    board_frame = tk.Frame(clicker, bg="#f0f0f0")
    board_frame.pack(fill="both", expand=True, padx=10)

    button_images = []
    button_image_paths = [
        r"\PycharmProjects\PythonProject3\Jeff1.png",
        r"\PycharmProjects\PythonProject3\Jeff2.png",
        r"\PycharmProjects\PythonProject3\Jeff3.png",
    ]
    for path in button_image_paths:
        if os.path.isfile(path):
            img = Image.open(path)
            img.thumbnail((500, 500))
            button_images.append(ImageTk.PhotoImage(img, master=clicker))
    if not button_images:
        button_images = [None]

    button_image_index = 0

    def update_leaderboard():
        nonlocal click_count
        for i, (n, s) in enumerate(leaderboard_data):
            if n == player:
                leaderboard_data[i] = (n, click_count)
        leaderboard_data.sort(key=lambda x: x[1], reverse=True)

    def render_leaderboard():
        for widget in board_frame.winfo_children():
            widget.destroy()

        for idx, (n, s) in enumerate(leaderboard_data[:3], start=1):
            row = tk.Frame(board_frame, bg="#f0f0f0")
            row.pack(fill="x", pady=2)

            icon_img = RESIZED_ICONS.get(idx)
            required_score = ICON_PATHS.get(idx)[1]

            if icon_img and s >= required_score:
                tk.Label(row, image=icon_img, bg="#f0f0f0").pack(side="left", padx=(0, 5))
            else:
                tk.Label(row, width=5, bg="#f0f0f0").pack(side="left")

            tk.Label(row, text=f"{idx}. {n} — {s}", font=("Arial", 12, "bold"), fg="blue", bg="#f0f0f0").pack(
                side="left")

        tk.Frame(board_frame, height=2, bd=1, relief="sunken", bg="#999").pack(fill="x", pady=5)

        for idx, (n, s) in enumerate(leaderboard_data[3:], start=4):
            tk.Label(board_frame, text=f"{idx}. {n} — {s}", font=("Arial", 11), fg="blue", bg="#f0f0f0").pack(
                anchor="w", pady=1)

    def on_click():
        nonlocal click_count, button_image_index
        click_count += 1
        title_label.config(text=f"Clicks: {click_count}")
        button_image_index = (button_image_index + 1) % len(button_images)
        btn.config(image=button_images[button_image_index])
        update_leaderboard()
        render_leaderboard()

    btn = tk.Button(clicker, text="Click Me!", font=("Arial", 12), command=on_click)
    btn.pack(pady=10)

    if button_images[0]:
        btn.config(image=button_images[0])
        btn.image = button_images[0]

    update_leaderboard()
    render_leaderboard()
    clicker.mainloop()

def validate_login(username_var, pw_var, cp_var, win, error_label):
    user = username_var.get().strip()
    pw = pw_var.get()
    cp = cp_var.get()

    if not user:
        error_label.config(text="Username cannot be empty", fg="red")
        return
    if pw != cp:
        error_label.config(text="Passwords do not match", fg="red")
        return

    global player_name
    player_name = user
    win.destroy()
    open_clicker_window(user)

def password_window():
    login = tk.Tk()
    login.title("Login")
    login.geometry("350x200")
    login.configure(bg="#f0f0f0")

    tk.Label(login, text="Username", bg="#f0f0f0", fg="blue").grid(row=0, column=0, padx=10, pady=5)
    username_var = tk.StringVar()
    tk.Entry(login, textvariable=username_var).grid(row=0, column=1)

    tk.Label(login, text="Password", bg="#f0f0f0", fg="blue").grid(row=1, column=0)
    password_var = tk.StringVar()
    tk.Entry(login, textvariable=password_var, show="*").grid(row=1, column=1)

    tk.Label(login, text="Confirm Password", bg="#f0f0f0", fg="blue").grid(row=2, column=0)
    confirm_var = tk.StringVar()
    tk.Entry(login, textvariable=confirm_var, show="*").grid(row=2, column=1)

    error_label = tk.Label(login, text="", fg="red", bg="#f0f0f0")
    error_label.grid(row=4, column=0, columnspan=2)

    login_btn = partial(validate_login, username_var, password_var, confirm_var, login, error_label)
    tk.Button(login, text="Login", command=login_btn).grid(row=3, column=0, columnspan=2, pady=10)

    login.mainloop()

if __name__ == "__main__":
    password_window()

