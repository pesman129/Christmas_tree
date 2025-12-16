from random import randint
from os import system
from time import sleep
from termcolor import colored
import tree_generator
from sys import argv, platform

clear = {"linux": "clear", "macos": "clear", "windows": "cls"}

tree = tree_generator.main(int(input("What is the height of the tree: ")))
colors = {1: "red", 2: "blue", 3: "yellow"}
leaf_color = "green"

if "let-it-snow" in argv:
	colors[4] = "green"
	leaf_color = "white"

while True:
	for i in tree:
		if i == "*":
			cube = randint(1, 3)
			if cube == 1:
				print(colored('*', colors[randint(1, len(colors))]), end="")
			else:
				print(colored("*", leaf_color), end="")
		elif i == "|":
			print(i)
			sleep(0.5)
			system(clear[f"{platform()}"])
		else:
			print(i, end="")

