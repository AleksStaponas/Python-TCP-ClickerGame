import tkinter as tk
from tkinter import messagebox

numberOfClicks = 0
label = None  # define label at module level to avoid scope issues

# the use of subroutines is for code reusability and organisation
def update_image():
    global numberOfClicks, label
    # Makes it accessible to other subroutines
    numberOfClicks += 1

    label.config(text=f"The button was clicked {numberOfClicks} times...")

def create_imageWindow():
    # creation of the main window
    image = tk.Toplevel()  
    image.title("Archangel and Alek's Cookie Clicker")
    image.geometry("500x500")
    # the title of the window
    lbl = tk.Label(image, text="Welcome to Archangel + Alek's Cookie Clicker! ")  
    lbl.pack(pady=10)  # ensures the text is visible
    return image, lbl


def ModuxCookie_Creation(image_window, lbl):
    cookie_image = tk.PhotoImage(file="C:/Users/abell/PycharmProjects/PythonProject4/Jeff3.png")

    # create a button with the cookie image
    button = tk.Button(image_window, image=cookie_image, command=update_image)
    button.image = cookie_image
    button.config(width=100, height=100)
    button.pack(pady=5)

def main():
    global label  # this is used to easily access the label keyword anywhere anytime

    image_window, label_local = create_imageWindow()
    label = label_local
    ModuxCookie_Creation(image_window, label)

#  LOGIN SECTION
def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Archangel" and password == "Aleks":
        login_window.destroy()
        main()  # launch cookie clicker after login
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

# create login window
login_window = tk.Tk()
login_window.title("Login")

tk.Label(login_window, text="Username:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(login_window)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(login_window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_window, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(login_window, text="Login", command=check_login).grid(row=2, column=0, columnspan=2, pady=10)

login_window.mainloop()
