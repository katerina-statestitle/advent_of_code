


with open('puzzle_2_input.csv') as fp:
	lines = fp.readlines()

pairs = []
for line in lines:
	rule, password = line.split(':')
	pattern, letter = rule.split(' ')
	minimum, maximum = pattern.split('-')
	pairs.append({
		"min": int(minimum),
		"max": int(maximum),
		"letter": letter,
		"password": password.strip()
		}
	)

valid = 0
for pair in pairs:
	password = pair["password"]
	letter = pair["letter"]
	try:
		position1 = password[(pair["min"] - 1)]
		position2 = password[(pair["max"] - 1)]
		
		if position1 == letter and position2 == letter:
			print(position1, position2, letter, "invalid")
		elif position1 == letter or position2 == letter:
			print(position1, position2, letter, "valid")
			valid += 1
		else:
			print(position1, position2, letter, "invalid2")
	except IndexError:
		print(pair)

print(f'Valids: {valid}')
