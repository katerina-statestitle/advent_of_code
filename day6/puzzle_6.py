

def main():
	with open('puzzle_6_input.txt') as fp:
		lines = fp.readlines()

	questionaires = []

	questionaire = ''
	num_people = 0
	for line in lines:
		if line == '\n':
			q = questionaire.strip().replace(' ', '')
			questionaires.append(f'{num_people}{q}')
			questionaire = ''
			num_people = 0
		else:
			num_people += 1
			questionaire += line.strip() + ' '

	sets = [(int(q[0]), q[1:]) for q in questionaires]

	myints = []
	for s in sets:
		myint = 0
		c, quests = s
		myset = set(quests)
		for char in myset:
			if c == quests.count(char):
				myint += 1
		myints.append(myint)

	print(sum(myints))





if __name__ == '__main__':
	main()
