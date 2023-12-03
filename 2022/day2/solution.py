
counterpick = {
	"A": "B",
	"B": "C",
	"C": "A"
}
# tie = {
# 	"A": "X",
# 	"B": "Y",
# 	"C": "Z"
# }
lose = {
	"B": "A",
	"C": "B",
	"A": "C"
}
choice_scores = {
	"A": 1,
	"B": 2,
	"C": 3
}

win_score = 6
def part1():
	with open("input.txt") as file:
		lines = file.read()
		lines = lines.split("\n")
		score = 0
		for line in lines:
			line = line.split(" ")
			first, second = line[0], line[1]
			if counterpick[first] == second: score += 6
			if map[first] == second: score += 3
			score += choice_scores[second]
			print(first, second, score)
		print(score)

def part2():
	with open("input.txt") as file:
		lines = file.read()
		lines = lines.split("\n")
		score = 0
		for line in lines:
			line = line.split(" ")
			first, second = line[0], line[1]
			if second == "X": score += choice_scores[lose[first]] + 0
			if second == "Y": score += choice_scores[first] + 3
			if second == "Z": score += choice_scores[counterpick[first]] + 3
			print(first, second, score)
		print(score)

if __name__ == "__main__":
	part2()