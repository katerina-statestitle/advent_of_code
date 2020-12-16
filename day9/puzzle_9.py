
PUZZLE_DAY = '9'

def is_sum_of_two_previous(preamble, target):
	preamble_length = len(preamble)
	for x in preamble[:]:
		for y in preamble[1:]:
			if x + y == target:
				return True
	return False


def main(input_mode, test_mode = False):
	if test_mode:
		input_file = f'puzzle_{PUZZLE_DAY}_test.txt'
	else:
		input_file = f'puzzle_{PUZZLE_DAY}_input.txt'

	with open(input_file) as fp:
		lines = fp.readlines()

	if input_mode == 'standard':
		lines = [l.strip() for l in lines]
		lines = [int(l) for l in lines]
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

	# # round1
	# preamble_length = 5 if test_mode else 25


	# for i in range(preamble_length, len(lines)):
	# 	preamble = lines[(i-preamble_length):i]
	# 	num = lines[i]
	# 	if is_sum_of_two_previous(preamble, num):
	# 		continue
	# 	else:
	# 		print("First not sum", num)
	# 		break

	def test_contiguous(i):
		found = False
		test_ints = []
		j = i
		while not found:
			test_ints.append(lines[j])
			mysum = sum(test_ints)
			if mysum < target_number:
				j += 1
			elif mysum == target_number:
				print("Found", test_ints)
				return test_ints
			else:
				return False


	target_number = 393911906
	for i in range(0, len(lines)):
		test_ints = test_contiguous(i)
		if test_ints:
			print("Sum min and max", sum([min(test_ints), max(test_ints)]))
		





if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = False
	main(input_mode, test_mode)
