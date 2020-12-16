
PUZZLE_DAY = '7'


def main(input_mode, test_mode = False):
	if test_mode:
		input_file = f'puzzle_{PUZZLE_DAY}_test.txt'
	else:
		input_file = f'puzzle_{PUZZLE_DAY}_input.txt'
	with open(input_file) as fp:
				lines = fp.readlines()

	if input_mode == 'standard':
		lines = [l.strip().split(' ') for l in lines]
	
	ended_naturally, noop_jmp_indexes = round_2(lines)
	noop_jmp_indexes.reverse()
	for tup in noop_jmp_indexes:
		with open(input_file) as fp:
			lines = fp.readlines()

		if input_mode == 'standard':
			lines = [l.strip().split(' ') for l in lines]
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

		ended_naturally, _ = round_2(lines, tup[0])
		if ended_naturally:
			print("Found")
			break


def round_1(lines):
	acc = 0
	i = 1
	check = True
	next_i = 0
	
	while check:
		this_i = next_i
		command = lines[next_i][0]
		integer = int(lines[next_i][1])
		if command == 'nop':
			next_i += 1
		elif command == 'acc':
			next_i += 1
			acc += integer
		elif command == 'jmp':
			next_i += integer
		else:
			raise Exception("Invalid command", command)
		lines[this_i].append(i)
		i += 1
		if len(lines[this_i]) > 3:
			check = False
			if command == "acc":
				acc -= integer

	print("Last acc value:", acc)


def round_2(lines, check_index = None):
	print("Checking index", check_index)
	ended_naturally = False
	acc = 0
	i = 1
	check = True
	next_i = 0
	commands_length = len(lines)
	last_10_indexes = []
	while check:
		this_i = next_i
		command = lines[next_i][0]
		integer = int(lines[next_i][1])
		if check_index and next_i == check_index:
			if command == 'jmp':
				command = 'nop'
			elif command == 'nop':
				command = 'jmp'
		if command == 'nop':
			next_i += 1
		elif command == 'acc':
			next_i += 1
			acc += integer
		elif command == 'jmp':
			next_i += integer
		else:
			raise Exception("Invalid command", command)
		lines[this_i].append(i)
		if command in ('nop', 'jmp'):
			last_10_indexes.append((this_i, command, i))
		i += 1
		if len(lines[this_i]) > 3:
			check = False
			if command == "acc":
				acc -= integer
		if next_i >= commands_length:
			check = False
			ended_naturally = True

	print("Last acc value:", acc)
	return ended_naturally, last_10_indexes





if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = False
	main(input_mode, test_mode)
