import pdb
PUZZLE_DAY = '14'


def masked_value(value, mask):
	bin_val = '{0:36b}'.format(int(value)).replace(' ', '0')
	val_list = list(bin_val)
	val_list = [int(x) for x in val_list]
	val_list.reverse()
	for i, val in enumerate(val_list):
		if i in mask:
			val_list[i] = mask[i]

	val_list.reverse()
	num = ''.join([str(x) for x in val_list])
	return int(num, 2)


def float_address(val):
	if 'X' in val:
		index_X = val.index('X')
		prefix = val[:index_X]
		postfix = val[index_X+1:]
		for i in ('0', '1'):
			if 'X' in postfix:
				js = [j for j in float_address(postfix)]
				for j in js:
					yield prefix + i + j
			else:
				yield prefix + i + postfix
	else:
		yield val

def float_addresses(val):
	addresses = []
	for address in float_address(val):
		addresses.append(address.strip())
	return addresses

def masked_addresses(address, mask):
	bin_address = '{0:36b}'.format(int(address)).replace(' ', '0')
	val_list = list(bin_address)
	val_list.reverse()
	for i, char in enumerate(val_list):
		if i in mask:
			val_list[i] = mask[i]
	val_list.reverse()
	addresses = float_addresses(''.join(val_list))
	return addresses


def main(input_mode, test_mode = False):
	if test_mode:
		input_file = f'puzzle_{PUZZLE_DAY}_test.txt'
	else:
		input_file = f'puzzle_{PUZZLE_DAY}_input.txt'

	with open(input_file) as fp:
		lines = fp.readlines()
		lines = [l.strip() for l in lines]


	steps = []
	for line in lines:
		instructions, value = line.split('=')
		value = value.strip()
		instructions = instructions.strip()
		if instructions == 'mask':
			steps.append(('mask', value))
		else:
			instructions = instructions[4:-1]
			mem = int(instructions)
			steps.append(('mem', mem, value))

	memory = {}
	print("steps", steps)

	for step in steps:
		if step[0] == 'mask':
			mask = {}
			reverse_bitmap = list(step[1])
			reverse_bitmap.reverse()
			for i, char in enumerate(reverse_bitmap):
				if char != '0':
					mask[i] = char
		elif step[0] == 'mem':
			mem_addresses = masked_addresses(step[1], mask)
			new_val = step[2]
			for address in mem_addresses:
				dec_address = int(address, 2)
				memory[dec_address] = new_val

	print(memory)
	# 660855262312 too low
	s = 0
	for k, v in memory.items():
		s += int(v)

	print(s)
	# 100 in 26, 27. 58, 59

	# 1 in 16, 17, 18, 19, 24, 25, 26, 27






if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = False
	main(input_mode, test_mode)
