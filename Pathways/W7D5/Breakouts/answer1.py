import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_form():
    # Get values from the form
    name = name_entry.get()
    email = email_entry.get()
    
    # Create message with form data
    message = f"Registration submitted!\n\nName: {name}\nEmail: {email}"
    
    if newsletter_var.get():
        message += "\nSubscribed to newsletter: Yes"
    else:
        message += "\nSubscribed to newsletter: No"
        
    message += f"\nYear of Study: {year_var.get()}"
    
    # Show message box with form data
    messagebox.showinfo("Form Submitted", message)

# Create main window
window = tk.Tk()
window.title("Student Registration Form")
window.geometry("500x400")
window.configure(bg="#f0f0f0")  # Light gray background

# Title label
title_label = tk.Label(
    window,
    text="Student Registration Form",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    pady=15
)
title_label.pack()

# Create a frame for form fields
form_frame = tk.Frame(window, bg="#f0f0f0")
form_frame.pack(pady=10)

# 1. Name field
name_label = tk.Label(form_frame, text="Name:", width=15, anchor="w", bg="#f0f0f0")
name_label.grid(row=0, column=0, padx=5, pady=10, sticky="w")

name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=10)

# 2. Email field
email_label = tk.Label(form_frame, text="Email:", width=15, anchor="w", bg="#f0f0f0")
email_label.grid(row=1, column=0, padx=5, pady=10, sticky="w")

email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=10)

# 3. Checkbox for newsletter
newsletter_var = tk.BooleanVar()
newsletter_check = tk.Checkbutton(
    form_frame,
    text="Subscribe to newsletter",
    variable=newsletter_var,
    bg="#f0f0f0"
)
newsletter_check.grid(row=2, column=0, columnspan=2, pady=10, sticky="w")

# 4. Radio buttons for year of study
year_frame = tk.Frame(form_frame, bg="#f0f0f0")
year_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky="w")

year_label = tk.Label(year_frame, text="Year of Study:", bg="#f0f0f0")
year_label.pack(side=tk.LEFT, padx=5)

year_var = tk.StringVar(value="First Year")
years = ["First Year", "Second Year", "Third Year", "Fourth Year"]

for i, year in enumerate(years):
    rb = tk.Radiobutton(
        year_frame,
        text=year,
        variable=year_var,
        value=year,
        bg="#f0f0f0"
    )
    rb.pack(side=tk.LEFT, padx=5)

# 5. Submit button
submit_button = tk.Button(
    window,
    text="Submit Registration",
    command=submit_form,
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5
)
submit_button.pack(pady=20)

# Start the main event loop
window.mainloop()