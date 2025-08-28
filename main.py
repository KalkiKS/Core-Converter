import customtkinter as ctk
from tkinter import messagebox

# ---- Conversion Function ----
def convert_length(value, unit):

    factor = {
        "Meter": 1,
        "Centimeter": 0.01,
        "Kilometer": 1000,
        "Millimeter": 0.001,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Mile": 1609.34,
        "Yard": 0.9144
    }
    
    if unit not in factor:
        return None

    value_in_meter = value * factor[unit] # First convert input into meters
    results = {u: value_in_meter / f for u, f in factor.items()}
    return results

def convert_weight(value, unit):

    factor = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
        "Ton": 1000
    }
    
    if unit not in factor:
        return None
    
    value_in_kg = value * factor[unit] # First convert input into kilograms
    results = {u: value_in_kg / f for u, f in factor.items()}
    return results

def convert_temperature(value, unit):

    results = {}

    if unit == "Celsius":
        results["Celsius"] = value
        results["Fahrenheit"] = (value * 9/5) + 32
        results["Kelvin"] = value + 273.15

    elif unit == "Fahrenheit":
        results["Celsius"] = (value - 32) * 5/9
        results["Fahrenheit"] = value
        results["Kelvin"] = (value - 32) * 5/9 + 273.15

    elif unit == "Kelvin":
        results["Celsius"] = value - 273.15
        results["Fahrenheit"] = (value - 273.15) * 9/5 + 32
        results["Kelvin"] = value
    
    else:
        return None
    
    return results


# --- Tkinter GUI
def convert_units(category, entry_value, unit_box, results_text):
    try:
        value = float(entry_value.get())
        unit = unit_box.get()

        if category == "Length":
            converted = convert_length(value, unit)
        elif category == "Weight":
            converted = convert_weight(value, unit)
        elif category == "Temperature":
            converted = convert_temperature(value, unit)
        else:
            messagebox.showerror("Error", "Invalid category selected")
            return
        
        # Display results
        results_text.configure(state="normal")
        results_text.delete("1.0", "end")
        results_text.insert("end", f"Converted from {value} {unit}:\n\n")
        for u, v in converted.items(): # type: ignore
            results_text.insert("end", f"{u}: {v:.4f}\n")
        results_text.configure(state="disabled")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


# --- Setup ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


root = ctk.CTk()
root.title("Unit Converter")
root.geometry("500x500")
root.resizable(False,False)

tabview = ctk.CTkTabview(root)
tabview.pack(expand=True, fill="both", padx=20, pady=20)

length_tab = tabview.add("Length")
weight_tab = tabview.add("Weight")
temp_tab = tabview.add("Temperature")


# --- Length Tab ---
ctk.CTkLabel(length_tab, text="Enter Value:").pack(pady=5)
length_entry = ctk.CTkEntry(length_tab, placeholder_text="Enter number")
length_entry.pack(pady=5)


length_units = list(convert_length(1, "Meter").keys()) # type: ignore
length_unit_box = ctk.CTkComboBox(length_tab, values=length_units)
length_unit_box.pack(pady=5)
length_unit_box.set(length_units[0])

length_results = ctk.CTkTextbox(length_tab, width=400, height=200)
length_results.pack(pady=10)
length_results.configure(state="disabled")

ctk.CTkButton(length_tab, text="Convert", command=lambda: convert_units("Length", length_entry, length_unit_box, length_results)).pack(pady=10)



# --- Weight Tab ---
ctk.CTkLabel(weight_tab, text="Enter Value:").pack(pady=5)
weight_entry = ctk.CTkEntry(weight_tab, placeholder_text="Enter number")
weight_entry.pack(pady=5)


weight_units = list(convert_weight(1, "Kilogram").keys()) # type: ignore
weight_unit_box = ctk.CTkComboBox(weight_tab, values=weight_units)
weight_unit_box.pack(pady=5)
weight_unit_box.set(weight_units[0])


weight_results = ctk.CTkTextbox(weight_tab, width=400, height=200)
weight_results.pack(pady=10)
weight_results.configure(state="disabled")

ctk.CTkButton(weight_tab, text="Convert", command=lambda: convert_units("Weight", weight_entry, weight_unit_box, weight_results)).pack(pady=10)



# --- Temperature Tab ---

ctk.CTkLabel(temp_tab, text="Enter Value:").pack(pady=5)
temp_entry = ctk.CTkEntry(temp_tab, placeholder_text="Enter number")
temp_entry.pack(pady=5)


temp_units = list(convert_temperature(1, "Celsius").keys()) # type: ignore
temp_unit_box = ctk.CTkComboBox(temp_tab, values=temp_units)
temp_unit_box.pack(pady=5)
temp_unit_box.set(temp_units[0])


temp_results = ctk.CTkTextbox(temp_tab, width=400, height=200)
temp_results.pack(pady=10)
temp_results.configure(state="disabled")

ctk.CTkButton(temp_tab, text="Convert", command=lambda: convert_units("Temperature", temp_entry, temp_unit_box, temp_results)).pack(pady=10)



root.mainloop()