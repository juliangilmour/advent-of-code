
priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def part1():

	sum = 0

	with open("/home/julia/repos/advent-of-code/day3/input.txt") as file:
		lines = file.read()
		lines = lines.split("\n")
		for line in lines:
			c1, c2 = line[:len(line)//2], line[len(line)//2:]
			for char in c1:
				if char in c2:
					print(c1, c2, char, sum, priority.index(char) + 1)
					sum += priority.index(char) + 1
					break
		print(sum)

def part2():
	sum = 0
	with open("/home/julia/repos/advent-of-code/day3/input.txt") as file:
		lines = file.read()
		lines = lines.split("\n")
		for i in range(0, len(lines), 3):
			c1, c2, c3 = lines[i], lines[i+1], lines[i+2]
			for char in c1:
				if char in c2 and char in c3:
					print(c1, c2, char, sum, priority.index(char) + 1)
					sum += priority.index(char) + 1
					break
		print(sum)


if __name__ == "__main__":
	part1()
	part2()