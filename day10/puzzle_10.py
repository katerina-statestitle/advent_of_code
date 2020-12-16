
import math
PUZZLE_DAY = '9'


def main(input_mode, test_mode = False):
	if test_mode:
		input_file = f'puzzle_{PUZZLE_DAY}_test.txt'
	else:
		input_file = f'puzzle_{PUZZLE_DAY}_input.txt'

	with open(input_file) as fp:
		lines = fp.readlines()

	if input_mode == 'standard':
		lines = [int(l.strip()) for l in lines]
	else:
		items = []
		item = ''
		for line in lines:
			if line == '\n':
				item = item.strip().replace(' ', '')
				items.append(item)
				item = ''
			else:
				item += line.strip() + ' '

	lines.append(0)
	lines.sort()
	last = lines[-1]
	lines.append(last + 3)
	print(lines)
	lines_length = len(lines)

	def runs_of_ones(start_index):
		try:
			diff = lines[start_index + 1] - lines[start_index]
		except IndexError:
			return []
		run = []
		while diff == 1:
			run.append(lines[start_index + 1])
			start_index += 1
			try:
				diff = lines[start_index + 1] - lines[start_index]
			except IndexError:
				break
		return run

	runs = []
	extras = set()
	i = 0
	while i < lines_length:
		run = runs_of_ones(i)
		if run:
			i += len(run)
			if len(run) > 1:
				print("run of ones", run)
				runs.append(run[:-1])
		else:
			i += 1

	print(runs)

	mult = 1
	mults = []
	for l in runs:
		if len(l) == 1:
			mult *= 2
			mults.append(2)
		elif len(l) == 2:
			mult *= 4
			mults.append(4)
		elif len(l) == 3:
			mult *= 7
			mults.append(7)

	print(mults)
	print(mult)


if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = False
	main(input_mode, test_mode)
