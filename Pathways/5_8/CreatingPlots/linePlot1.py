import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create and save a plot
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.savefig('my_plot.png')  # This saves the plot as an image
plt.close()  # Clean up

print("Plot saved as 'my_plot.png'")
print("Open the file to see your plot!")