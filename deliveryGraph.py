import matplotlib.pyplot as plt
import numpy as np

# Number of vertices
V = np.linspace(1, 5, 100)  # From 1 to 1000 vertices
E = V * (V - 1) / 2  # Maximum number of edges in a complete graph (complete graph)

# Time complexity functions
def best_case(V):
    return V**2

def average_case(V, E):
    return V**2 + E

def worst_case(V, E):
    return V**2 + E

# Calculate time complexities
best = best_case(V)
average = average_case(V, E)
worst = worst_case(V, E)

# Plotting
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Plot Best Case
axs[0].plot(V, best, label='Best Case: O(V^2)', color='green')
axs[0].set_xlabel('Number of Vertices (V)')
axs[0].set_ylabel('Time Complexity')
axs[0].set_title('Best Case Time Complexity of Dijkstra\'s Algorithm')
axs[0].legend()
axs[0].grid(True)
axs[0].set_yscale('log')  # Use logarithmic scale for better visualization

# Plot Average Case
axs[1].plot(V, average, label='Average Case: O(V^2 + E)', color='orange')
axs[1].set_xlabel('Number of Vertices (V)')
axs[1].set_ylabel('Time Complexity')
axs[1].set_title('Average Case Time Complexity of Dijkstra\'s Algorithm')
axs[1].legend()
axs[1].grid(True)
axs[1].set_yscale('log')  # Use logarithmic scale for better visualization

# Plot Worst Case
axs[2].plot(V, worst, label='Worst Case: O(V^2 + E)', color='red')
axs[2].set_xlabel('Number of Vertices (V)')
axs[2].set_ylabel('Time Complexity')
axs[2].set_title('Worst Case Time Complexity of Dijkstra\'s Algorithm')
axs[2].legend()
axs[2].grid(True)
axs[2].set_yscale('log')  # Use logarithmic scale for better visualization

# Adjust layout
plt.tight_layout()
plt.show()
