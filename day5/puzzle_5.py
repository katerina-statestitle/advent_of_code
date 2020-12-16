
def main():
	with open('puzzle_5_input.txt') as fp:
		lines = fp.readlines()
		lines = [l.strip() for l in lines]



	seat_ids = []
	for boarding_pass in lines:
		row = get_row(boarding_pass[:7])
		column = get_column(boarding_pass[7:])
		seat_id = get_seat_id(row, column)
		seat_ids.append(seat_id)

	seat_ids.sort()
	missing_ids = []
	for i in range(0, len(seat_ids) - 1):
		if seat_ids[i] + 1 == seat_ids[i + 1]:
			continue
		else:
			missing_ids.append(seat_ids[i] + 1)

	print(seat_ids)
	print(missing_ids)


def get_seat_id(row, column):
	return row * 8 + column


def get_row(chars):
	rows = [x for x in range(0, 128)]
	for char in chars:
		half = int(len(rows) / 2)
		if char == "B":
			rows = rows[half:]
		elif char == "F":
			rows = rows[:half]
		else:
			raise Exception("Not F or B")
	if len(rows) == 1:
		return rows[0]
	else:
		print(rows, chars)
		raise Exception("Too many rows")


def get_column(chars):
	cols = [x for x in range(0, 8)]
	for char in chars:
		half = int(len(cols) / 2)
		if char == 'L':
			cols = cols[:half]
		elif char == 'R':
			cols = cols[half:]
		else:
			raise Exception("Not R or L")
	if len(cols) == 1:
		return cols[0]
	else:
		print(cols, chars)
		raise Exception("Too many cols")


if __name__ == '__main__':
	boarding_pass = 'FBFBBFFRLR'
	row = get_row(boarding_pass[:7])
	column = get_column(boarding_pass[7:])
	seat_id = get_seat_id(row, column)
	print(row, column, seat_id)
	assert seat_id == 357

	boarding_pass = 'BFFFBBFRRR'
	row = get_row(boarding_pass[:7])
	column = get_column(boarding_pass[7:])
	seat_id = get_seat_id(row, column)
	print(row, column, seat_id)
	assert seat_id == 567

	boarding_pass = 'FFFBBBFRRR'
	row = get_row(boarding_pass[:7])
	column = get_column(boarding_pass[7:])
	seat_id = get_seat_id(row, column)
	print(row, column, seat_id)
	assert seat_id == 119

	boarding_pass = 'BBFFBBFRLL'
	row = get_row(boarding_pass[:7])
	column = get_column(boarding_pass[7:])
	seat_id = get_seat_id(row, column)
	print(row, column, seat_id)
	assert seat_id == 820

	main()

