import sqlite3
import console

# Connecting to a specified database.
chosen_database = input("Choose a database (if it doesn't exist, it will be created): ")
connection = sqlite3.connect(f"{chosen_database}.db")

# Getting the cursor.
c = connection.cursor()

# Telling the user how to exit.
print("Type exit() to exit.")	
# Looping forever.
while True:
	# Getting the input.
	user_input = input(">>> ")
	
	# Checking if the input is exit().
	if user_input == "exit()":
		# Saving the changes.
		connection.commit()
		# Closing the connection.
		connection.close()
		# Exiting the loop.
		break
	else:
		try:
			# Executing the code.
			c.execute(user_input)
		except sqlite3.OperationalError as e:
			print("The following error occurred:")
			console.set_color(255, 0, 0)
			print(e)
			console.set_color(255, 255, 255)
			continue
		# Checking if it was a SELECT statement.
		if user_input.lower().startswith("select"):
			# Fetching all the results.
			print(c.fetchall())
