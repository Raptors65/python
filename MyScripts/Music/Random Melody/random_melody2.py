# CHANGELOG:
#     - Individual interval probabilities
#     - More comments

import random
import sound
import time

# Basic Settings
LENGTH = 64
TIMES = [0.5, 1]
INTERVALS = {1: 1/6, 2: 5/18, 3: 5/18, 4: 5/18}
TEMPO = 180
INTERVAL_PROB = 0.8

# Making sure the probabilities add up to one
assert sum(INTERVALS.values()) == 1

# Playable Notes
NOTES = ["piano:C3", "piano:D3", "piano:E3", "piano:F3", "piano:G3", "piano:A3", "piano:B3"]


# Helper Function
def weighted_choice(options, weights):
	return random.choices(list(options), list(weights))[0]

# Looping while song isn't finished
sum = 0
while sum < LENGTH:
	# Play note
	note = random.randint(0, len(NOTES) - 1)
	sound.play_effect(NOTES[note])
	
	# 50% of the time play other note with random interval
	random_decimal = random.random()
	if random_decimal <= INTERVAL_PROB:
		interval = weighted_choice(INTERVALS.keys(), INTERVALS.values())
		if note <= ((len(NOTES) - 1) - interval):
			sound.play_effect(NOTES[note + interval])
		else:
			sound.play_effect(NOTES[(note + interval) % len(NOTES)][:-1] + "4")
	
	# Random length/number of beats
	beats = random.choice(TIMES)
	length = beats / (TEMPO / 60)
	time.sleep(length)
	
	# Store current beats
	sum += beats
