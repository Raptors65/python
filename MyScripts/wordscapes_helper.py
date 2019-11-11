from itertools import permutations
from urllib.request import urlopen

LETTERS = "sseema"
words = [word.decode().strip() for word in urlopen("http://www.openbookproject.net/courses/python4fun/_static/spellcheck/spell.words")]
valid_words = []

for length in range(3, len(LETTERS) + 1):
	for possible_word in permutations(LETTERS, length):
		if "".join(possible_word) in words:
			valid_words.append("".join(possible_word))

for word in sorted(set(valid_words)):
	print(word)
