from itertools import product
from multiprocessing import Pool

START_MONEY = 10
BET_MONEY = 1
MAX_FLIPS = 20

results = {i: 0 for i in range(10, MAX_FLIPS + 1)}
outcomes = product([True, False], repeat=MAX_FLIPS)

def worker(outcome):
	current_money = START_MONEY
	for i, was_successful in enumerate(outcome, start=1):
		if was_successful:
			current_money += BET_MONEY
		else:
			current_money -= BET_MONEY
			if current_money < BET_MONEY:
				results[i] += 1
				break

if __name__ == "__main__":
	with Pool(2) as p:
		p.map(worker, outcomes)
	
	total_outcomes = 2 ** MAX_FLIPS
	percentages = {i: count / total_outcomes for i, count in results.items()}
