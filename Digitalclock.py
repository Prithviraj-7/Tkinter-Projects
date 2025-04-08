import tkinter as tk
from PIL import Image, ImageTk
from time import strftime
import requests

API_KEY = "b7dc34014b7a49049a0130925250804"

root = tk.Tk()
root.title("Weather + Clock App")
root.geometry("600x600")
root.iconbitmap("favicon (1).ico")
root.configure(bg="black")

bg_image = Image.open("black.png")
bg_image = bg_image.resize((2050, 2400), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def time():
    string = strftime("%H : %M : %S %p\n%D")
    clock_label.config(text=string)
    clock_label.after(1000, time)

clock_label = tk.Label(root, font=('calibri', 54, 'bold'), background="black", foreground="#FF5F1F")
clock_label.pack(pady=20)
time()

placeholder = "Enter city name..."

def get_weather():
    city = w_city.get()
    if city == "" or city == placeholder:
        result_label.config(text="Please enter a city name!", fg="red")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        try:
            weather = data['current']['condition']['text']
            temp = data['current']['temp_c']
            result_label.config(
                text=f"Weather in {city}:\n{weather}, {temp}°C", fg="#FF5F1F"
            )
        except KeyError:
            result_label.config(text="City not found!", fg="red")
    else:
        error_msg = data.get("error", {}).get("message", "Unknown error")
        result_label.config(text=error_msg, fg="red")

def on_entry_click(event):
    if w_city.get() == placeholder:
        w_city.delete(0, tk.END)
        w_city.config(fg="#FF5F1F")

def on_focus_out(event):
    if w_city.get() == "":
        w_city.insert(0, placeholder)
        w_city.config(fg="gray")

w_city = tk.Entry(root, font=("Arial", 16), fg="gray", bg="black", insertbackground="#FF5F1F")
w_city.insert(0, placeholder)
w_city.bind("<FocusIn>", on_entry_click)
w_city.bind("<FocusOut>", on_focus_out)
w_city.place(relx=0.5, rely=0.45, anchor="center")

w_button = tk.Button(
    root,
    text="Click here to get current weather condition",
    font=("Arial", 12),
    bg="#FF5F1F",
    fg="black",
    wraplength=280,
    command=get_weather
)
w_button.place(relx=0.5, rely=0.55, anchor="center")

result_label = tk.Label(root, text="", font=("Arial", 14), fg="#FF5F1F", bg="black", wraplength=350)
result_label.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()
