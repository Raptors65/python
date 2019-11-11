from decimal import Decimal
import math

STEP = 10

def get_candidates():
	x_data = list(range(361))
	y_data = [abs(x - ((12 * x) % 360)) for x in x_data]
	return list(filter(lambda x: y_data[x] < 12, x_data))

def get_times():
	times = set()
	for x in range(0, 360, STEP):
		decimal = (x + ((x - (x * 12 % 360)) / 11)) / 360
		time = f"{math.floor(decimal * 12)}:{round(decimal * 60):02d}"
		times.add(time)
	return times

if __name__ == "__main__":
	print(sorted(get_times()))

