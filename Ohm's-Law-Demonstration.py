
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Ohm's Law: V = I * R

def calculate():
    try:
        voltage_text = voltage_entry.get().strip()
        current_text = current_entry.get().strip()
        resistance_text = resistance_entry.get().strip()

        # Calculate missing value automatically
        if not voltage_text and current_text and resistance_text:
            current = float(current_text)
            resistance = float(resistance_text)

            if current < 0 or resistance <= 0:
                raise ValueError("Current must be non-negative and resistance positive.")

            voltage = current * resistance

        elif not current_text and voltage_text and resistance_text:
            voltage = float(voltage_text)
            resistance = float(resistance_text)

            if voltage < 0 or resistance <= 0:
                raise ValueError("Voltage must be non-negative and resistance positive.")

            current = voltage / resistance

        elif not resistance_text and voltage_text and current_text:
            voltage = float(voltage_text)
            current = float(current_text)

            if voltage < 0 or current <= 0:
                raise ValueError("Voltage must be non-negative and current positive.")

            resistance = voltage / current

        else:
            messagebox.showwarning(
                "Input Error",
                "Exactly two values enter karein aur teesri value blank chhorein."
            )
            return

        voltage_entry.delete(0, tk.END)
        current_entry.delete(0, tk.END)
        resistance_entry.delete(0, tk.END)

        voltage_entry.insert(0, f"{voltage:.3f}")
        current_entry.insert(0, f"{current:.3f}")
        resistance_entry.insert(0, f"{resistance:.3f}")

        result_label.config(
            text=f"Voltage: {voltage:.3f} V\n"
                 f"Current: {current:.3f} A\n"
                 f"Resistance: {resistance:.3f} Ω"
        )

    except ValueError as error:
        messagebox.showerror(
            "Invalid Input",
            str(error) if str(error) else "Please enter valid numeric values."
        )


def show_graph():
    try:
        voltage = float(voltage_entry.get())
        current = float(current_entry.get())
        resistance = float(resistance_entry.get())

        if voltage < 0 or current < 0 or resistance <= 0:
            messagebox.showerror(
                "Input Error",
                "Voltage/current non-negative aur resistance positive honi chahiye."
            )
            return

        currents = [i / 100 for i in range(0, int(current * 100) + 1)]
        voltages = [i * resistance for i in currents]

        plt.plot(currents, voltages, marker="o", label="V = I × R")
        plt.title("Ohm's Law: Voltage vs Current")
        plt.xlabel("Current (A)")
        plt.ylabel("Voltage (V)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Pehle calculate karein ya teeno valid values enter karein."
        )


def clear_fields():
    voltage_entry.delete(0, tk.END)
    current_entry.delete(0, tk.END)
    resistance_entry.delete(0, tk.END)
    result_label.config(text="Enter any two values to calculate the third.")


# Create application window
root = tk.Tk()
root.title("Ohm's Law Demonstration")
root.geometry("450x470")
root.configure(bg="#101827")
root.resizable(False, False)

title = tk.Label(
    root,
    text="OHM'S LAW DEMONSTRATION",
    font=("Arial", 16, "bold"),
    fg="#55e6c1",
    bg="#101827"
)
title.pack(pady=20)

def add_field(label_text):
    frame = tk.Frame(root, bg="#101827")
    frame.pack(pady=7)

    label = tk.Label(
        frame,
        text=label_text,
        width=15,
        anchor="w",
        font=("Arial", 11),
        fg="white",
        bg="#101827"
    )
    label.pack(side="left")

    entry = tk.Entry(frame, width=20, font=("Arial", 11))
    entry.pack(side="left")
    return entry


voltage_entry = add_field("Voltage (V):")
current_entry = add_field("Current (A):")
resistance_entry = add_field("Resistance (Ω):")

tk.Label(
    root,
    text="V = I × R",
    font=("Arial", 14, "bold"),
    fg="#55e6c1",
    bg="#101827"
).pack(pady=12)

button_frame = tk.Frame(root, bg="#101827")
button_frame.pack(pady=5)

tk.Button(
    button_frame,
    text="Calculate",
    command=calculate,
    width=12,
    bg="#55e6c1",
    fg="#101827"
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Show Graph",
    command=show_graph,
    width=12,
    bg="#3498db",
    fg="white"
).pack(side="left", padx=5)

tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    width=12
).pack(pady=8)

result_label = tk.Label(
    root,
    text="Enter any two values to calculate the third.",
    font=("Arial", 10),
    fg="white",
    bg="#101827",
    justify="center"
)
result_label.pack(pady=12)

root.mainloop()
