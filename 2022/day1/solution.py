
with open("input.txt") as file:
	lines = file.read()
	lines = lines.split('\n')
	lines.append('')
	sums = []
	sum = 0
	for i in range(len(lines)):
		if lines[i].isnumeric():
			sum += int(lines[i])
		else:
			sums.append(sum)
			sum = 0
	sums = sorted(sums, reverse=True)
	print(sums)
	print(sums[0] + sums[1] + sums[2])