import math
import numpy as np
from random import randint

class Coins():

	def __init__(self):
		self.index = 0
		self.iter_number = 0

	def counterfeit_coin(self, coins):
		self.iter_number += 1
		if len(coins) == 1:
			return coins[0]

		if len(coins) == 2:
			stack_size = 1
		else:
			stack_size = math.floor(len(coins)/3)

		if sum(coins[:stack_size]) != sum(coins[stack_size:2*stack_size]):
			if sum(coins[:stack_size]) < sum(coins[stack_size:2*stack_size]):
				return self.counterfeit_coin(coins[:stack_size])
			else:
				self.index = self.index + stack_size 
				return self.counterfeit_coin(coins[stack_size:2*stack_size])
		else:
			self.index = self.index + 2 * stack_size 
			return self.counterfeit_coin(coins[2*stack_size:])
	

stack_size = 2000000
std_coin_mass = 10
stack = np.full(stack_size, std_coin_mass)
stack[randint(0,stack_size-1)] = std_coin_mass - 1
print(stack)
mystack = Coins()
mystack.counterfeit_coin(stack)
print(mystack.index, mystack.iter_number)
