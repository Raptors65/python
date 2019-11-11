import matplotlib.pyplot as plt
from decimal import Decimal
import math

# Graph Settings
X_LABEL = ""
Y_LABEL = ""
TITLE = ""
GRID = True

def create_data():
	x_data = list(range(361))
	y_data = [abs(x - ((12 * x) % 360)) for x in x_data]
	print(list(filter(lambda x: y_data[x] < 10, x_data)))
	return (x_data, y_data)

def get_exact_value(x):
	return x + ((x - (x * 12 % 360)) / 11)

def get_time(x):
	return f"{math.floor(x / 360 * 12)}:{round(x / 360 * 60):02d}"

data = create_data()
x = data[0]
y = data[1]
plt.plot(x, y)

plt.xlabel(X_LABEL)
plt.ylabel(Y_LABEL)
plt.title(TITLE)
plt.grid(GRID)
plt.show()
