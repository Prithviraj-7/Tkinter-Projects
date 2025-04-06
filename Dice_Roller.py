import tkinter as tk
from PIL import Image, ImageTk
import random

def roll_dice():
    dice_number = random.randint(1, 6)
    dice_label.config(text=str(dice_number))

root = tk.Tk()
root.title("Dice Roller")
root.geometry("300x200")
root.iconbitmap("favicon.ico") 

bg_image = Image.open("download.jpg")
bg_image = bg_image.resize((2000, 2500), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title = tk.Label(root, text="Dice Roller", font=("Arial", 20), bg="white")
title.place(relx=0.5, y=20, anchor="center")

dice_label = tk.Label(root, text="0", font=("Arial", 80), bg="white")
dice_label.place(relx=0.5, rely=0.5, anchor="center")

roll_button = tk.Button(root, text="Roll", font=("Arial", 16), command=roll_dice)
roll_button.place(relx=0.5, rely=0.85, anchor="center")

root.mainloop()