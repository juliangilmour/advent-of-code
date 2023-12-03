def part1():
	sum = 0
	with open("/home/julia/repos/advent-of-code/day4/input.txt") as file:
		lines = file.read()
		lines = lines.split("\n")
		for line in lines:
			pair = line.split(",")
			first, second = pair[0].split("-"), pair[1].split("-")
			if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]): sum += 1; print(pair, 1)
			elif int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]): sum += 1; print(pair, 1)
			elif int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[0]): sum += 1; print(pair, 1)
			elif int(first[1]) >= int(second[1]) and int(first[0]) <= int(second[1]): sum += 1; print(pair, 1)
			else: print(pair, 0)
		print(sum)

def part2():
	pass

if __name__ == "__main__":
	part1()
	part2()