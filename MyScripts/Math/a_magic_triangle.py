from itertools import permutations

remaining_numbers = (4, 5, 6, 7, 8, 9)
vertices = (1, 2, 3)


for permutation in permutations(remaining_numbers):
	for vertex1 in range(1, len(remaining_numbers) - 1):
		for vertex2 in range(vertex1 + 1, len(remaining_numbers)):
			if (sum(permutation[:vertex1]) + vertices[0] + vertices[1]) == 17 and (sum(permutation[vertex1:vertex2]) + vertices[1] + vertices[2]) == 17 and (sum(permutation[vertex2:]) + vertices[2] + vertices[0]) == 17:
				print(permutation, vertex1, vertex2)
