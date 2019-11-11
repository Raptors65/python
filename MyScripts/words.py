from urllib.request import urlopen

words = [word.decode().strip() for word in urlopen("http://www.openbookproject.net/courses/python4fun/_static/spellcheck/spell.words")]

letter_to_numbers = {letter: number for number, letter in enumerate("abcdefghijklmnopqrstuvwxyz", 1)}


for word in words:
	if not all(char in "abcdefghijklmnopqrstuvwxyz" for char in word):
		continue
	if sum(letter_to_numbers[letter] for letter in word) == 42:
		print(word)


