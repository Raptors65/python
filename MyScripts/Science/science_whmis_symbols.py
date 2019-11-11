"""A program to help with studying WHMIS symbols."""

# Imports
from PIL import Image
from random import sample

# Classes
class WHMISClass:
	"""Represents a class in WHMIS."""
	
	def __init__(self, name, risks, handling, examples):
		"""Initializes a WHMIS class."""
		
		# Initializing all the properties.
		self.name = name
		self.risks = risks
		self.handling = handling
		self.examples = examples

# Constants
WHMIS_CLASSES = {
	"class_a.png": WHMISClass("Class A: Compressed Gas", ["explodes from pressure, heat, and when dropped"], ["store in cool place", "do not drop"], ["oxygen tanks", "fire extinguishers"]),#break
	"class_b.png": WHMISClass("Class B: Flammable and Combustible Material", ["contents burn easily when exposed to heat, flame, or spark"], ["store in well-ventilated area", "keep away from heat, flame, and spark", "never smoke near"], ["paper", "gasoline"]),#break
	"class_c.png": WHMISClass("Class C: Oxidizing Material", ["makes flammable materials burn more easily"], ["store/use in well-ventilated area", "keep away from heat, flame, and spark"], ["oxygen tanks", "hydrogen peroxide"])
}

# Global Variables
correct_answers = 0
total_answers = 0

# Functions
def ask_question(prompt, answers):
	"""Gets answers from the user for the specified question."""
	
	# Opening access to the global counters.
	global correct_answers, total_answers
	
	# Checking if answers is a list.
	if isinstance(answers, list):
                # Prompting the user.
		print(prompt)
		# Looping through the answers.
		for answer in answers:
			# Printing a mark to show that an answer is expected.
			user_input = input("- ")
			# Comparing the input to the correct answer.
			if user_input != answer:
				# Printing that the user got it wrong.
				print(f"Wrong, the correct answer is \"{answer}\".")
			else:
				# Storing the correct answer.
				correct_answers += 1
			# Incrementing the answers counter.
			total_answers += 1
	else:
		# Asking the user the question.
		user_input = input(prompt)
		# Comparing the input to the correct answer.
		if user_input != answers:
			# Printing that the user got it wrong.
			print(f"Wrong, the correct answer is \"{answer}\".")
		else:
			# Storing the correct answer.
			correct_answers += 1
		# Incrementing the answers counter.
		total_answers += 1

def test_class(image_filename):
	"""Tests the user on the specified WHMIS class."""
	
	# Opening the image.
	image = Image.open(image_filename)
	# Printing the image.
	image.show()
	
	# Getting the WHMIS class data.
	whmis_class = WHMIS_CLASSES[image_filename]
	
	# Asking the user about all the info about the WHMIS class.
	ask_question("Class name: ", whmis_class.name)
	ask_question("Risks: ", whmis_class.risks)
	ask_question("Handling: ", whmis_class.handling)
	ask_question("Examples: ", whmis_class.examples)

# Main
if __name__ == "__main__":
	# Looping through all the WHMIS classes after shuffling.
	for whmis_class in sample(list(WHMIS_CLASSES), len(WHMIS_CLASSES)):
		# Testing the user about this class.
		test_class(whmis_class)
	# Printing the results.
	print()
	print(f"You got {round(correct_answers / total_answers * 100, 2)}% ({correct_answers}/{total_answers}) right.")
