import itertools
import ui
from urllib.request import urlopen

# Opening the file with the words.
with open("scrabble_words.txt") as words_file:
	# Storing a set of English words.
	words = {word.rstrip() for word in words_file.readlines()}

# Run when button to find valid words is pressed.
def find_words(sender):
	'@type sender: ui.Button'
	
	# Getting the characters entered by the user.
	characters = sender.superview["characters"].text.upper()
	# Getting the placed characters entered by the user.
	placed_characters = sender.superview["placed_characters"].text.upper()
	# Getting all the permutations of the characters and finding the ones that are in the list of English words.
	valid_words = words.intersection("".join(word)[:index] + placed_characters + "".join(word)[index:] for word in itertools.chain.from_iterable(itertools.permutations(characters, length) for length in range(2, len(characters) + 1)) for index in range(len(word) + 1))
	# Printing the words to the output text box.
	sender.superview["words_output"].text = "\n".join(sorted(valid_words, key=lambda x: len(x), reverse=True))

# Run when clear button is pressed.
def clear_field(sender):
	'@type sender: ui.Button'
	
	# Clearing the output text box.
	sender.superview["words_output"].text = ""
	

v = ui.load_view()
v.present('sheet')
