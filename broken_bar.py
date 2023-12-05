import matplotlib.pyplot as plt

# Dummy data for parking lot occupancy
parking_lot_1 = [(1, 3), (6, 4), (10, 2)]
parking_lot_2 = [(2, 5), (7, 3), (11, 4)]
parking_lot_3 = [(3, 4), (8, 5), (12, 3)]

fig, ax = plt.subplots(figsize=(10, 6))

# Plot for parking lot occupancy with different colors
ax.broken_barh(parking_lot_1, (1, 1), facecolors='blue', alpha=0.5, label='Parking Lot 1')
ax.broken_barh(parking_lot_2, (3, 1), facecolors='orange', alpha=0.5, label='Parking Lot 2')
ax.broken_barh(parking_lot_3, (5, 1), facecolors='green', alpha=0.5, label='Parking Lot 3')

# Settings for the chart
ax.set_xlabel('Time')
ax.set_yticks([2, 4, 6])
ax.set_yticklabels(['Parking Lot 3', 'Parking Lot 2', 'Parking Lot 1'])
ax.set_ylabel('Parking Lots')
ax.set_title('Broken Barh Chart of Parking Lot Data')
ax.legend()

plt.show()
plt.savefig('brokenbar.jpg')
