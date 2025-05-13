"""
Example 3: Basic Tkinter Widgets
This demonstrates various common Tkinter widgets and their basic usage
"""

import tkinter as tk
from tkinter import ttk  # ttk provides themed widgets

def show_selection():
    # Get values from various widgets and show them
    name = name_entry.get()
    password = password_entry.get()
    
    if name and password:
        message = f"Hello, {name}!"
        if agree_var.get():
            message += "\nYou agreed to the terms."
        else:
            message += "\nYou did not agree to the terms."
            
        message += f"\nYour favorite color is: {color_var.get()}"
        message += f"\nSelected hobby: {hobby_combobox.get()}"
        
        # Update the result text widget
        result_text.delete(1.0, tk.END)  # Clear current text
        result_text.insert(tk.END, message)
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please fill in all fields!")

# Create the main window
window = tk.Tk()
window.title("Tkinter Widgets Demo")
window.geometry("600x500")
window.configure(padx=20, pady=20)

# Create a title label
title_label = tk.Label(
    window,
    text="Tkinter Widgets Showcase",
    font=("Arial", 16, "bold"),
    pady=10
)
title_label.pack()

# 1. Text Labels
info_label = tk.Label(
    window,
    text="This demo showcases common Tkinter widgets.",
    font=("Arial", 10, "italic"),
    fg="gray"
)
info_label.pack(pady=(0, 20))

# 2. Entry fields (text input)
# Name entry with label
name_frame = tk.Frame(window)
name_frame.pack(fill=tk.X, pady=5)

name_label = tk.Label(name_frame, text="Name:", width=10, anchor="w")
name_label.pack(side=tk.LEFT)

name_entry = tk.Entry(name_frame, width=40)
name_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

# Password entry with label
password_frame = tk.Frame(window)
password_frame.pack(fill=tk.X, pady=5)

password_label = tk.Label(password_frame, text="Password:", width=10, anchor="w")
password_label.pack(side=tk.LEFT)

password_entry = tk.Entry(password_frame, width=40, show="*")  # Hide password with *
password_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

# 3. Checkbutton
agree_var = tk.BooleanVar()
agree_check = tk.Checkbutton(
    window,
    text="I agree to the terms and conditions",
    variable=agree_var,
    onvalue=True,
    offvalue=False
)
agree_check.pack(anchor="w", pady=10)

# 4. Radio Buttons for color selection
color_frame = tk.Frame(window)
color_frame.pack(anchor="w", pady=10)

color_label = tk.Label(color_frame, text="Favorite color:")
color_label.pack(side=tk.LEFT)

color_var = tk.StringVar(value="Blue")  # Default selection

colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
for color in colors:
    radio = tk.Radiobutton(
        color_frame,
        text=color,
        variable=color_var,
        value=color
    )
    radio.pack(side=tk.LEFT, padx=5)

# 5. Combobox (dropdown)
hobby_frame = tk.Frame(window)
hobby_frame.pack(fill=tk.X, pady=10)

hobby_label = tk.Label(hobby_frame, text="Select hobby:", width=10, anchor="w")
hobby_label.pack(side=tk.LEFT)

hobby_combobox = ttk.Combobox(
    hobby_frame,
    values=["Reading", "Sports", "Music", "Cooking", "Gaming", "Coding"]
)
hobby_combobox.current(0)  # Set the default selection to the first item
hobby_combobox.pack(side=tk.LEFT, padx=5)

# 6. Button
submit_button = tk.Button(
    window,
    text="Submit",
    command=show_selection,
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5
)
submit_button.pack(pady=15)

# 7. Text widget for displaying results
result_label = tk.Label(window, text="Results:")
result_label.pack(anchor="w")

result_text = tk.Text(window, height=5, width=50)
result_text.pack(pady=5)

# Start the main event loop
window.mainloop()