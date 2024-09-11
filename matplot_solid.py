import matplotlib.pyplot as plt
import numpy as np

# Define the x and y values
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot


# Fill the area under the curve
plt.fill_between(x, y, alpha=0.5)

# Add labels and title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Solid Infill Under Sine Wave')
plt.legend()

# Show the plot
plt.show()
