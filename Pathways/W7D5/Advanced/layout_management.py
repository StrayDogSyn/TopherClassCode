"""
Topic 4: Layout Management in Tkinter (Simple)
This demonstrates the three basic geometry managers: pack, grid, and place
"""

import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Layout Managers Demo")
window.geometry("500x400")

# Create a notebook with tabs for each layout manager
import tkinter.ttk as ttk
tab_control = ttk.Notebook(window)

# ============ 1. PACK LAYOUT DEMO ============
pack_tab = ttk.Frame(tab_control)
tab_control.add(pack_tab, text="Pack Layout")

# Add a title
pack_title = tk.Label(pack_tab, text="Pack Layout Example", font=("Arial", 14))
pack_title.pack(pady=10)  # Add some padding above and below

# Add some buttons using pack
button1 = tk.Button(pack_tab, text="Button 1")
button1.pack()  # Default is top

button2 = tk.Button(pack_tab, text="Button 2")
button2.pack(pady=10)  # Add padding above and below

button3 = tk.Button(pack_tab, text="Button 3 (Left)")
button3.pack(side="left", padx=10)  # Pack to the left side

button4 = tk.Button(pack_tab, text="Button 4 (Right)")
button4.pack(side="right", padx=10)  # Pack to the right side

# Add explanation
pack_explanation = tk.Label(
    pack_tab,
    text="""
    Pack Layout:
    - Simple to use for basic layouts
    - Arranges widgets in order (top to bottom by default)
    - Use side='left'/'right'/'top'/'bottom' to control direction
    - Good for simple rows or columns of widgets
    """,
    justify="left"
)
pack_explanation.pack(side="bottom", pady=20)

# ============ 2. GRID LAYOUT DEMO ============
grid_tab = ttk.Frame(tab_control)
tab_control.add(grid_tab, text="Grid Layout")

# Add a title
grid_title = tk.Label(grid_tab, text="Grid Layout Example", font=("Arial", 14))
grid_title.grid(row=0, column=0, columnspan=2, pady=10)

# Create a simple form using grid
name_label = tk.Label(grid_tab, text="Name:")
name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")  # Right-aligned

name_entry = tk.Entry(grid_tab)
name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # Left-aligned

email_label = tk.Label(grid_tab, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

email_entry = tk.Entry(grid_tab)
email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

submit_button = tk.Button(grid_tab, text="Submit")
submit_button.grid(row=3, column=0, columnspan=2, pady=10)  # Spans both columns

# Add explanation
grid_explanation = tk.Label(
    grid_tab,
    text="""
    Grid Layout:
    - Arranges widgets in rows and columns
    - Specify position with row and column indices
    - Use columnspan/rowspan to make widgets span multiple cells
    - Perfect for forms and table-like layouts
    """,
    justify="left"
)
grid_explanation.grid(row=4, column=0, columnspan=2, pady=20)

# ============ 3. PLACE LAYOUT DEMO ============
place_tab = ttk.Frame(tab_control)
tab_control.add(place_tab, text="Place Layout")

# Add a title
place_title = tk.Label(place_tab, text="Place Layout Example", font=("Arial", 14))
place_title.place(x=150, y=10)  # Absolute positioning

# Add buttons using place with absolute positioning
button1 = tk.Button(place_tab, text="Top-Left")
button1.place(x=50, y=50)

button2 = tk.Button(place_tab, text="Top-Right")
button2.place(x=350, y=50)

button3 = tk.Button(place_tab, text="Bottom-Left")
button3.place(x=50, y=250)

button4 = tk.Button(place_tab, text="Bottom-Right")
button4.place(x=350, y=250)

button5 = tk.Button(place_tab, text="Center")
button5.place(x=200, y=150)

# Add explanation
place_explanation = tk.Label(
    place_tab,
    text="""
    Place Layout:
    - Positions widgets using x, y coordinates
    - Gives precise control over widget placement
    - Can use absolute position (pixels) or relative (0.0 to 1.0)
    - Good for absolute positioning and overlapping widgets
    """,
    justify="left"
)
place_explanation.place(x=100, y=300)

# Display the tab control
tab_control.pack(expand=1, fill="both")

# Start the main event loop
window.mainloop()