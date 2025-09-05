import json
import random 
from quiz import quiz

def main():
    print("Chose Easy, Medium or Hard by typing the letter for the difficulty")
    print("Type exit to exit anytime")

    #get difficulty
    difficulty= input("Easy(e),Medium(m),Hard(h): ")
    try:
        quiz(difficulty)
    except Exception as e:
        print(e)
        exit()

if __name__ == "__main__":
    main()
