"""
Modern Student Registration Form - Tkinter Application
A sleek, responsive design with gradient-like effects and modern typography

Features:
- Modern UI with gradient background simulation
- Responsive design with proper spacing
- Form validation and user feedback
- Elegant typography and color scheme
- Professional layout using grid system
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class ModernRegistrationForm:
    def __init__(self):
        # Initialize main window
        self.root = tk.Tk()
        self.setup_window()
        self.setup_styles()
        self.create_widgets()
        self.setup_layout()
          def setup_window(self):
        """Configure the main window with modern styling"""
        self.root.title("Student Registration Form")
        self.root.geometry("700x850")  # Increased size to handle content overflow
        self.root.resizable(True, True)
        self.root.minsize(650, 800)  # Set minimum size to prevent layout issues
        
        # Modern gradient-like background (simulated with frame layering)
        self.root.configure(bg="#f0f2f5")
        
        # Center the window on screen
        self.root.eval('tk::PlaceWindow . center')
        
    def setup_styles(self):
        """Configure modern styling for ttk widgets"""
        self.style = ttk.Style()
        
        # Configure modern button style
        self.style.configure(
            "Modern.TButton",
            font=("Segoe UI", 10, "bold"),
            foreground="white",
            background="#4285f4",
            borderwidth=0,
            focuscolor="none",
            padding=(20, 10)
        )
        
        # Configure modern entry style
        self.style.configure(
            "Modern.TEntry",
            font=("Segoe UI", 10),
            fieldbackground="white",
            borderwidth=1,
            relief="solid",
            padding=(10, 8)
        )
        
        # Configure modern combobox style
        self.style.configure(
            "Modern.TCombobox",
            font=("Segoe UI", 10),
            fieldbackground="white",
            borderwidth=1,
            relief="solid",
            padding=(10, 8)
        )
        
    def create_widgets(self):
        """Create all form widgets with modern styling"""
        
        # Main container frame with modern styling
        self.main_frame = tk.Frame(
            self.root, 
            bg="#ffffff",
            relief="raised",
            borderwidth=2
        )
        
        # Header section with gradient-like effect
        self.header_frame = tk.Frame(
            self.main_frame,
            bg="#4285f4",
            height=80
        )
        
        # Title label with modern typography
        self.title_label = tk.Label(
            self.header_frame,
            text="🎓 Student Registration",
            font=("Segoe UI", 24, "bold"),
            fg="white",
            bg="#4285f4",
            pady=20
        )
        
        # Form container
        self.form_frame = tk.Frame(
            self.main_frame,
            bg="#ffffff",
            padx=40,
            pady=30
        )
        
        # Personal Information Section
        self.section1_label = tk.Label(
            self.form_frame,
            text="Personal Information",
            font=("Segoe UI", 14, "bold"),
            fg="#333333",
            bg="#ffffff",
            anchor="w"
        )
        
        # Name field
        self.name_label = tk.Label(
            self.form_frame,
            text="Full Name *",
            font=("Segoe UI", 10),
            fg="#666666",
            bg="#ffffff",
            anchor="w"
        )
        self.name_entry = ttk.Entry(
            self.form_frame,
            style="Modern.TEntry",
            width=40
        )
        
        # Email field
        self.email_label = tk.Label(
            self.form_frame,
            text="Email Address *",
            font=("Segoe UI", 10),
            fg="#666666",
            bg="#ffffff",
            anchor="w"
        )
        self.email_entry = ttk.Entry(
            self.form_frame,
            style="Modern.TEntry",
            width=40
        )
        
        # Phone field
        self.phone_label = tk.Label(
            self.form_frame,
            text="Phone Number",
            font=("Segoe UI", 10),
            fg="#666666",
            bg="#ffffff",
            anchor="w"
        )
        self.phone_entry = ttk.Entry(
            self.form_frame,
            style="Modern.TEntry",
            width=40
        )
        
        # Academic Information Section
        self.section2_label = tk.Label(
            self.form_frame,
            text="Academic Information",
            font=("Segoe UI", 14, "bold"),
            fg="#333333",
            bg="#ffffff",
            anchor="w"
        )
        
        # Program selection (dropdown)
        self.program_label = tk.Label(
            self.form_frame,
            text="Program of Study *",
            font=("Segoe UI", 10),
            fg="#666666",
            bg="#ffffff",
            anchor="w"
        )
        self.program_var = tk.StringVar()
        self.program_combo = ttk.Combobox(
            self.form_frame,
            textvariable=self.program_var,
            style="Modern.TCombobox",
            width=37,
            state="readonly"
        )
        self.program_combo['values'] = (
            "Computer Science",
            "Engineering",
            "Business Administration",
            "Psychology",
            "Biology",
            "Mathematics",
            "English Literature",
            "Art & Design"
        )
        
        # Year level (radio buttons)
        self.year_label = tk.Label(
            self.form_frame,
            text="Year Level *",
            font=("Segoe UI", 10),
            fg="#666666",
            bg="#ffffff",
            anchor="w"
        )
        
        self.year_var = tk.StringVar(value="1st Year")
        self.year_frame = tk.Frame(self.form_frame, bg="#ffffff")
        
        years = ["1st Year", "2nd Year", "3rd Year", "4th Year", "Graduate"]
        self.year_buttons = []
        for i, year in enumerate(years):
            rb = tk.Radiobutton(
                self.year_frame,
                text=year,
                variable=self.year_var,
                value=year,
                font=("Segoe UI", 9),
                fg="#666666",
                bg="#ffffff",
                selectcolor="#4285f4",
                activebackground="#ffffff",
                activeforeground="#4285f4"
            )
            self.year_buttons.append(rb)
        
        # Preferences Section
        self.section3_label = tk.Label(
            self.form_frame,
            text="Preferences & Options",
            font=("Segoe UI", 14, "bold"),
            fg="#333333",
            bg="#ffffff",
            anchor="w"
        )
        
        # Checkboxes for additional options
        self.checkbox_frame = tk.Frame(self.form_frame, bg="#ffffff")
        
        self.newsletter_var = tk.BooleanVar()
        self.newsletter_check = tk.Checkbutton(
            self.checkbox_frame,
            text="📧 Subscribe to newsletter",
            variable=self.newsletter_var,
            font=("Segoe UI", 9),
            fg="#666666",
            bg="#ffffff",
            selectcolor="#4285f4",
            activebackground="#ffffff",
            activeforeground="#4285f4"
        )
        
        self.parking_var = tk.BooleanVar()
        self.parking_check = tk.Checkbutton(
            self.checkbox_frame,
            text="🚗 Request parking permit",
            variable=self.parking_var,
            font=("Segoe UI", 9),
            fg="#666666",
            bg="#ffffff",
            selectcolor="#4285f4",
            activebackground="#ffffff",
            activeforeground="#4285f4"
        )
        
        self.housing_var = tk.BooleanVar()
        self.housing_check = tk.Checkbutton(
            self.checkbox_frame,
            text="🏠 Interested in housing information",
            variable=self.housing_var,
            font=("Segoe UI", 9),
            fg="#666666",
            bg="#ffffff",
            selectcolor="#4285f4",
            activebackground="#ffffff",
            activeforeground="#4285f4"
        )
        
        # Submit button with modern styling
        self.button_frame = tk.Frame(self.form_frame, bg="#ffffff")
        
        self.submit_button = tk.Button(
            self.button_frame,
            text="✓ Submit Registration",
            command=self.submit_form,
            font=("Segoe UI", 12, "bold"),
            fg="white",
            bg="#4285f4",
            activebackground="#3367d6",
            activeforeground="white",
            border=0,
            padx=30,
            pady=12,
            cursor="hand2"
        )
        
        self.clear_button = tk.Button(
            self.button_frame,
            text="↺ Clear Form",
            command=self.clear_form,
            font=("Segoe UI", 10),
            fg="#666666",
            bg="#f8f9fa",
            activebackground="#e9ecef",
            activeforeground="#495057",
            border=1,
            padx=20,
            pady=8,
            cursor="hand2"
        )
        
        # Status label for feedback
        self.status_label = tk.Label(
            self.form_frame,
            text="",
            font=("Segoe UI", 9),
            fg="#666666",
            bg="#ffffff"
        )
        
    def setup_layout(self):
        """Arrange widgets using grid layout for responsive design"""
        
        # Main frame layout
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header layout
        self.header_frame.pack(fill="x", padx=0, pady=(0, 0))
        self.title_label.pack()
        
        # Form layout
        self.form_frame.pack(fill="both", expand=True)
        
        row = 0
        
        # Section 1: Personal Information
        self.section1_label.grid(row=row, column=0, columnspan=2, sticky="w", pady=(0, 15))
        row += 1
        
        # Name field
        self.name_label.grid(row=row, column=0, columnspan=2, sticky="w", pady=(0, 5))
        row += 1
        self.name_entry.grid(row=row, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        row += 1
        
        # Email field
        self.email_label.grid(row=row, column=0, columnspan=2, sticky="w", pady=(0, 5))
        row += 1
        self.email_entry.grid(row=row, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        row += 1
        
        # Phone field
        self.phone_label.grid(row=row, column=0, columnspan=2, sticky="w", pady=(0, 5))
        row += 1
        self.phone_entry.grid(row=row, column=0, columnspan=2, sticky="ew", pady=(0, 20))
        row += 1
        
        # Section 2: Academic Information
        self.section2_label.grid(row=row, column=0, columnspan=2, sticky="w", pady=(0, 15))
        row += 1
        
        # Program selection
        self.program_label.grid(row=row, column=0, columnspan=2, sticky="w", pady=(0, 5))
        row += 1
        self.program_combo.grid(row=row, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        row += 1
        
        # Year level
        self.year_label.grid(row=row, column=0, columnspan=2, sticky="w", pady=(0, 5))
        row += 1
        self.year_frame.grid(row=row, column=0, columnspan=2, sticky="ew", pady=(0, 20))
        
        # Layout radio buttons horizontally
        for i, rb in enumerate(self.year_buttons):
            rb.grid(row=0, column=i, padx=(0, 15), sticky="w")
        row += 1
        
        # Section 3: Preferences
        self.section3_label.grid(row=row, column=0, columnspan=2, sticky="w", pady=(0, 15))
        row += 1
        
        # Checkboxes
        self.checkbox_frame.grid(row=row, column=0, columnspan=2, sticky="ew", pady=(0, 20))
        self.newsletter_check.grid(row=0, column=0, sticky="w", pady=2)
        self.parking_check.grid(row=1, column=0, sticky="w", pady=2)
        self.housing_check.grid(row=2, column=0, sticky="w", pady=2)
        row += 1
        
        # Buttons
        self.button_frame.grid(row=row, column=0, columnspan=2, pady=(20, 10))
        self.submit_button.pack(side="left", padx=(0, 10))
        self.clear_button.pack(side="left")
        row += 1
        
        # Status label
        self.status_label.grid(row=row, column=0, columnspan=2, pady=(10, 0))
        
        # Configure grid weights for responsiveness
        self.form_frame.columnconfigure(0, weight=1)
        
    def validate_form(self):
        """Validate form fields and return validation status"""
        errors = []
        
        # Check required fields
        if not self.name_entry.get().strip():
            errors.append("Full Name is required")
            
        if not self.email_entry.get().strip():
            errors.append("Email Address is required")
        elif "@" not in self.email_entry.get() or "." not in self.email_entry.get():
            errors.append("Please enter a valid email address")
            
        if not self.program_var.get():
            errors.append("Program of Study is required")
            
        return errors
        
    def submit_form(self):
        """Handle form submission with validation and user feedback"""
        # Validate form
        errors = self.validate_form()
        
        if errors:
            # Show validation errors
            error_msg = "Please correct the following:\n\n" + "\n".join(f"• {error}" for error in errors)
            messagebox.showerror("Validation Error", error_msg)
            self.status_label.config(text="❌ Please correct the errors above", fg="#dc3545")
            return
        
        # Collect form data
        form_data = {
            "Name": self.name_entry.get().strip(),
            "Email": self.email_entry.get().strip(),
            "Phone": self.phone_entry.get().strip() or "Not provided",
            "Program": self.program_var.get(),
            "Year Level": self.year_var.get(),
            "Newsletter": "Yes" if self.newsletter_var.get() else "No",
            "Parking Permit": "Yes" if self.parking_var.get() else "No",
            "Housing Info": "Yes" if self.housing_var.get() else "No",
            "Submission Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Create summary message
        summary = "Registration Submitted Successfully! ✓\n\n"
        summary += "Summary of Information:\n"
        summary += "=" * 30 + "\n"
        for key, value in form_data.items():
            summary += f"{key}: {value}\n"
        
        # Show success message
        messagebox.showinfo("Registration Complete", summary)
        self.status_label.config(text="✅ Registration submitted successfully!", fg="#28a745")
        
        # Optional: Save to file or database here
        self.save_registration(form_data)
        
    def save_registration(self, data):
        """Save registration data to a file (demonstration)"""
        try:
            import os
            filename = "registrations.txt"
            with open(filename, "a", encoding="utf-8") as f:
                f.write(f"\n--- Registration: {data['Submission Time']} ---\n")
                for key, value in data.items():
                    f.write(f"{key}: {value}\n")
                f.write("-" * 50 + "\n")
            print(f"Registration saved to {filename}")
        except Exception as e:
            print(f"Error saving registration: {e}")
            
    def clear_form(self):
        """Clear all form fields"""
        # Clear text entries
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        
        # Reset selections
        self.program_var.set("")
        self.year_var.set("1st Year")
        
        # Clear checkboxes
        self.newsletter_var.set(False)
        self.parking_var.set(False)
        self.housing_var.set(False)
        
        # Clear status
        self.status_label.config(text="")
        
        # Show confirmation
        self.status_label.config(text="🔄 Form cleared", fg="#6c757d")
        
    def run(self):
        """Start the application"""
        # Add some sample data for demonstration (remove in production)
        self.name_entry.insert(0, "")
        self.email_entry.insert(0, "")
        
        # Start the main event loop
        self.root.mainloop()


# Create and run the application
if __name__ == "__main__":
    app = ModernRegistrationForm()
    app.run()