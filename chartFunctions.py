import matplotlib.pyplot as plt
import numpy as np

"""
# Read data from text file
data_file = "results/distances.txt"
with open(data_file, "r") as file:
    lines = file.readlines()

# Process data
data = []
for line in lines:
    row = [float(value.strip()) for value in line.split(",")]
    data.append(row)

# Extracting data columns
distances_without_random_edges = [row[0] for row in data]
a_star_distances = [row[1] for row in data]
enhanced_algorithm_distances = [row[2] for row in data]

# Plotting the graph
plt.plot(distances_without_random_edges, label="Without Random Edges")
plt.plot(a_star_distances, label="A* Algorithm")
plt.plot(enhanced_algorithm_distances, label="Enhanced Algorithm")
plt.xlabel("Data Points")
plt.ylabel("Distances")
plt.title("Comparison of Distances")
plt.legend()
plt.show()"""

import matplotlib.pyplot as plt
import numpy as np

# Data for the result sets
data = {
    "Result Set 1": {
        "A*": {"Distance": 2618.61, "Loop Count": 70},
        "Enhanced A*": {"Distance": 2950.35, "Loop Count": 278}
    },
    "Result Set 2": {
        "A*": {"Distance": 4387.37, "Loop Count": 170},
        "Enhanced A*": {"Distance": 4966.29, "Loop Count": 705}
    },
    "Result Set 3": {
        "A*": {"Distance": 3743.31, "Loop Count": 176},
        "Enhanced A*": {"Distance": 4479.53, "Loop Count": 454}
    }
}


# Function to create grouped bar charts
def create_grouped_bar_chart(result_set, data):
    algorithms = list(data[result_set].keys())
    attributes = list(data[result_set][algorithms[0]].keys())

    values = {attr: [data[result_set][alg][attr] for alg in algorithms] for attr in attributes}

    x = np.arange(len(attributes))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()

    # Prettier colors
    colors = ['#ffcc00', '#ff7f0e']  # yellow, orange

    # Plot each algorithm's bars
    for i, alg in enumerate(algorithms):
        ax.bar(x + i * width - width / 2, [values[attr][i] for attr in attributes], width, label=alg, color=colors[i])

    # Add labels, title, and custom x-axis tick labels
    ax.set_xlabel('Attributes')
    ax.set_ylabel('Values')
    ax.set_title(result_set)
    ax.set_xticks(x)
    ax.set_xticklabels(attributes)
    ax.legend()

    # Add value labels on bars
    for i, alg in enumerate(algorithms):
        for j, attr in enumerate(attributes):
            value = values[attr][i]
            ax.text(j + i * width - width / 2, value + (0.05 * value), f'{value:.2f}', ha='center', color=colors[i])

    fig.tight_layout()
    plt.show()


# Create charts for each result set
for result_set in data:
    create_grouped_bar_chart(result_set, data)
