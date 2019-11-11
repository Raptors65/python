from urllib.request import urlopen

words = [word.decode().strip() for word in urlopen("http://www.openbookproject.net/courses/python4fun/_static/spellcheck/spell.words")]

for word in words:
	if not all(char in "abcdefghijklmnopqrstuvwxyz" for char in word):
		continue
	if "" in word:
		print(word)

