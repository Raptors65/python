import datetime as dt
import appex
import ui

# Constants (change each year)
last_day = dt.date(2020, 6, 25)
holidays = [dt.date(2019, 9, 2), dt.date(2019, 10, 11), dt.date(2019, 10, 14), dt.date(2019, 11, 15), dt.date(2019, 12, 6), dt.date(2019, 12, 23), dt.date(2019, 12, 24), dt.date(2019, 12, 25), dt.date(2019, 12, 26), dt.date(2019, 12, 27), dt.date(2019, 12, 30), dt.date(2019, 12, 31), dt.date(2020, 1, 1), dt.date(2020, 1, 2), dt.date(2020, 1, 3), dt.date(2020, 1, 17), dt.date(2020, 2, 14), dt.date(2020, 2, 17), dt.date(2020, 3, 16), dt.date(2020, 3, 17), dt.date(2020, 3, 18), dt.date(2020, 3, 19), dt.date(2020, 3, 20), dt.date(2020, 4, 10), dt.date(2020, 4, 13), dt.date(2020, 5, 18), dt.date(2020, 6, 5)]

def date_range(start, end):
	"""Returns range of dates (inclusive)."""
	
	# Looping through dates.
	for difference in range((end - start).days + 1):
		# Yielding the date.
		yield start + dt.timedelta(days=difference)

def get_days_left():
	"""Returns the number of days of school left."""
	
	# Counter to store the number of days.
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

# Creating a label.
label = ui.Label(font=("<system>", 16), alignment=ui.ALIGN_CENTER)
# Adding text to the label.
label.text = "Including today, there are " + str(get_days_left()) + " days left of school."
# Setting the number of lines to 0 so that it's set automatically.
label.number_of_lines = 0
# Adding the label as a widget.
appex.set_widget_view(label)
