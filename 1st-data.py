import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.plot(x, y)
plt.title('Example Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Save the plot as a file
plt.savefig('Figure_2.png')  # Save in the current working directory
plt.close()  # Close the figure
