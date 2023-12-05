import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

# Example data: Times and parking lot occupancy
np.random.seed(0)
times = pd.date_range('2023-01-01 06:00', periods=7, freq='H')
parking_lot_1 = np.random.randint(0, 40, size=(7,))
parking_lot_2 = np.random.randint(0, 40, size=(7,))
parking_lot_3 = np.random.randint(0, 40, size=(7,))

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(12, 6))

# Plot for parking lot occupancy with specific time format
ax1.plot(times, parking_lot_1, lw=2, label='Parking Lot 1')
ax1.plot(times, parking_lot_2, lw=2, label='Parking Lot 2')
ax1.plot(times, parking_lot_3, lw=2, label='Parking Lot 3')
ax1.set_ylabel('Number of Parking Lots')
ax1.legend()
ax1.grid(True)
ax1.set_title('Parking Lot Occupancy Over Time')

# Settings for the time axis
ax1.xaxis.set_major_locator(mdates.HourLocator(interval=1))  # Hourly locator
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:00'))  # Set time format

# Fill Between plot for parking lot occupancy with specific time format
parking_lot_min = min(parking_lot_1.min(), parking_lot_2.min(), parking_lot_3.min())
ax2.fill_between(times, parking_lot_min, parking_lot_1, alpha=0.5, label='Parking Lot 1')
ax2.fill_between(times, parking_lot_min, parking_lot_2, alpha=0.5, label='Parking Lot 2')
ax2.fill_between(times, parking_lot_min, parking_lot_3, alpha=0.5, label='Parking Lot 3')
ax2.legend()
ax2.grid(True)
ax2.set_title('Fill Between: Parking Lot Occupancy Over Time')

# Setting for time axis
ax2.xaxis.set_major_locator(mdates.HourLocator(interval=1))  # Hourly locator
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:00'))  # Set time format

plt.tight_layout()
plt.show()
plt.savefig('fill_between.jpg')
