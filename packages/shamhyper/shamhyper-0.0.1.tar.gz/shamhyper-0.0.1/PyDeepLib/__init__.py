import os

def clear():
	"""Clears the terminal screen"""
	os.system('cls' if os.name == 'nt' else 'clear')