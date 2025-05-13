"""
Topic 5: Building Responsive Interfaces (Simple)
This demonstrates how to create interfaces that adapt when the window is resized
"""

import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Responsive Interface Demo")
window.geometry("600x400")

# Configure rows and columns to make them expandable
# This is the key to creating responsive interfaces!
window.columnconfigure(0, weight=1)  # Left column
window.columnconfigure(1, weight=3)  # Right column - will expand more
window.rowconfigure(1, weight=1)     # Content row will expand

# Create a header that spans across the window
header = tk.Label(
    window,
    text="Responsive Interface Example",
    font=("Arial", 16),
    bg="#4CAF50",
    fg="white",
    pady=10
)
# sticky="ew" makes the header expand horizontally
header.grid(row=0, column=0, columnspan=2, sticky="ew")

# Create a sidebar on the left
sidebar = tk.Frame(window, bg="#f0f0f0", padx=10, pady=10)
# sticky="ns" makes the sidebar expand vertically
sidebar.grid(row=1, column=0, sticky="ns")

# Add some buttons to the sidebar
sidebar_label = tk.Label(sidebar, text="Sidebar", font=("Arial", 12))
sidebar_label.pack(pady=(0, 10))

# Create some buttons for the sidebar
for i in range(1, 6):
    button = tk.Button(sidebar, text=f"Option {i}", width=15)
    button.pack(pady=5)

# Create a main content area that will expand
main_area = tk.Frame(window, bg="white", padx=20, pady=20)
# sticky="nsew" makes the main area expand in all directions
main_area.grid(row=1, column=1, sticky="nsew")

# Configure the main area's row and column to expand
main_area.columnconfigure(0, weight=1)
main_area.rowconfigure(0, weight=0)  # Title (won't expand)
main_area.rowconfigure(1, weight=1)  # Content (will expand)

# Add a title to the main area
main_title = tk.Label(
    main_area,
    text="Main Content Area",
    font=("Arial", 14),
    bg="white"
)
main_title.grid(row=0, column=0, sticky="w", pady=(0, 10))

# Add a text area that will expand with the window
# First, create a frame to hold the text widget and scrollbar
text_frame = tk.Frame(main_area)
text_frame.grid(row=1, column=0, sticky="nsew")

# Add a scrollbar
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Add a text widget that will expand
text_widget = tk.Text(
    text_frame,
    wrap="word",
    yscrollcommand=scrollbar.set,
    font=("Arial", 11)
)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=text_widget.yview)

# Add some sample text content
sample_text = """
This is a simple example of a responsive interface in Tkinter.

What makes this interface responsive:

1. We used grid.columnconfigure() and grid.rowconfigure() 
   with weight parameters to make certain rows and columns expandable.

2. We used the sticky parameter to make widgets expand within their grid cells:
   - "ew" for horizontal expansion (east-west)
   - "ns" for vertical expansion (north-south)
   - "nsew" for expansion in all directions

3. We used nested frames to organize related elements.

4. We created a scrollable text area for content that might not fit.

Try resizing this window now!
- The header will stretch horizontally
- The sidebar will stretch vertically
- The main area will expand both horizontally and vertically
- The text area will grow with the main area

This approach creates interfaces that look good at different window sizes.
"""
text_widget.insert(tk.END, sample_text)

# Create a footer
footer = tk.Label(
    window,
    text="Resize the window to see how the elements adapt!",
    bg="#f0f0f0",
    pady=5
)
footer.grid(row=2, column=0, columnspan=2, sticky="ew")

# Start the main event loop
window.mainloop()