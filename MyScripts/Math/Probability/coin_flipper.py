import random

NUMBER_OF_COINS = 2
NUMBER_OF_ITERATIONS = 20

int_to_value = ["heads", "tails"]
results = {}

for i in range(NUMBER_OF_ITERATIONS):
	coins = [int_to_value[random.randint(0, len(int_to_value) - 1)] for i in range(NUMBER_OF_COINS)]
	result = "-".join(coins)
	
	if result not in results:
		results.update({result: 1})
	else:
		results[result] += 1
		
print("Estimated result:", round(NUMBER_OF_ITERATIONS / len(int_to_value)**NUMBER_OF_COINS))
print(results)
