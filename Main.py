import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow required for resizing

def check_login():
    global login_window

    username = username_entry.get()
    password = password_entry.get()

    if username == "user" and password == "pass":
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        login_window.withdraw()  # Hide login window instead of destroying
        open_tcp_panel()
    else:
        messagebox.showerror(":( Login Failed", "Incorrect username or password. LOCK IN")

def open_tcp_panel():
    tcp_window = tk.Toplevel()
    tcp_window.title("TCP Panel .~.")
    tcp_window.geometry("800x800")

    click_count = [0]
    size = [100]  # Initial size for resizing images

    image_paths = [
        "C:/Users/abell/PycharmProjects/PythonProject1/Jeff1.gif",
        "C:/Users/abell/PycharmProjects/PythonProject1/Jeff2.gif",
        "C:/Users/abell/PycharmProjects/PythonProject1/Jeff3.gif"
    ]

    original_images = [Image.open(path) for path in image_paths]

    lbl = tk.Label(tcp_window, text="Feed him cookies🍪", font=("Arial", 14))
    lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Use place geometry manager for smooth vertical movement
    image_label = tk.Label(tcp_window)
    image_label.place(x=400, y=200, anchor="center")  # Start near center top

    # Variables for animation
    direction = [1]  # 1 means moving down, -1 means moving up
    y_pos = [200]    # Current y position

    def update_image():
        idx = click_count[0] % len(original_images)
        img = original_images[idx]
        resized = img.resize((size[0], size[0]))
        tk_image = ImageTk.PhotoImage(resized)
        image_label.config(image=tk_image)
        image_label.image = tk_image  # keep reference

        image_label.place_configure(y=y_pos[0])


    def on_click():
        click_count[0] += 1
        size[0] += 20  # Increase size on click

        feedback_emojis = [":/", "$", "£", ":(", ":)"]
        emoji = feedback_emojis[click_count[0] % len(feedback_emojis)]
        lbl.config(text=f"Clicked {click_count[0]} times {emoji}")

    update_image()

    btn = tk.Button(tcp_window, text="Cookie generator 9000🍪", font=("Arial", 14), command=on_click)
    btn.grid(row=1, column=15, columnspan=2, padx=10, pady=20)



# ---------------- Login Window ----------------
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x180")

tk.Label(login_window, text="Username:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(login_window)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(login_window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(login_window, text="Login", command=check_login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

login_window.mainloop()
