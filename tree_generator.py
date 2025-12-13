import math

tree = []

def main(height):
	width = 2 * height - 1
	middle = math.floor(width / 2)
	middle_2 = middle
	count_stars = 1
	count_stars_2 = count_stars
	for i in range(1, height):
		for j in range(1, width):
			if middle_2 > 0:
				tree.append(" ")
				middle_2 -= 1
			else:
				for k in range(0, count_stars_2):
					tree.append("*")
					count_stars_2 -= 1
		middle -= 1
		middle_2 = middle
		count_stars += 2
		count_stars_2 = count_stars
		tree.append("\n")
	for l in range(0, math.floor(width/2)):
		tree.append(" ")
	tree.append("|")
	return tree
