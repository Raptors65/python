import sound
import time

notes = []
while True:
	note = input("Note: ")
	if note == "exit":
		break
	
	delay = float(input("Delay: "))
	
	notes.append((f"piano:{note}", delay))

for note, delay in notes:
	sound.play_effect(note)
	time.sleep(delay)
