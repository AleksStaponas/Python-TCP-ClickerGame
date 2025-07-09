from tkinter import *

def scoreboard():
    image = Tk()
    image.title("LEADERBOARD")
    image.geometry("350x400")
    image.configure(bg="#f8f9fa")
    image.resizable(width=False, height=False)

    # Colours
    image.colours = {
        'sideBar': '#6e3a8a',
        'main_bg': '#198754',
        'card_blue': '#fff3cd'
    }

    # Title label
    label = Label(image, text="LEADERBOARD", font=("Arial", 32),
                  bg=image.colours['main_bg'], fg="white")
    label.pack(pady=20)

    # Unsorted leaderboard data (name, score)
    leaderboard_data = [

    ]
    # leaderboard_data.sort(reverse=True)

    # Sort the data by score descending (highest first)
    leaderboard_data.sort(key=lambda x: x[1], reverse=True)

    # Display each entry, sorted
    for index, (name, score) in enumerate(leaderboard_data, start=1):
        entry_text = f"{index}. {name} - {score}"
        entry_label = Label(image, text=entry_text, font=("Arial", 18),
                            bg="#f8f9fa", fg="black")
        entry_label.pack(anchor="w", padx=20)

    return image


def main():
    window = scoreboard()
    window.mainloop()


if __name__ == "__main__":
    main()
