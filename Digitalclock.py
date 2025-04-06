import tkinter as tk 
from PIL import Image, ImageTk  
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="white")
root.iconbitmap("favicon (1).ico")

bg_image = Image.open("black.png")

bg_image = bg_image.resize((2050, 2400), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def time():
    string = strftime("%H : %M : %S %p \n %D")
    label.config(text=string)
    label.after(2000, time)

label = tk.Label(root, font=('calibri', 70, 'bold'), background="black", foreground="grey")
label.pack(anchor='center')

time()
root.mainloop()