import tkinter as tk
import webbrowser
from tkinter import messagebox
from transport_carbon_footprint import TransportCarbonFootprintCalculator
from waste_carbon_footprint import WasteEmissionCalculator
from electricity_footprint import ElectricityFootprintCalculator
import subprocess


def display_health_benefits():
    messagebox.showinfo("Health Benefits", "Reducing your carbon footprint has many health benefits, including lower risk of heart disease and respiratory illnesses. By reducing your carbon footprint, you can help improve air and water quality, reduce pollution, and support a healthier environment for all.")

def display_users_manual():
    messagebox.showinfo("User Manual", "Gaia is a Python-based multi-functional carbon footprint calculator that allows users to calculate their carbon footprint in three categories: transportation, waste, and electricity. Additionally, Giaia offers diverse feature that allows users to experince AI powered object detection model to identify items that contribute to carbon footprint, the AI powered chatbot that the user can inquiry about environmenal haealth for the research purpose, and reading researches on the website for free.Once you have launched Giaia, the GUI will be displayed.")

def exit_program():
    root.destroy()

def open_eco_teaching():
    EcoTeaching(root)


def open_vision():
    root.withdraw()  # hide the main window
    subprocess.Popen(['python', 'vision.py'])

# Create the main window
root = tk.Tk()
root.title("GAIA")

# Load the background image
bg_image = tk.PhotoImage(file="bg.png")

# Create a label for the background image and place it behind other widgets
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a label for the instruction slogan
instruction_label = tk.Label(root, text="See the bigger picture with GAIA - Your Carbon Footprint Companion", bg='snow')
instruction_label.pack(padx=10, pady=10)

# Create a button to calculate transport carbon footprint
transport_button = tk.Button(root, text="Transport Carbon Footprint", command=lambda: TransportCarbonFootprintCalculator(root), bg='snow', width=20)
transport_button.pack(padx=10, pady=10)

# Create a button to calculate waste carbon footprint
waste_button = tk.Button(root, text="Waste Carbon Footprint", command=lambda: WasteEmissionCalculator(root), bg='snow', width=20)
waste_button.pack(padx=10, pady=10)

# Create a button to calculate electricity carbon footprint
electricity_button = tk.Button(root, text="Electricity Carbon Footprint", command=lambda: ElectricityFootprintCalculator(root), bg="snow", width=20)
electricity_button.pack(padx=10, pady=10)

# Create a button to learn about health benefits
health_button = tk.Button(root, text="Learn about Health Benefits", command=display_health_benefits, bg="snow", width=20)
health_button.pack(padx=10, pady=10)

# Create a button to open vision.py
vision_button = tk.Button(root, text="Vision", command=open_vision, bg='snow', width=20)
vision_button.pack(padx=10, pady=10)

# Create a button to open the Our Researches page
about_button = tk.Button(root, text="Our Researches", command=lambda: webbrowser.open("https://c4c.netlify.app/"), bg="snow", width=20)
about_button.pack(padx=10, pady=10)

# Create a button to open the Our Chat Bot page
about_button = tk.Button(root, text="Chat Bot", command=lambda: webbrowser.open("http://127.0.0.1:7860"), bg="snow", width=20)
about_button.pack(padx=10, pady=10)

# Create a button to learn about the app
health_button = tk.Button(root, text="About GAIA", command=display_users_manual, bg="snow", width=20)
health_button.pack(padx=10, pady=10)

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=exit_program, bg="snow", width=20)
exit_button.pack(padx=10, pady=10)


# Run the main event loop
root.mainloop()
