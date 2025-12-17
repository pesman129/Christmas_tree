from random import randint
from os import system
from time import sleep
from termcolor import colored
import tree_generator
import platform
from sys import stdout

term = stdout.isatty()
tree = tree_generator.main(int(input("What is the height of the tree: ")))
colors = {1: "red", 2: "blue", 3: "yellow"}

while True:
	for i in tree:
		if i == "*":
			cube = randint(1, 3)
			if cube == 1:
				print(colored('*', colors[randint(1, 3)]), end="")
			else:
				print(colored("*", "green"), end="")
		elif i == "|":
			print(i)
			sleep(0.5)
			if term == True:
				print("\033[2J\033[H", end="")
			else:
				print("\n" * 100)
		else:
			print(i, end="")
