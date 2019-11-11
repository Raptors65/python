import itertools
import ui
import re
from urllib.request import urlopen

# Opening the file with the words.
with open("words.txt") as words_file:
	# Storing a set of English words.
	words = {word.rstrip() for word in words_file.readlines()}

# Run when button to find valid words is pressed.
def find_words(sender):
	# Getting the characters entered by the user.
	characters = sender.superview["characters"].text.lower()
	# Compiling the regular expression.
	exp = re.compile(sender.superview["regular_expression"].text.lower())
	# Getting all the permutations of the characters and finding the ones that are in the list of English words and match the regular expression.
	valid_words = words.intersection(contructed_word for contructed_word in (
		"".join(word) for word in itertools.chain.from_iterable(itertools.permutations(characters, length)
			for length in range(3, len(characters) + 1))
	) if exp.fullmatch(contructed_word) is not None)
	# Printing the words to the output text box.
	sender.superview["words_output"].text = "\n".join(sorted(valid_words))

# Run when clear button is pressed.
def clear_field(sender):
	'@type sender: ui.Button'
	
	# Clearing the output text box.
	sender.superview["words_output"].text = ""

# Run when text field is done editing.
def text_field_exited(sender):
	'@type sender: ui.TextField'
	
	# Getting the possible words with the letters in the text field.
	find_words(sender)

v = ui.load_view()
v.present('sheet')
