
PUZZLE_DAY = '10'

def copy_grid(grid):
	return [x for x in grid]


DIRECTIONS = [
	(-1, -1),
	(-1, 0),
	(-1, 1),
	(0, 1),
	(0, -1),
	(1, -1),
	(1, 0),
	(1, 1)
]

def get_adjacent(grid, x, y):
	rows = len(grid)
	cols = len(grid[0])
	seats = []
	for dx, dy in DIRECTIONS:
		x1 = x + dx
		y1 = y - dy
		if x1 >= 0 and y1 >= 0 and x1 < rows and y1 < cols:
			seat = grid[x1][y1]
			seats.append(seat)
		else:
			seats.append(None)
	return seats

def new_adjacent(grid, x, y):
	rows = len(grid)
	cols = len(grid[0])
	seats = []
	for dx, dy in DIRECTIONS:
		at_end = False
		x1 = x
		y1 = y
		while not at_end:
			x1 = x1 + dx
			y1 = y1 - dy
			if x1 >= 0 and y1 >= 0 and x1 < rows and y1 < cols:
				seat = grid[x1][y1]
				seats.append(seat)
				if seat in ('L', '#'):
					at_end = True
			else:
				at_end = True
				seats.append(None)
	return seats


def num_occupied(seats):
	return seats.count('#')


def round(grid):
	rows = len(grid)
	cols = len(grid[0])
	new_grid = [[None] * cols for row in range(rows)]
	changed = False
	for x in range(0, rows):
		for y in range(0, cols):
			current_seat = grid[x][y]
			seats = new_adjacent(grid, x, y)
			occupied_adjacent = num_occupied(seats)
			if current_seat == 'L':
				if occupied_adjacent == 0:
					seat = '#'
					changed = True
				else:
					seat = current_seat
			elif current_seat == '#':
				if occupied_adjacent >= 5:
					seat = 'L'
					changed = True
				else:
					seat = current_seat
			else:
				seat = current_seat
			new_grid[x][y] = seat
	return new_grid, changed

def total_occupied(grid):
	occupied = sum([x.count('#') for x in grid])
	print(f'Occupied {occupied}')

def pretty_print(grid):
	ans = []
	for line in grid:
		ans.append(''.join(line))
	ans = '\n'.join(ans)
	print(ans)

def main(input_mode, test_mode = False):
	if test_mode:
		input_file = f'puzzle_{PUZZLE_DAY}_test.txt'
	else:
		input_file = f'puzzle_{PUZZLE_DAY}_input.txt'

	with open(input_file) as fp:
		lines = fp.readlines()

	lines = [l.strip() for l in lines]
	lines = [[char for char in line] for line in lines]

	num_rounds = 0
	changed = True
	grid = lines
	while changed:
		grid, changed = round(grid)
		num_rounds += 1
		print("num_rounds", num_rounds)
	total_occupied(grid)



if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = False
	main(input_mode, test_mode)
