from itertools import combinations

rows_and_columns = ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15), (0, 4, 8, 12), (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15))

possible_boards = combinations(range(16), 10)
for board in possible_boards:
	for line in rows_and_columns:
		if len([cell for cell in line if cell in board]) % 2 != 0:
			break
	else:
		print(board)
