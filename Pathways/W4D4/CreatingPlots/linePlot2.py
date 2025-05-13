import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a more customized plot
fig, ax = plt.subplots(figsize=(12, 7))
print(fig)
print(ax)

# Custom line style, color, and markers
ax.plot(x, y, linestyle='--', color='blue', linewidth=2, marker='o', 
        markersize=5, markerfacecolor='red', label='Sine Wave')
ax.plot(x, np.cos(x), linestyle='-', color='green', linewidth=2, 
        marker='^', markersize=5, label='Cosine Wave')

# Add a horizontal line at y=0
ax.axhline(y=0, color='black', linestyle='-', alpha=0.3)

# Customize title and labels with fonts
ax.set_title('Sine and Cosine Waves', fontsize=16, fontweight='bold')
ax.set_xlabel('X-axis', fontsize=12)
ax.set_ylabel('Y-axis', fontsize=12)

# Customize grid
ax.grid(True, linestyle=':', alpha=0.7)

# Customize axis limits
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

# Add a legend
ax.legend(loc='upper right', frameon=True, shadow=True)

# Add text annotation
ax.annotate('Maximum', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.3),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

plt.savefig('my_plot.png')  # This saves the plot as an image
plt.close()  # Clean up

print("Plot saved as 'my_plot.png'")
print("Open the file to see your plot!")
