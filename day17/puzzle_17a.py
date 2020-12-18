from collections import defaultdict
import operator


PUZZLE_DAY = '17'

DIRECTIONS = []
for x in (-1, 0, 1):
	for y in (-1, 0, 1):
		for z in (-1, 0, 1):
			for w in (-1, 0, 1):
				if (x, y, z, w) != (0, 0, 0, 0):
					DIRECTIONS.append((x, y, z, w))


def get_cell(x, y, z, w, matrix):
	return matrix[z][y][x][w]

def get_neighbors(x, y, z, w, matrix):
	neighbors = []
	for tup in DIRECTIONS:
		neighbor = matrix.get_cell(x + tup[0], y + tup[1], z + tup[2], w + tup[3])
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
	w = 0
	for y, line in enumerate(lines):
		for x, char in enumerate(list(line)):
			cell_state = 'active' if char == '#' else 'inactive'
			matrix.add_cell(x, y, z, w, cell_state)
	
	print("Starting matrix:")
	matrix.print_matrix()
	for cycle in range(0, 6):
		print(f"Cycle {cycle + 1}: ")
		matrix = matrix.cycle()

	print("Final matrix:")
	matrix.print_matrix()
	print(f"Total active: {matrix.total_actives()}")

class Cell():
	def __init__(self, x, y, z, w, state):
		self.x = x
		self.y = y
		self.z = z
		self.w = w
		self.state = state

	def __eq__(self, cell2):
		return self.x == cell2.x and self.y == cell2.y and self.z == cell2.z and self.w == cell2.w

	def match(self, x, y, z, w):
		return self.x == x and self.y == y and self.z == z and self.w == w
	
	@property
	def active(self):
		return self.state == 'active'

	@property
	def inactive(self):
		return self.state == 'inactive'

	def symbol(self):
		return '#' if self.active else '.'

	def num_active_neighbors(self, cell_matrix):
		neighbors = get_neighbors(self.x, self.y, self.z, self.w, cell_matrix)
		return sum([c.active for c in neighbors])

	def __str__(self):
		return self.symbol()

	def __hash__(self):
		return hash(str(' '.join([str(i) for i in (self.x, self.y, self.z, self.w, self.state)])))

	def __getitem__(self, x):
		n = (self.x, self.y, self.z, self.w)
		return n[x]

class Matrix():
	def __init__(self):
		self.cells = set([])
		self.index = {}
		self.xs = set([])
		self.ys = set([])
		self.zs = set([])
		self.ws = set([])

	def get_cell(self, x, y, z, w):
		c = self.index.get((x, y, z, w))
		if c:
			return c
		return self.add_cell(x, y, z, w, 'inactive')

	def add_cell(self, x, y, z, w, state):
		new_cell = Cell(x, y, z, w, state)
		self.cells.add(new_cell)
		self.index[(x, y, z, w)] = new_cell
		self.xs.add(x)
		self.ys.add(y)
		self.zs.add(z)
		self.ws.add(w)
		return new_cell

	def remove_cell(self, cell):
		self.cells.remove(cell)

	def cells_at_zw(self, z, w):
		zcells = []
		for cell in self.cells:
			if cell.z == z and cell.w == w:
				zcells.append(cell)
		return zcells

	def total_actives(self):
		return sum([c.active for c in self.cells])

	def minz(self, w):
		return min([c.z for c in self.cells if c.w == w])

	def maxz(self, w):
		return max([c.z for c in self.cells if c.w == w])

	def minx(self, y, z, w):
		return min([c.x for c in self.cells if c.w == w and c.z == z and c.y == y])

	def maxx(self, y, z, w):
		return max([c.x for c in self.cells if c.w == w and c.z == z and c.y == y])

	def miny(self, z, w):
		try:
			return min([c.y for c in self.cells if c.w == w and c.z == z])
		except ValueError:
			return None

	def maxy(self, z, w):
		return max([c.y for c in self.cells if c.w == w and c.z == z])

	def minw(self):
		return min([c.w for c in self.cells])

	def maxw(self):
		return max([c.w for c in self.cells])

	def print_matrix(self, printme = True):
		minw, maxw = self.minw(), self.maxw()
		for w in range(minw, maxw + 1):
			minz, maxz = self.minz(w), self.maxz(w)
			for z in range(minz, maxz + 1):
				miny, maxy = self.miny(z, w), self.maxy(z, w)
				if printme: print(f"z = {z} w = {w}")
				for y in range(miny, maxy + 1):
					minx, maxx = self.minx(y, z, w), self.maxx(y, z, w)					
					xs = ''.join([str(self.get_cell(x, y, z, w)) for x in range(minx, maxx + 1)])
					if printme: print(xs)
				if printme: print('\n')

	def remove_layer(self, z, w):
		cells = self.cells_at_zw(z, w)
		for cell in cells:
			self.remove_cell(cell)

	def layer_is_inactive(self, z, w):
		cells = self.cells_at_zw(z, w)
		return all([c.inactive for c in cells])

	def clean_up_inactive_layers(self):
		minw = self.minw()
		maxw = self.maxw()
		for w in range(minw, maxw + 1):
			minz = self.minz(w)
			maxz = self.maxz(w)
			for z in (minz, maxz):
				if self.layer_is_inactive(z, w):
					self.remove_layer(z, w)
				if self.layer_is_inactive(z, w):
					self.remove_layer(z, w)

	def cycle(self):
		new_matrix = Matrix()
		frozen_cells = list(self.cells)
		for cell in frozen_cells:
			active_neighbors = cell.num_active_neighbors(self)

		frozen_cells = list(self.cells)
		for i, cell in enumerate(frozen_cells):
			active_neighbors = cell.num_active_neighbors(self)
			if cell.active:
				if active_neighbors == 2 or active_neighbors == 3:
					new_matrix.add_cell(cell.x, cell.y, cell.z, cell.w, 'active')
				else:
					new_matrix.add_cell(cell.x, cell.y, cell.z, cell.w, 'inactive')
			elif cell.inactive:
				if active_neighbors == 3:
					new_matrix.add_cell(cell.x, cell.y, cell.z, cell.w, 'active')
				else:
					new_matrix.add_cell(cell.x, cell.y, cell.z, cell.w, 'inactive')
		
		new_matrix.print_matrix(printme=False)
		self.clean_up_inactive_layers()
		return new_matrix


if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = False
	main(input_mode, test_mode)
