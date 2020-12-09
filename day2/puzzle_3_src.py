with open('puzzle_3_input.txt') as fp:
	lines = fp.readlines()

i = 0
j = 0

trees = 0
length = len(lines[0])

for line in range(0, len(lines) - 1):
	i += 3
	if i > length:
		i = i % length
	j += 1
	check = lines[i][j]
	if check == "#":
		trees += 1

print(trees)