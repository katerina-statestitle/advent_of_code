


with open('puzzle_1_input.csv') as fp:
	integers = fp.readlines()

integers = [int(i.strip()) for i in integers]

print(integers[0:10])

l = len(integers)

multiple = 0
for i in range(0, l-2):
	for j in range(i+1, l-1):
		for k in range(j+1, l):
			a = integers[i]
			b = integers[j]
			c = integers[k]
			if a + b + c == 2020:
				multiple = a * b * c
				print(f"{a} * {b} * {c} = {multiple}")

