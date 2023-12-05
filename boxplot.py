import matplotlib.pyplot as plt
import numpy as np

parking_lot_1 = np.random.normal(30, 5, 100)  # Parking time for Parking Lot 1
parking_lot_2 = np.random.normal(40, 8, 100)  # Parking time for Parking Lot 2
parking_lot_3 = np.random.normal(20, 3, 100)  # Parking time for Parking Lot 3

# Combining the data for the boxplot
data = [parking_lot_1, parking_lot_2, parking_lot_3]

# Create a boxplot
plt.boxplot(data)

# Adding title and labels
plt.title('Parking Time at Different Parking Lots')
plt.xlabel('Parking Lots')
plt.ylabel('Parking Time (Minutes)')
plt.xticks(ticks=[1, 2, 3], labels=['Parking Lot 1', 'Parking Lot 2', 'Parking Lot 3'])

# Display the boxplot
plt.show()
plt.savefig('boxplot.jpg')
