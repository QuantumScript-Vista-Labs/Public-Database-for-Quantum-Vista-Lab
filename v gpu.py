import random
import time
import tkinter as tk

class ThermalSensor:
    def __init__(self):
        self.temperature = 25  # Initial temperature

    def measure_temperature(self):
        # Simulate temperature fluctuations
        self.temperature += random.uniform(-0.5, 0.5)
        return self.temperature

def update_temperature_label():
    current_temperature = sensor.measure_temperature()
    temperature_label.config(text=f"Current temperature: {current_temperature:.2f}°c")
    root.after(1000, update_temperature_label)  # Update temperature label every 1000 milliseconds (1 second)

if __name__ == "__main__":
    sensor = ThermalSensor()

    root = tk.Tk()
    root.title("Thermal Sensor")

    temperature_label = tk.Label(root, text="", font=("Arial", 16))
    temperature_label.pack(pady=20)

    update_temperature_label()

    root.mainloop()
