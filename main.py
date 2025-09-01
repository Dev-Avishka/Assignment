import json
import random 
from readjson import readjsonfile
from quiz import quiz

def main():
    print("Chose Easy, Medium or Hard by typing the letter for the difficulty")
    print("Type exit to exit anytime")

    #get difficulty
    difficulty= input("Easy(e),Medium(m),Hard(h): ")

    file = ""
    if difficulty == "e":
        file = "./easy.json"
    elif difficulty == "m":
        file = "./medium.json"
    elif difficulty == "h":
        file = "./hard.json"
    else:
        print("Invalid input quitting now")
        exit()
    try:
        quiz_data = readjsonfile(file)
        quiz(quiz_data)
    except Exception as e:
        print(e)
        exit()

if __name__ == "__main__":
    main()
