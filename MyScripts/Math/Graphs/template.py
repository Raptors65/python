import matplotlib.pyplot as plt

# Graph Settings
X_LABEL = ""
Y_LABEL = ""
TITLE = ""
GRID = True

def create_data():
	# Return a tuple of two lists: the x and the y data.
	pass


data = create_data()
x = data[0]
y = data[1]
plt.plot(x, y)

plt.xlabel(X_LABEL)
plt.ylabel(Y_LABEL)
plt.title(TITLE)
plt.grid(GRID)
plt.show()
