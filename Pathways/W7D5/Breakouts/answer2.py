import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Contact Us Form")
window.geometry("500x450")

# Make the window responsive
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)  # Content row will expand

# =============================================================================
# TASK 1 & 3: Create frames for organization
# =============================================================================

# Header frame
header_frame = tk.Frame(window, bg="#4CAF50", padx=10, pady=10)
header_frame.grid(row=0, column=0, sticky="ew")

header_label = tk.Label(
    header_frame,
    text="Contact Us",
    font=("Arial", 16, "bold"),
    bg="#4CAF50",
    fg="white"
)
header_label.pack()

# Content frame (will expand)
content_frame = tk.Frame(window, bg="#f9f9f9", padx=20, pady=20)
content_frame.grid(row=1, column=0, sticky="nsew")

# Make the content frame responsive
content_frame.columnconfigure(1, weight=1)  # Entry column expands
content_frame.rowconfigure(3, weight=1)     # Message row expands

# Footer frame
footer_frame = tk.Frame(window, bg="#f0f0f0", padx=10, pady=10)
footer_frame.grid(row=2, column=0, sticky="ew")

footer_label = tk.Label(
    footer_frame,
    text="© 2025 My Company",
    font=("Arial", 8),
    bg="#f0f0f0"
)
footer_label.pack()

# =============================================================================
# TASK 1 & 2: Create form using grid layout
# =============================================================================

# Define a common font for all labels
label_font = ("Arial", 10)
entry_width = 40

# Name field
name_label = tk.Label(
    content_frame,
    text="Name:",
    font=label_font,
    bg="#f9f9f9"
)
name_label.grid(row=0, column=0, sticky="e", padx=5, pady=10)

name_entry = tk.Entry(content_frame, width=entry_width)
name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=10)

# Email field
email_label = tk.Label(
    content_frame,
    text="Email:",
    font=label_font,
    bg="#f9f9f9"
)
email_label.grid(row=1, column=0, sticky="e", padx=5, pady=10)

email_entry = tk.Entry(content_frame, width=entry_width)
email_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=10)

# Subject field
subject_label = tk.Label(
    content_frame,
    text="Subject:",
    font=label_font,
    bg="#f9f9f9"
)
subject_label.grid(row=2, column=0, sticky="e", padx=5, pady=10)

subject_entry = tk.Entry(content_frame, width=entry_width)
subject_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=10)

# Message field (multiline Text widget)
message_label = tk.Label(
    content_frame,
    text="Message:",
    font=label_font,
    bg="#f9f9f9"
)
message_label.grid(row=3, column=0, sticky="ne", padx=5, pady=10)

# Text widget with scrollbar
message_frame = tk.Frame(content_frame, bg="#f9f9f9")
message_frame.grid(row=3, column=1, sticky="nsew", padx=5, pady=10)

# Make the message frame responsive
message_frame.columnconfigure(0, weight=1)
message_frame.rowconfigure(0, weight=1)

message_scrollbar = tk.Scrollbar(message_frame)
message_scrollbar.grid(row=0, column=1, sticky="ns")

message_text = tk.Text(
    message_frame,
    width=30,
    height=5,
    yscrollcommand=message_scrollbar.set
)
message_text.grid(row=0, column=0, sticky="nsew")
message_scrollbar.config(command=message_text.yview)

# Submit button
submit_button = tk.Button(
    content_frame,
    text="Submit",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=20,
    pady=5
)
submit_button.grid(row=4, column=0, columnspan=2, pady=15)

# Start the main event loop
window.mainloop()