import matplotlib.pyplot as plt
import numpy as np

# Categories and results (example values)
categories = ['Empty', 'Partially Occupied', 'Full']
parking_lot_1 = [20, 30, 10]
parking_lot_2 = [15, 25, 20]
parking_lot_3 = [10, 35, 15]

num_categories = len(categories)
bar_width = 0.2  # Width of the bars

# Bar positions for each category
bar_positions_1 = np.arange(num_categories)
bar_positions_2 = [pos + bar_width for pos in bar_positions_1]
bar_positions_3 = [pos + bar_width * 2 for pos in bar_positions_1]

# Creating the bar chart
plt.figure(figsize=(8, 5))

plt.barh(bar_positions_1, parking_lot_1, height=bar_width, label='Parking Lot 1')
plt.barh(bar_positions_2, parking_lot_2, height=bar_width, label='Parking Lot 2')
plt.barh(bar_positions_3, parking_lot_3, height=bar_width, label='Parking Lot 3')

# Adding labels and title
plt.xlabel('Number of Parking Lots')
plt.yticks([pos + bar_width for pos in range(num_categories)], categories)
plt.ylabel('Parking Lot Occupancy')
plt.title('Parking Lot Occupancy by Category')

plt.legend()
plt.tight_layout()

# Display the chart
plt.show()
plt.savefig('colored_lines.jpg')
