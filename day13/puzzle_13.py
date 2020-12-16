
PUZZLE_DAY = '13'


def y(bus_set):
	return bus_set[0] * bus_set[2] - bus_set[1]

def ys_equal(bus_sets):
	return len(set([y(a) for a in bus_sets])) == 1

def calculate(bus_set, target_y):
	multiplier = (target_y + bus_set[1]) // bus_set[0]
	return multiplier

def ys_list(bus_sets):
	return [y(a) for a in bus_sets]

def main(input_mode, test_mode = False):
	if test_mode:
		input_file = f'puzzle_{PUZZLE_DAY}_test.txt'
	else:
		input_file = f'puzzle_{PUZZLE_DAY}_input.txt'

	with open(input_file) as fp:
		lines = fp.readlines()

	# # Part 1
	# earliest_time = int(lines[0])
	# buses = [int(x) for x in lines[1].split(',') if x != 'x']

	# print(buses)


	# time_to_bus = {}
	# for bus in buses:
	# 	near_time = (earliest_time // bus) * bus

	# 	if near_time <= earliest_time:
	# 		next_time = near_time + bus
	# 		time_to_bus[bus] = next_time
	# 	else:
	# 		next_time = near_time
	# 	print(bus, near_time, next_time)

	# min_time, min_bus = 0, 0
	# for bus, time in time_to_bus.items():
	# 	if time < min_time or min_time == 0:
	# 		min_time = time
	# 		min_bus = bus

	# print(f'min_time {min_time}, bus {bus}')
	# time_to_wait  = min_time - earliest_time
	# print("Multiple: ", time_to_wait * min_bus)


	# Part 2
	buses = lines[1].split(',')
	bus_to_index  = []
	max_bus = 0
	for i, bus in enumerate(buses):
		if bus == 'x':
			pass
		else:
			bus_to_index.append([int(bus), i])
			if int(bus) > max_bus:
				max_bus = int(bus)

	bus_sets = []
	for mylist in bus_to_index:
		mylist.append(1)
		bus_sets.append([int(x) for x in mylist])

	print(bus_sets)
	key_bus = bus_sets[0][0]
	# 1797391531030110 too high
	# 279739153103011 wrong
	# 179739153103011 too low
	# 100030606600000 too low
	target_y = 534035653563209
	for bus_set in bus_sets:
		bus_set[2] = calculate(bus_set, target_y)
	
	i = 0
	while not ys_equal(bus_sets):
		i += 1
		target_y += key_bus
		if i % 100000 == 0:
			print(target_y)
		for bus_set in bus_sets:
			bus_set[2] = calculate(bus_set, target_y)


	print(ys_list(bus_sets))


if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = False
	main(input_mode, test_mode)
