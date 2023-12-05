import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Coordinates
x_dach = [-0.5, 0, 0.5, -0.5]
y_dach = [0.5, 1, 0.5, 0.5]

x_wand = [-0.5, -0.5, 0.5, 0.5, -0.5]
y_wand = [0, 0.5, 0.5, 0, 0]

x_tuer = [-0.1, -0.1, 0.1, 0.1, -0.1]
y_tuer = [0, 0.4, 0.4, 0, 0]

fig, ax = plt.subplots(figsize=(6, 6))

# Polygon-Patches for House
dach = Polygon(xy=list(zip(x_dach, y_dach)), closed=True, edgecolor='black', facecolor='red')
wand = Polygon(xy=list(zip(x_wand, y_wand)), closed=True, edgecolor='black', facecolor='white')
tuer = Polygon(xy=list(zip(x_tuer, y_tuer)), closed=True, edgecolor='black', facecolor='black')

# Add parts of house to diagram
ax.add_patch(dach)
ax.add_patch(wand)
ax.add_patch(tuer)

# Diagram
ax.set_aspect('equal')
ax.set_xlim(-1, 1)
ax.set_ylim(0, 1.5)
ax.set_xlabel('X-Achse')
ax.set_ylabel('Y-Achse')
ax.set_title('House in Matplotlib')

plt.show()
plt.savefig('filled_polygon.jpg')
