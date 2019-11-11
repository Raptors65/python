while True:
	text = input("Enter your text:\n")
	print(" ".join(f"{int(bin(ord(character))[2:]):08}" for character in text)),
	print()
