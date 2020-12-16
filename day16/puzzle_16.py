
from collections import defaultdict
PUZZLE_DAY = '16'

def is_between(num, pair):
	return num >= pair[0] and num <= pair[1]


def invalids(pairs, ticket):
	valids = []
	invalids = []
	for num in ticket:
		found = False
		for pair in pairs:
			if is_between(num, pair):
				found = True
				break
		if not found:
			invalids.append(num)
	return invalids


def main(input_mode, test_mode = False):
	input_file = f'puzzle_{PUZZLE_DAY}_input.txt'

	with open(input_file) as fp:
		lines = fp.readlines()

	master_rules = defaultdict(list)
	pairs = []
	i = 0
	for line in lines:
		if line == '\n':
			break
		field, rules = line.split(':')
		rules = rules.strip()
		rules = rules.split(' ')
		for rule in rules:
			if rule != 'or':
				minimum, maximum = rule.split('-')
				pairs.append((int(minimum), int(maximum)))
				master_rules[field].append((int(minimum), int(maximum)))
		i += 1

	pairs.sort()
	my_tickets = [int(i) for i in lines[i+2].split(',')]
	# print(pairs)



	nearby_tickets = []
	for line in lines[i+5:]:
		ticket_nums = [int(i) for i in line.split(',')]
		nearby_tickets.append(ticket_nums)

	# print(dict(master_rules))
	# print(my_tickets)
	# print(nearby_tickets[-1])

	valid_tickets = []
	for ticket in nearby_tickets:
		invalid_nums = invalids(pairs, ticket)
		if len(invalid_nums) == 0:
			valid_tickets.append(ticket)

	cantbe = [set([]) for i in range(0, 20)]
	for ticket in valid_tickets:
		for index, number in enumerate(ticket):
			for field, pairs in master_rules.items():
				matching = False
				for pair in pairs:
					if is_between(number, pair):
						matching = True
				if not matching:
					cantbe[index].add(field)

	total_set = set(master_rules.keys())
	possible_fields = []
	for i  in cantbe:
		fields = total_set - i
		possible_fields.append(fields)
	
	for fields in possible_fields:
		f = list(fields).sort()
		# print(fields)
	# too high 2437546
	fields = [
	'train',
	'arrival platform',
	'duration',
	'route',
	'arrival location',
	'departure station',
	'class',
	'price',
	'departure location',
	'row',
	'departure date',
	'zone',
	'arrival station',
	'departure platform',
	'seat',
	'type',
	'departure track',
	'arrival track',
	'departure time',
	'wagon']
	print(my_tickets)
	departures = []
	for i, field in enumerate(fields):
		if field.startswith('departure'):
			departures.append(my_tickets[i])
	print(departures)
	mult = 1
	for i in departures:
		mult *= i

	print('Multiple', mult)



if __name__ == '__main__':
	input_mode = 'standard'
	test_mode = True
	main(input_mode, test_mode)
