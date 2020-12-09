with open('puzzle_3_input.txt') as fp:
	lines = fp.readlines()
lines = [line.strip() for line in lines]


pairs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

ans = []

for pair in pairs:
	i = 0
	j = 0

	trees = 0
	not_trees = 0
	row_count = len(lines[0]) - 1
	puzzle_length = len(lines)

	for line in range(0, puzzle_length - pair[1]):
		i += pair[0]
		j += pair[1]
		if i > row_count:
			i = (i % row_count) - 1

		try:
			check = lines[j][i]
		except IndexError as e:
			print(j, i)
			continue
		if check == "#":
			trees += 1
		else:
			not_trees += 1

	print(f'Trees: {trees}, not_trees: {not_trees}')
	print(f'Puzzle: {puzzle_length}, hits{trees + not_trees}')
	ans.append(trees)

res = ans[0]
for an in ans[1:]:
	res *= an

print(res)
