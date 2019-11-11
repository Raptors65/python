import matplotlib.pyplot as plt
import numpy as np
import math

# Graph Settings
X_LABEL = ""
Y_LABEL = ""
TITLE = ""
GRID = True

def function(x):
	# Return a value from x.
	
	return math.sqrt(1 - (x * x))

def create_data():
	# Return a tuple of two lists: the x and the y data.
	
	x_data = [i for i in np.linspace(0, 1, 1000)]
	y_data = [function(x) for x in x_data]
	
	return (x_data, y_data)


x, y = create_data()
plt.plot(x, y)

plt.xlabel(X_LABEL)
plt.ylabel(Y_LABEL)
plt.title(TITLE)
plt.grid(GRID)
plt.show()
