from collections import defaultdict
import operator


PUZZLE_DAY = '17'

DIRECTIONS = []
for x in (-1, 0, 1):
	for y in (-1, 0, 1):
		for z in (-1, 0, 1):
			if (x, y, z) != (0, 0, 0):
				DIRECTIONS.append((x, y, z))


def get_cell(x, y, z, matrix):
	return matrix[z][y][x]

def get_neighbors(x, y, z, matrix):
	neighbors = []
	for tup in DIRECTIONS:
		neighbor = matrix.get_cell(x + tup[0], y + tup[1], z + tup[2])
		if neighbor:
			neighbors.append(neighbor)
	return neighbors


def main(input_mode, test_mode = False):
	if test_mode:
		input_file = f'puzzle_{PUZZLE_DAY}_test1.txt'
	else:
		input_file = f'puzzle_{PUZZLE_DAY}_input.txt'

	with open(input_file) as fp:
		lines = fp.readlines()
		lines = [l.strip() for l in lines]


	matrix = Matrix()
	z = 0
	for y, line in enumerate(lines):
		for x, char in enumerate(list(line)):
			cell_state = 'active' if char == '#' else 'inactive'
			matrix.add_cell(x, y, z, cell_state)
	
	print("Starting matrix:")
	matrix.print_matrix()
	for cycle in range(0, 6):
		print(f"Cycle {cycle + 1}: ")
		matrix = matrix.cycle()

	print("Final matrix:")
	matrix.print_matrix()
	print(f"Total active: {matrix.total_actives()}")

class Cell():
	def __init__(self, x, y, z, state):
		self.x = x
		self.y = y
		self.z = z
		self.state = state

	def __eq__(self, cell2):
		return self.x == cell2.x and self.y == cell2.y and self.z == cell2.z

	def match(self, x, y, z):
		return self.x == x and self.y == y and self.z == z
	
	@property
	def active(self):
		return self.state == 'active'

	@property
	def inactive(self):
		return self.state == 'inactive'

	def symbol(self):
		return '#' if self.active else '.'

	def num_active_neighbors(self, cell_matrix):
		neighbors = get_neighbors(self.x, self.y, self.z, cell_matrix)
		return sum([c.active for c in neighbors])

	def __str__(self):
		return self.symbol()

	def __hash__(self):
		return hash(str(' '.join([str(i) for i in (self.x, self.y, self.z, self.state)])))

	def __getitem__(self, x):
		n = (self.x, self.y, self.z)
		return n[x]

class Matrix():
	def __init__(self):
		self.cells = set([])

	def get_cell(self, x, y, z):
		for cell in list(self.cells):
			if cell.match(x, y, z):
				return cell
		return self.add_cell(x, y, z, 'inactive')

	def add_cell(self, x, y, z, state):
		new_cell = Cell(x, y, z, state)
		self.cells.add(new_cell)
		return new_cell

	def remove_cell(self, cell):
		self.cells.remove(cell)

	def cells_at_z(self, z):
		zcells = []
		for cell in self.cells:
			if cell.z == z:
				zcells.append(cell)
		return zcells

	def total_actives(self):
		return sum([c.active for c in self.cells])

	def minz(self):
		return min([c.z for c in self.cells])

	def maxz(self):
		return max([c.z for c in self.cells])

	def minx(self):
		return min([c.x for c in self.cells])

	def maxx(self):
		return max([c.x for c in self.cells])

	def miny(self):
		return min([c.y for c in self.cells])

	def maxy(self):
		return max([c.y for c in self.cells])

	def print_matrix(self, printme = True):
		cell_list = list(self.cells)
		cell_list = sorted(cell_list, key = operator.itemgetter(2, 1, 0))
		minx, maxx = self.minx(), self.maxx()
		miny, maxy = self.miny(), self.maxy()
		minz, maxz = self.minz(), self.maxz()
		for z in range(minz, maxz + 1):
			if printme: print(f"z = {z}")
			for y in range(miny, maxy + 1):
				xs = ''.join([str(self.get_cell(x, y, z)) for x in range(minx, maxx + 1)])
				if printme: print(xs)
			if printme: print('\n')

	def remove_layer(self, z):
		cells = self.cells_at_z(z)
		for cell in cells:
			self.remove_cell(cell)

	def layer_is_inactive(self, z):
		cells = self.cells_at_z(z)
		return all([c.inactive for c in cells])

	def clean_up_inactive_layers(self):
		minz = self.minz()
		maxz = self.maxz()
		if self.layer_is_inactive(minz):
			self.remove_layer(minz)
		if self.layer_is_inactive(maxz):
			self.remove_layer(maxz)

	def cycle(self):
		frozen_cells = list(self.cells)
		new_matrix = Matrix()
		frozen_cells = list(self.cells)
		for cell in frozen_cells:
			active_neighbors = cell.num_active_neighbors(self)

		frozen_cells = list(self.cells)
		for cell in frozen_cells:
			active_neighbors = cell.num_active_neighbors(self)
			if cell.active:
				if active_neighbors in (2, 3):
					new_matrix.add_cell(cell.x, cell.y, cell.z, 'active')
				else:
					new_matrix.add_cell(cell.x, cell.y, cell.z, 'inactive')
			if cell.inactive:
				if active_neighbors == 3:
					new_matrix.add_cell(cell.x, cell.y, cell.z, 'active')
				else:
					new_matrix.add_cell(cell.x, cell.y, cell.z, 'inactive')
		new_matrix.print_matrix()
		new_matrix.clean_up_inactive_layers()
		return new_matrix


if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = False
	main(input_mode, test_mode)
