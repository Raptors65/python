# Imports
# Numpy is used to vectorize everything to make everything more Pythonic.
import numpy as np

# Conversion Dictionaries
# This converts a numerical value to a text move.
number_to_move = {0: "rock", 1: "paper", 2: "scissors"}
# This converts a text move to a numerical value.
move_to_number = {"rock": 0, "paper": 1, "scissors": 2}
# This converts a numerical move into the numerical move that beats it.
beats = {0: 1, 1: 2, 2: 0}

# Constants/Settings
# This is how many moves back are considered when calculating the next move.
MOVE_DEPTH = 4
# This is the multiplier used when adjusting the weights in the neural network.
ALPHA = 2

# Mathematical Functions
# sigmoid(x) is used to convert the outputs from each neuron layer into a value between 0 and 1.
# It converts any value into a decimal between 0 and 1.
def sigmoid(x):
	"""Applies sigmoid to an array."""
	
	# Returning sigmoided array.
	return 1 / (1 + np.exp(-x))

# sigmoid_output_derivative(x) is used to calculate the "sureness" (i.e. distance from 0.5) of a neuron layer.
# It takes a value between 0 and 1 and returns higher values for inputs closer to 0.5.
def sigmoid_output_derivative(x):
	"""Gets the derivative of a sigmoid output."""
	
	# Returning the derivative.
	return x * (1 - x)

# Base Classes
# The NeuronLayer class defines a layer of neurons that is initialized with random weights and can use those weights to generate an output from an array of values between 0 and 1.
class NeuronLayer:
	"""Defines a layer of neurons."""
	
	def __init__(self, number_of_neurons, number_of_inputs):
		"""Making a layer of neurons with the specified number of inputs."""
		
		# Generating random weights between -1 and 1.
		self.weights = 2 * np.random.random((number_of_neurons, number_of_inputs)) - 1
	
	def think(self, inputs):
		"""Passes inputs through the layer."""
		
		# Returning the product of the weights and inputs passed through sigmoid.
		return sigmoid(np.dot(self.weights, inputs))

# The NeuralNetwork class defines an ordered group of NeuronLayers. It can take an array of values between 0 and 1 and pass the input through each layer, returning an array of the output of each layer. It can also correct the weights in each layer when given the "correct answer" (i.e. the ideal output).
class NeuralNetwork:
	"""Defines an ordered group of neuron layers."""
	
	def __init__(self, layers):
		"""Makes a neural network with the specified layers."""
		
		# Storing the layers.
		self.layers = layers
	
	def think(self, inputs):
		"""Passes inputs through the network."""
		
		# List to store the outputs.
		outputs = []
		# Looping through the layers.
		for layer in self.layers:
			# Passing the inputs through the layer.
			inputs = layer.think(inputs)
			# Storing the output.
			outputs.append(inputs)
		# Returning the outputs.
		return outputs
	
	def adjust(self, inputs, outputs, correct_output):
		"""Adjusts the weights."""
		
		# Getting the error of the last layer.
		error = correct_output - outputs[-1]
		# Multiplying by the sigmoid derivative to get the sureness of the network.
		delta = error * sigmoid_output_derivative(outputs[-1])
		# Multiplying the error by the activations to get how much it affected the final output.
		adjustment = np.array([[x * y for y in outputs[-2]] for x in delta])
		# Applying the adjustment.
		self.layers[-1].weights += ALPHA * adjustment
		
		# Looping through the middle layers.
		for layer in reversed(range(1, len(self.layers) - 1)):
			# Getting the error.
			error = np.dot(self.layers[layer + 1].weights.T, delta)
			# Multiplying by the sureness.
			delta = error * sigmoid_output_derivative(outputs[layer])
			# Multiplying by the activations.
			adjustment = np.array([[x * y for y in outputs[layer - 1]] for x in delta])
			# Applying the adjustment.
			self.layers[layer].weights += ALPHA * adjustment
		
		# Getting the error of the first layer.
		error = np.dot(self.layers[1].weights.T, delta)
		# Multiplying by the sureness.
		delta = error * sigmoid_output_derivative(outputs[0])
		# Multiplying by the activations.
		adjustment = np.array([[x * y for y in inputs] for x in delta])
		# Applying the adjustment.
		self.layers[0].weights += ALPHA * adjustment

