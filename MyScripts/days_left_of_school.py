import datetime as dt

# Constants (change each year)
last_day = dt.date(2019, 6, 27)
holidays = [dt.date(2018, 9, 3), dt.date(2018, 10, 5), dt.date(2018, 10, 8), dt.date(2018, 11, 16), dt.date(2018, 12, 7), dt.date(2018, 12, 24), dt.date(2018, 12, 25), dt.date(2018, 12, 26), dt.date(2018, 12, 27), dt.date(2018, 12, 28), dt.date(2018, 12, 31), dt.date(2019, 1, 1), dt.date(2019, 1, 2), dt.date(2019, 1, 3), dt.date(2019, 1, 4), dt.date(2019, 1, 18), dt.date(2019, 2, 15), dt.date(2019, 2, 18), dt.date(2019, 3, 11), dt.date(2019, 3, 12), dt.date(2019, 3, 13), dt.date(2019, 3, 14), dt.date(2019, 3, 15), dt.date(2019, 4, 19), dt.date(2019, 4, 22), dt.date(2019, 5, 20), dt.date(2019, 6, 7)]

def date_range(start, end):
	"""Returns range of dates (inclusive)."""
	
	# Looping through dates.
	for difference in range((end - start).days + 1):
		# Yielding the date.
		yield start + dt.timedelta(days=difference)

def get_days_left():
	"""Returns the number of days of school left."""
	
	# Counter to store the number of days (today counts).
	days = 0
	# Storing the current date.
	today = dt.date.today()
	
	# Looping through the days between today and the end of school.
	for date in date_range(today, last_day):
		# Making sure it's a school day.
		if date.weekday() not in [5, 6] and date not in holidays:
			# Incrementing the days counter.
			days += 1
	return days

if __name__ == "__main__":
	# Printing the number of days left.
	print("There are " + str(get_days_left()) + " days left of school including today.")
