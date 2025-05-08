"""
Example 1: Your First Tkinter Window
This demonstrates the basics of creating a Tkinter application window
"""

# Import the tkinter module (we'll use 'tk' as a short name)
import tkinter as tk

# Create the main application window
window = tk.Tk()

# Configure the window
window.title("My First GUI Application")  # Set the window title
window.geometry("400x300")  # Set the window size (width x height)
window.resizable(True, True)  # Allow the window to be resized

# Add a simple label with some welcome text
welcome_label = tk.Label(
    window,  # The parent window
    text="Welcome to Tkinter!",  # The text to display
    font=("Arial", 18),  # Font family and size
    fg="blue"  # Text color
)

# Display the label in the window
welcome_label.pack(pady=50)  # Add some padding around the label

# Create a button that closes the application
exit_button = tk.Button(
    window,
    text="Exit Application",
    command=window.destroy  # This function will be called when the button is clicked
)

# Display the button in the window
exit_button.pack(pady=20)

# Start the main event loop
# This is essential - it processes events and updates the window
window.mainloop()

# Note: Code after mainloop() won't run until the window is closed
print("The application has been closed!")