

def main():
	with open('puzzle_7_input.txt') as fp:
		lines = fp.readlines()

	rules = {}
	for line in lines:
		top_bag, sub_bags = line.split('contain')
		top_bag = top_bag.replace(' bags ', '')
		sub_bags = [x.replace(' bags', '').replace('.', '').strip() for x in sub_bags.split(',')]
		sub_bags = [(x[0], x[2:].replace("bag", "").strip()) for x in sub_bags]
		colors = [x[1] for x in sub_bags]
		rules[top_bag] = {"colors": colors, "sub_bags": sub_bags}

	containers = find_recursively(rules, "shiny gold")
	print("Final Containers", len(set(containers)))

def find_recursively(rules, color):
	containers = []
	for rule in rules.keys():
		if color in rules[rule]["colors"]: 
			if rule not in containers:
				containers.append(rule)
				additional = find_recursively(rules, rule)
				containers += additional
	return containers


def main2():
	with open('puzzle_7_input.txt') as fp:
		lines = fp.readlines()

	rules = {}
	for line in lines:
		top_bag, sub_bags = line.split('contain')
		top_bag = top_bag.replace(' bags ', '')
		sub_bags = [x.replace(' bags', '').replace('.', '').strip() for x in sub_bags.split(',')]
		sub_bags = [(x[0], x[2:].replace("bag", "").strip()) for x in sub_bags]
		bags_count = {}
		for pair in sub_bags:
			if pair[0] != 'n':
				bags_count[pair[1]] = int(pair[0])
			else:
				bags_count[pair[1]] = 0

		rules[top_bag] = bags_count

	total = get_bags_in_bag(rules, "shiny gold")

	print("total containers", total - 1)


def get_bags_in_bag(rules, color):
	total = 1
	for bag in rules[color].keys():
		bag_count = rules[color][bag]
		if bag_count > 0:
			sub_count = get_bags_in_bag(rules, bag)
			total += sub_count * bag_count
	return total


if __name__ == '__main__':
	# main()
	main2()
