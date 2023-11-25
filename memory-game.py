from random import randint, choice
from time import sleep

def print_string(string):
    for i in string:
        print(i)
        sleep(1)
        print("\x1b[2J")
        sleep(0.2)

def gameplay_loop(symbols):
    word = ""
    playing = True
    while playing:
        word = word + choice(symbols)
        print_string(word)
        input_word = input("What was the word? (Case sensitive!)\n")
        if input_word != word:
            playing = False
            print("Incorrect! Too bad! :(")
            sleep(1)
        else:
            print("Correct! :D")
            sleep(1)
        print("\x1b[2J")

while True:
    print("\x1b[2JMemory Game!\n")
    start = input('Press "Enter" to continue.\n')
    print("\x1b[2J")
    gameplay_loop("ABCD")
    end = input("Keep playing? (y/n): ")
    if end.lower() == "n":
        print("Okay! Bye! :D")
        exit(0)
