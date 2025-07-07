import tkinter as tk

clickCount = 0

root = tk.Tk()
root.title("Button app")

lbl = tk.Label(root, text="Click Button")
lbl.grid(row=0, column=0)


def on_click():
    clickCount = clickCount + 1 #not working rn
    print("Client clicked button")
    print("Button new value :",clickCount)


btn =tk.Button(root, text="Button", command=on_click)
btn.grid(row=0,column=1)

root.mainloop()