import decimal
import itertools
import math

# Settings
SCORING_NUM_PERCENT = 0.8
SCORING_PERCENTAGE = decimal.Decimal(str(SCORING_NUM_PERCENT))
MISSING_PERCENTAGE = 1 - SCORING_PERCENTAGE
SHOTS = 10
DECIMAL_PRECISION = 100

# Setting the precision.
decimal.getcontext().prec = DECIMAL_PRECISION

# Calculating the number of permutations of ways to get each score.
total_permutations = math.factorial(SHOTS)

# Looping through possible scores.
for score in range(SHOTS + 1):
	# Calculating the number of ways to get to this score (it does this by calculating the number of total permutations, then dividing by number of permutations for the identical elements).
	number_of_ways = total_permutations // (math.factorial(score) * math.factorial(SHOTS - score))
	# Calculating the probability.
	probability = number_of_ways * (SCORING_PERCENTAGE ** score) * (MISSING_PERCENTAGE ** (SHOTS - score))
	# Printing the probability.
	print("{}: {}%".format(score, (probability * 100).normalize()))
