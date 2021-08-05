"""Randomly walk through notes under the directory."""
import os
from random import randint
files = os.listdir("./")

total = len(files)


def random_note():
    """Show a random note and edit it."""
    index = randint(0, total-1)
    print(files[index])
    ans = input("Want to print the file? Y or N: ")

    if ans == "Y":
        filepath = files[index]
        f = open(str(filepath), "r", encoding="UTF-8")
        for line in f:
            print(line)
        ans = input("Want to edit the file? Y or N: ")
        if ans == "Y":
            os.startfile(str(filepath))
    elif ans == "N":
        random_note()
    elif ans == "Q":
        pass


random_note()