
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
				if char != 'X':
					mask[i] = int(char)
		elif step[0] == 'mem':
			mem_address = step[1]
			new_val = masked_value(step[2], mask)
			if mem_address in memory:
				print('Overwriting', mem_address)
			memory[mem_address] = new_val

	print(sum(memory.values()))

	print(memory)
	# 660855262312 too low
	s = 0
	for k, v in memory.items():
		s += v

	print(s)






if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = False
	main(input_mode, test_mode)
