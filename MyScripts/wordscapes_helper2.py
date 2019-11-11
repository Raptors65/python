from itertools import chain, permutations
from urllib.request import urlopen

LETTERS = "sseema"
words = {word.decode().strip() for word in urlopen("http://www.openbookproject.net/courses/python4fun/_static/spellcheck/spell.words")}
valid_words = words.intersection("".join(word) for word in chain.from_iterable(permutations(LETTERS, length) for length in range(3, len(LETTERS) + 1)))

for word in sorted(valid_words):
	print(word)
