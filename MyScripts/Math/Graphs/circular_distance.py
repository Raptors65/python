import matplotlib.pyplot as plt
import numpy as np
import math

# Graph Settings
X_LABEL = "Degrees"
Y_LABEL = "Sum of Dimensions"
TITLE = ""
GRID = True

def function(x):
	# Return a value from x.
	
	x = math.tan(math.radians(x))
	
	a = math.sqrt(1 / (1 + (x * x)))
	b = math.sqrt(1 / ((1 / (x * x)) + 1))
	
	return a + b

def create_data():
	# Return a tuple of two lists: the x and the y data.
	
	x_data = [i for i in range(1, 91)]
	y_data = [1] + [function(x) for x in x_data]
	
	return ([0] + x_data, y_data)


x, y = create_data()
plt.plot(x, y)

plt.xlabel(X_LABEL)
plt.ylabel(Y_LABEL)
plt.title(TITLE)
plt.grid(GRID)
plt.show()
