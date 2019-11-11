import copy

def permutations(remaining_chars, length, used_chars=""):
	"""Returns the permutations of a certain length for a string."""
	
	# Checking if we're at the bottom of the tree.
	if length == 0:
		# Returning a list with the permutation.
		return [used_chars]
	
	# List to store the permutations.
	permutations_found = []
	# Looping through the possible characters to add.
	for char in range(len(remaining_chars)):
		# Moving through the tree.
		permutations_found.extend(permutations(remaining_chars[:char] + remaining_chars[char + 1:], length - 1,
		used_chars + remaining_chars[char]))
	# Returning the list of permutations.
	return permutations_found

def permutations2(string, length):
	"""Gets all the permutations of a string using a non-recursive algorithm."""
	
	# List to store the partial permutations found.
	partial_permutations = []
	
	# Initializing the partial permutations.
	for char in string:
		# Temporary copy of string.
		new_string = list(string)
		# Removing the character.
		new_string.remove(char)
		# Storing both values as a tuple.
		partial_permutations.append(("".join(new_string), char))
	
	# Looping to certain length.
	for length in reversed(range(1, length)):
		# List to store the new partial permutations.
		new_partial_permutations = []
		# While there are still old partial permutations:
		while partial_permutations:
			# Storing the partial permutation.
			partial_permutation = partial_permutations.pop()
			# Looping through the remaining characters.
			for char in partial_permutation[0]:
				# Making a copy of the remaining characters.
				remaining_chars = list(partial_permutation[0])
				# Removing the character.
				remaining_chars.remove(char)
				# Making a copy of the new string.
				new_string = partial_permutation[1]
				# Adding the character to the string.
				new_string += char
				# Storing the partial permutation.
				new_partial_permutations.append(("".join(remaining_chars), new_string))
		# Updating the list of partial permutations.
		partial_permutations = copy.deepcopy(new_partial_permutations)
	return [permutation[1] for permutation in partial_permutations]
