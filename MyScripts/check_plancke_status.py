import requests
import sys

# Constants
PLAYER = "LionRaptor"
GAME_CHECK = "SKYBLOCK"

# Getting the text of the Plancke page.
request = requests.get(f"https://plancke.io/hypixel/player/stats/{PLAYER}")
text = request.text

# Finding the game the player is playing.
index = text.find("GameType:")
# Checking if the player is online.
if index == -1:
	print(f"{PLAYER} is offline.")
	sys.exit(0)
start_index = index + 14
end_index = text.find(" </div>", start_index)
game = text[start_index:end_index]

# Checking if it matches.
if game == GAME_CHECK:
	print(f"{PLAYER} is playing {GAME_CHECK}.")
else:
	print(f"{PLAYER} is not playing {GAME_CHECK}. He ")

# Closing the request.
request.close()
