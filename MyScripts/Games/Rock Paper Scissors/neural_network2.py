# NOTE: doesn't work

import numpy as np

number_to_move = {0: "rock", 1: "paper", 2: "scissors"}
move_to_number = {"rock": 0, "paper": 1, "scissors": 2}
beats = {0: 1, 1: 2, 2: 0}

MOVE_DEPTH = 4
ALPHA = 1
ITERATIONS = 100

def sigmoid(x):
	"""Applies sigmoid to an array."""
	
	# Returning sigmoided array.
	return 1 / (1 + np.exp(-x))

def sigmoid_output_derivative(x):
	"""Gets the derivative of a sigmoid output."""
	
	# Returning the derivative.
	return x * (1 - x)

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

class RPSbot(NeuralNetwork):
	def __init__(self, layers, move_depth):
		"""Makes a RPS bot based on a neural network."""
		
		# Calling the NeuralNetwork initialization.
		super().__init__(layers)
		# Storing the move depth.
		self.move_depth = move_depth
		# Making a list to store the opponent's move history.
		self.move_history = [0] * (move_depth * 6)
		# Creating a list to store the history of move histories.
		self.move_histories = []
		# Creating a list to store the outputs generated by the neural network.
		self.outputs = []
		# Creating a list to store the correct results.
		self.correct_outputs = []
		# Storing the initial weights.
		self.initial_weights = [layer.weights for layer in self.layers]
	
	def play_as_player(self):
		"""Plays RPS as a player (i.e. doesn't first reveal move)."""
		
		# Game loop
		while True:
			# Choosing a move.
			outputs = self.think(self.move_history)
			self_move = list(outputs[-1]).index(max(outputs[-1]))
			# Storing the move.
			self.outputs.append(outputs)
			
			# Input loop
			while True:
				# Asking for input.
				user_input = input("Choose rock, paper, or scissors: ")
				# Checking if it's a valid move.
				if user_input in move_to_number:
					# Converting the move to a number.
					user_move = move_to_number[user_input]
					# Breaking out of the input loop.
					break
				else:
					# Informing the user that their move wasn't valid.
					print("That's not a valid move!")
			
			# Telling the user what the computer played.
			print("I played %s." % number_to_move[self_move])
			
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
			# Storing the ideal output.
			self.correct_outputs.append(perfect_output)
			
			# Creating the addition to add to the move history.
			history_addition = [0] * 6
			history_addition[self_move] = 1
			history_addition[user_move + 3] = 1
			# Updating the move history.
			self.move_history[:-6] = self.move_history[6:]
			self.move_history[-6:] = history_addition
			# Storing the move history.
			self.move_histories.append(self.move_history)
			
			# Updating the weights.
			self.train()
	
	def train(self):
		"""Trains the neural network based on previous moves."""
		
		# Looping through layers.
		for layer in range(len(self.layers)):
			# Resetting the weights.
			self.layers[layer].weights = self.initial_weights[layer]
		# Looping a certain amount of times.
		for iteration in range(ITERATIONS):
			# Looping through the move histories and the correct outputs.
			for move_history, output, correct_output in zip(self.move_histories, self.outputs, self.correct_outputs):
				# Adjusting weights.
				self.adjust(np.array(move_history), np.array(output), np.array(correct_output))

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
