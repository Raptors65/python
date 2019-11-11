import random
import sound
import time

LENGTH = 32
TIMES = [0.5, 1]
INTERVALS = [2, 3, 4]
TEMPO = 180
INTERVAL_PROB = 0.8

NOTES = ["piano:C3", "piano:D3", "piano:E3", "piano:F3", "piano:G3", "piano:A3", "piano:B3"]


sum = 0
while sum < LENGTH:
	# Play note
	note = random.randint(0, len(NOTES) - 1)
	sound.play_effect(NOTES[note])
	
	# 50% of the time play other note with random interval
	random_decimal = random.random()
	if random_decimal <= INTERVAL_PROB:
		interval = random.choice(INTERVALS)
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
