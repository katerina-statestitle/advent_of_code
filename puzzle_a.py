
PUZZLE_DAY = 'a'


def main(input_mode, test_mode = False):
	if test_mode:
		input_file = f'puzzle_{PUZZLE_DAY}_test.txt'
	else:
		input_file = f'puzzle_{PUZZLE_DAY}_input.txt'

	with open(input_file) as fp:
		lines = fp.readlines()

	if input_mode == 'standard':
		lines = [l.strip() for l in lines]
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












if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = True
	main(input_mode, test_mode)
