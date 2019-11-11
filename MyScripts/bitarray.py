# TODO:
# • implement __setitem__ for slices, __delitem__
# • implement list methods (e.g. insert)
# • implement __repr__, __str__, etc.
# • implement __add__
# • add more ways to initialize list

# POSSIBLE IMPROVEMENTS:
# • optimize extend to not have lots of calls to
#   append

# INFO:
# • Items are accessed by using the & operator
#   with powers of 2, then shifting the value
#   back to the ones place.
# • Slices simply use loop through indices, using
#   the above.

# COMPLETED:
# • __init__
# • __getitem__, __setitem__ for integers
# • append, extend
# • type errors for __getitem__, __setitem__


class BitArray:
	"""Defines a boolean array with bits."""
	
	def __init__(self, length):
		"""Initializes the list with True."""
		
		# Making the bytearray that this list is based off of.
		self._bytearray = bytearray([0]) * ((length - 1) // 8 + 1)
		# Storing the length to keep leading 0s.
		self._length = length
	
	def __getitem__(self, index):
		"""Gets the value of an index or slice."""
		
		# Checking if the type is an int or a slice.
		if isinstance(index, int):
			# Checking if the index is positive or negative.
			if index >= 0:
				# Making sure the index is in range.
				if index < len(self):
					# Accessing the value at this position.
					return bool((self._bytearray[index // 8] & (2 ** (7 - (index % 8)))) >> (7 - (index % 8)))
				else:
					# Raising an IndexError.
					raise IndexError("BitArray index out of range")
			else:
				# Converting the index to the equivalent positive.
				index = len(self) - (-index)
				# Making sure the index is in range (other way because index won't be >= len(self) here)
				if index >= 0:
					# Accessing the value at this position.
					return bool((self._bytearray[index // 8] & (2 ** (7 - (index % 8)))) >> (7 - (index % 8)))
				else:
					# Raising an IndexError.
					raise IndexError("BitArray index out of range")
		elif isinstance(index, slice):
			# Converting the slice to a tuple usable for looping.
			indices = index.indices(len(self))
			# Making a bitarray to store the values.
			values = BitArray(len(range(*indices)))
			# Looping through the indices.
			for i in range(*indices):
				# Storing the value.
				values.append(self[i])
			# Returning the values.
			return values
		else:
			# Raising TypeError.
			raise TypeError("BitArray indices must be integers or slices, not " + type(index).__name__)
	
	def __setitem__(self, index, value):
		"""Sets the value of an index or slice."""
		
		# Casting value to bool.
		value = bool(value)
		# Checking if the index is an int or a slice.
		if isinstance(index, int):
			# Checking if the index is positive or negative.
			if index >= 0:
				# Making sure the index is in range.
				if index < len(self):
					# Checking if value is true or false and if the specified bit is set to something else.
					if value == True and self[index] == False:
						# Changing specified bit.
						self._bytearray[index // 8] += (2 ** (7 - (index % 8)))
					elif value == False and self[index] == True:
						# Changing specified bit.
						self._bytearray[index // 8] -= (2 ** (7 - (index % 8)))
				else:
					# Raising an IndexError.
					raise IndexError("BitArray assignment index out of range")
			else:
				# Converting the index to the equivalent positive.
				index = len(self) - (-index)
				# Making sure the index is in range (other way because index won't be >= len(self) here)
				if index >= 0:
					# Checking if value is true or false and if the specified bit is set to something else.
					if value == True and self[index] == False:
						# Changing specified bit.
						self._bytearray[index // 8] += (2 ** (7 - (index % 8)))
					elif value == False and self[index] == True:
						# Changing specified bit.
						self._bytearray[index // 8] -= (2 ** (7 - (index % 8)))
				else:
					# Raising an IndexError.
					raise IndexError("BitArray index out of range")
		elif isinstance(index, slice):
			# Looping through the indices.
			for i in range(*index.indices(len(self))):
				# TODO: find out how slice assignment works
				pass
		else:
			# Raising TypeError.
			raise TypeError("BitArray indices must be integers or slices, not " + type(index).__name__)
				
	def __len__(self):
		"""Returns the length of this bitarray."""
		
		# Returning the stored length.
		return self._length
	
	def __add__(self, other):
		pass
	
	def __str__(self):
		"""Returns a string representation of this bitarray."""
		
		# Looping through bits, converting to a string, and returning.
		return "".join(str(int(bit)) for bit in self)
	
	def append(self, value):
		"""Appends a value to the bitarray.
		
		Value is converted to a bool before appending.
		"""
		
		# Casting value to bool.
		value = bool(value)
		
		# Checking if the current length makes full use of the bytes.
		if (len(self) % 8) == 0:
			# Adding a byte to the bytearray.
			self._bytearray.append(0)
		
		# Increasing the length.
		self._length += 1
		# Setting the bit.
		self[-1] = value
	
	def extend(self, iterable):
		"""Appends values in an iterable to the bitarray.
		
		Values are converted to a bool before appending.
		"""
		
		# Looping through items in iterable.
		for item in iterable:
			# Appending the item.
			self.append(item)
