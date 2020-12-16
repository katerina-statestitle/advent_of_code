
from collections import defaultdict
PUZZLE_DAY = '15'


class Game():
	def __init__(self, starting_input):
		self.test_input = starting_input
		self.last_spoken = None
		self.turn = 0
		self.times_spoken = defaultdict(list)

	def play(self, rounds):
		for x in range(0, rounds):
			self.make_turn()
		return self.last_spoken

	def make_turn(self):
		self.turn += 1
		if self.last_spoken is None or self.turn <= len(self.test_input):
			value = self.test_input[self.turn -1]
			self.speak(value)
		else:
			if self.last_spoken in self.times_spoken:
				when_spoken = self.times_spoken[self.last_spoken]
				num_times_spoken = len(when_spoken)
				if num_times_spoken == 1:
					value = 0
				elif num_times_spoken >= 2:
					value = when_spoken[-1] - when_spoken[-2]
			else:
				value = 0
			self.speak(value)



	def speak(self, value):
		# print(f"Turn: {self.turn}, {value}")
		self.last_spoken = value
		self.times_spoken[value].append(self.turn)


def main(input_mode, test_mode = False):
	test_input = [0, 3, 6]
	g = Game(test_input)
	last_spoken = g.play(10)
	print(f"Test1: {last_spoken == 0}")
	assert last_spoken == 0

	rounds = 2020
	test_input = [1,3,2]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test2: {last_spoken == 1}")
	assert last_spoken == 1

	test_input = [2, 1, 3]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test3: {last_spoken == 10}")
	assert last_spoken == 10

	test_input = [1, 2, 3]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test4: {last_spoken == 27}")
	assert last_spoken == 27

	test_input = [2,3,1]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test5: {last_spoken == 78}")
	assert last_spoken == 78

	test_input = [3,2,1]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test6: {last_spoken == 438}")
	assert last_spoken == 438

	test_input = [3,1,2]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test7: {last_spoken == 1836}")
	assert last_spoken == 1836

	rounds = 30000000
	test_input = [0,3,6]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test8: {last_spoken == 175594}")
	assert last_spoken == 175594

	test_input = [1,3,2]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test9: {last_spoken == 2578}")
	assert last_spoken == 2578

	test_input = [2, 1, 3]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test10: {last_spoken == 3544142}")
	assert last_spoken == 3544142

	test_input = [1, 2, 3]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test11: {last_spoken == 261214}")
	assert last_spoken == 261214

	test_input = [2,3,1]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test12: {last_spoken == 6895259}")
	assert last_spoken == 6895259

	test_input = [3,2,1]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test13: {last_spoken == 18}")
	assert last_spoken == 18

	test_input = [3,1,2]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print(f"Test14: {last_spoken == 362}")
	assert last_spoken == 362

	test_input = [0,1,5,10,3,12,19]
	g = Game(test_input)
	last_spoken = g.play(rounds)
	print("Final answer", last_spoken)


if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = True
	main(input_mode, test_mode)
