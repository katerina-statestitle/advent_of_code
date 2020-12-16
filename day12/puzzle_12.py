import math

PUZZLE_DAY = '12'


class Boat():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.w_x = 10
		self.w_y = 1
		self.moves = 0

	def move(self, direction, value):
		self.moves += 1
		if direction != 'F':
			print(f'Moving waypoint {direction} by {value}')
			if direction == 'E':
				self.w_x += value
			elif direction == 'N':
				self.w_y += value
			elif direction == 'S':
				self.w_y -= value
			elif direction == 'W':
				self.w_x -= value
			elif direction == 'L':
				self.rotate(direction, value)
			elif direction == 'R':
				self.rotate(direction, value)
		else:
			self.forward(value)

	def rotate(self, direction, value):
		self.print_current_waypoint()
		print('Moving waypoint', direction, value)
		if direction == 'L':
			if value == 90:
				self.w_x, self.w_y = -self.w_y, self.w_x
			elif value == 180:
				self.w_x = -self.w_x
				self.w_y = -self.w_y
			elif value == 270:
				self.w_x, self.w_y = self.w_y, -self.w_x
		if direction == 'R':
			if value == 90:
				self.w_x, self.w_y = self.w_y, -self.w_x
			elif value == 180:
				self.w_x = -self.w_x
				self.w_y = -self.w_y
			elif value == 270:
				self.w_x, self.w_y = -self.w_y, self.w_x
		self.print_current_waypoint()

	def print_current(self):
		print(f'Current Coordinates {self.x} {self.y}')

	def print_current_waypoint(self):
		print(f'Current Waypoint Coordinates {self.w_x} {self.w_y}')

	def turn(self, direction, degrees):
		if direction == 'L':
			self.facing += degrees
		elif direction == 'R':
			self.facing -= degrees
		else:
			print(value)

	def forward(self, value):
		dx, dy = self.waypoint_diff()
		print(f'Moving ship to waypoint x {value} by {dx} {dy}')
		self.x += (dx * value)
		self.y += (dy * value)

	def waypoint_diff(self):
		dx = self.w_x 
		dy = self.w_y
		return dx, dy

	def manhatten_distance(self):
		return abs(self.x) + abs(self.y)


def main(input_mode, test_mode = False):
	if test_mode:
		input_file = f'puzzle_{PUZZLE_DAY}_test.txt'
	else:
		input_file = f'puzzle_{PUZZLE_DAY}_input.txt'

	with open(input_file) as fp:
		lines = fp.readlines()

	print(len(lines))
	if input_mode == 'standard':
		lines = [l.strip() for l in lines]
		directions = [(l[0], int(l[1:])) for l in lines]


	b = Boat()
	for direction, value in directions:
		b.move(direction, value)
	
		# b.print_current_waypoint()
	b.print_current()		
	print('Manhatten Distance: ', b.manhatten_distance())
	print(len(directions))
	print(b.moves)



if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = False
	main(input_mode, test_mode)