# Other Classes
# The RPSbot class defines an RPS bot based on a NeuralNetwork. It has a customizable move history depth and stores the last few moves by the opponent and itself. It contains two methods: play_as_player and play_as_bot. play_as_player makes the bot play as if it's playing against someone directly while play_as_bot makes the bot simply suggest moves to the user.
class RPSbot(NeuralNetwork):
	"""Defines a rock-paper-scissors bot based on a neural network."""
	
	def __init__(self, layers, move_depth):
		"""Makes a RPS bot based on a neural network."""
		
		# Calling the NeuralNetwork initialization.
		super().__init__(layers)
		# Storing the move depth.
		self.move_depth = move_depth
		# Making a list to store the opponent's move history.
		self.move_history = [0] * (move_depth * 6)
	
	def get_move_input(self, prompt):
		"""Retrieves a move from the user with the specified prompt."""
		
		# An input loop to ensure valid input.
		while True:
			# Asking the user for a move with the specified prompt.
			move_input = input(prompt)
			# Checking if it's a valid move.
			if move_input in move_to_number:
				# Converting the move to a number.
				numeric_move = move_to_number[move_input]
				# Returning the numeric move.
				return numeric_move
			else:
				# Informing the user that their input wasn't valid.
				print("That's not a valid move!")
	
	def play_as_player(self):
		"""Plays RPS as a player (i.e. doesn't first reveal move)."""
		
		# Game loop
		while True:
			# Choosing a move by passing the move history through the bot.
			outputs = self.think(self.move_history)
			self_move = list(outputs[-1]).index(max(outputs[-1]))
			
			# Getting the user's move.
			user_move = self.get_move_input("Choose rock, paper, or scissors: ")
			
			# Telling the user what the computer played.
			print(f"I played {number_to_move[self_move]}.")
			
			# Checking who won.
			if beats[user_move] == self_move:
				print("I win!")
			elif beats[self_move] == user_move:
				print("You win.")
			else:
				print("Tie!")
			# Adding a line break for readability.
			print()
			
			# Making the ideal output.
			perfect_output = [0] * 3
			perfect_output[beats[user_move]] = 1
			# Correcting the weights.
			self.adjust(self.move_history, outputs, perfect_output)
			
			# Creating the addition to add to the move history.
			history_addition = [0] * 6
			history_addition[self_move] = 1
			history_addition[user_move + 3] = 1
			# Updating the move history by shifting the existing values and adding the addition.
			self.move_history[:-6] = self.move_history[6:]
			self.move_history[-6:] = history_addition
	
	def play_as_bot(self):
		"""Plays RPS as a bot (i.e. suggests moves)."""
		
		# Game loop
		while True:
			# Choosing a move by passing the move history through the bot.
			outputs = self.think(self.move_history)
			self_move = list(outputs[-1]).index(max(outputs[-1]))
			
			# Telling the user what the computer thinks they should play.
			print(f"Play {number_to_move[self_move]}. I'm {round(max(outputs[-1]) / sum(outputs[-1]) * 100, 2)}% confident.")
			
			# Getting the opponent's move.
			opponent_move = self.get_move_input("What did your opponent play: ")
			
			# Checking who won.
			if beats[opponent_move] == self_move:
				print("You won!")
			elif beats[self_move] == opponent_move:
				print("They won.")
			else:
				print("Tie!")
			# Adding a line break for readability.
			print()
			
			# Making the ideal output.
			perfect_output = [0] * 3
			perfect_output[beats[opponent_move]] = 1
			# Correcting the weights.
			self.adjust(self.move_history, outputs, perfect_output)
			
			# Creating the addition to add to the move history.
			history_addition = [0] * 6
			history_addition[self_move] = 1
			history_addition[opponent_move + 3] = 1
			# Updating the move history by shifting the existing values and adding the addition.
			self.move_history[:-6] = self.move_history[6:]
			self.move_history[-6:] = history_addition

# Main	
if __name__ == "__main__":
	# Setting the random seed (for testing purposes).
	np.random.seed(1)
	
	# Creating layer 1 with 10 neurons.
	layer1 = NeuronLayer(10, MOVE_DEPTH * 6)
	# Creating layer 2 with 3 neurons and 10 inputs.
	layer2 = NeuronLayer(3, 10)
	
	# Creating the RPS bot.
	rps_bot = RPSbot([layer1, layer2], MOVE_DEPTH)
	
	# Starting the RPS game.
	rps_bot.play_as_player()
