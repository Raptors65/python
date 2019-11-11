from itertools import accumulate, product, takewhile
import time

START_MONEY = 10
BET_MONEY = 1
MAX_FLIPS = 20

results = {i: 0 for i in range(10, MAX_FLIPS + 2)}
outcomes = product([True, False], repeat=MAX_FLIPS)

def bet(current_money, was_successful):
	if was_successful:
		return current_money + BET_MONEY
	else:
		return current_money - BET_MONEY


for outcome in outcomes:
	results[len(list(takewhile(lambda x: x >= BET_MONEY, accumulate((START_MONEY,) + outcome, bet))))] += 1

total_outcomes = 2 ** MAX_FLIPS
percentages = {i: count / total_outcomes for i, count in results.items()}

if __name__ == "__main__":
	for i, percentage in list(percentages.items())[:-1]:
		print(f"{i}: {percentage*100}%")
	print(f"{i + 1}+: {list(percentages.values())[-1] * 100}")
