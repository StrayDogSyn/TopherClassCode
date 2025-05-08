"""
Example 2: Window Management and Properties
This demonstrates window configuration options and creating additional windows
"""

import tkinter as tk
from tkinter import messagebox  # Import for message boxes

def open_new_window():
    # Create a new window (Toplevel widget)
    new_window = tk.Toplevel(main_window)
    new_window.title("Secondary Window")
    new_window.geometry("300x200")
    
    # Make it a modal window (must be closed before returning to the main window)
    new_window.grab_set()
    
    # Add some content to the new window
    label = tk.Label(new_window, text="This is a secondary window!", font=("Arial", 12))
    label.pack(pady=20)
    
    # Add a button to close this window
    close_button = tk.Button(new_window, text="Close Window", command=new_window.destroy)
    close_button.pack(pady=10)

def show_message():
    # Display a simple message box
    messagebox.showinfo("Information", "This is an information message!")

def confirm_exit():
    # Ask for confirmation before exiting
    result = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
    if result:
        main_window.destroy()

# Create the main window
main_window = tk.Tk()
main_window.title("Window Management Demo")
main_window.geometry("500x400+100+100")  # width x height + x position + y position

# Customize the window appearance
main_window.configure(bg="#f0f0f0")  # Set background color

# Add a title label
title_label = tk.Label(
    main_window,
    text="Window Management Demo",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0"
)
title_label.pack(pady=20)

# Create buttons for different actions
new_window_button = tk.Button(
    main_window,
    text="Open New Window",
    command=open_new_window,
    width=20,
    height=2
)
new_window_button.pack(pady=10)

message_button = tk.Button(
    main_window,
    text="Show Message",
    command=show_message,
    width=20,
    height=2
)
message_button.pack(pady=10)

exit_button = tk.Button(
    main_window,
    text="Exit Application",
    command=confirm_exit,
    width=20,
    height=2
)
exit_button.pack(pady=10)

# Set up a protocol handler for the window close button (X)
main_window.protocol("WM_DELETE_WINDOW", confirm_exit)

# Start the main event loop
main_window.mainloop()