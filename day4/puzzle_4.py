def main():
	with open('puzzle_4_input.txt') as fp:
		lines = fp.readlines()

	passports = []

	passport = ''
	for line in lines:
		if line == '\n':
			passports.append(passport.strip())
			passport = ''
		else:
			passport += line.strip() + ' '

	print(passports[-1])

	required_fields = {'hgt', 'iyr', 'pid', 'ecl', 'hcl', 'byr',  'eyr'}

	valid = 0
	for passport in passports:
		pairs = passport.split(' ')
		keys = {x.split(':')[0] for x in pairs}
		intersection = required_fields.intersection(keys)
		if len(intersection) == 7:
			data = {}
			for x in pairs:
				key, value = x.split(':')
				data[key] = value
			check = data_validate(data)
			if check:
				valid += 1
		else:
			print(intersection)

	print(f'Valids: {valid}')

def data_validate(data):
	birth_year = data['byr']
	if len(birth_year) != 4:
		return False
	birth_year = int(birth_year)
	if birth_year < 1920 or birth_year > 2002:
		return False
	issue_year = data['iyr']
	if len(issue_year) != 4:
		return False
	issue_year = int(issue_year)
	if issue_year < 2010 or issue_year > 2020:
		return False
	expiration_year = data['eyr']
	if len(expiration_year) != 4:
		return False
	expiration_year = int(expiration_year)
	if expiration_year < 2020 or expiration_year > 2030:
		return False
	height_data = data['hgt']
	height_unit = height_data[-2:]
	height = int(height_data[:-2])
	if height_unit == 'cm':
		if height < 150 or height > 193:
			return False
	elif height_unit == 'in':
		if height < 59 or height > 76:
			return False
	else:
		return False

	hair_color = data['hcl']
	if hair_color[0] != '#':
		return False
	if len(hair_color) != 7:
		return False
	for c in hair_color[1:]:
		if c not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'):
			return False
	eye_color = data['ecl']
	if eye_color not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
		return False
	pid = data['pid']
	if len(pid) != 9:
		return False
	for c in pid:
		if c not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
			return False
	return True

if __name__ == '__main__':
	main()
