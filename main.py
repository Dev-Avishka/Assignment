import json
import random
from quiz import Give_Quiz

def Main_FUNC():
    while True:
        print("Welcome to the Math Quiz!")
        print("Choose Easy, Medium, or Hard by typing the letter for the difficulty")
        print("Type 'exit' to exit anytime")

        # Get difficulty
        difficulty = input("Easy(e), Medium(m), Hard(h), Exit(ex): ").lower()
        if difficulty == "exit":
            break
        

        try:
            if (difficulty != "ex"):
                Give_Quiz(difficulty)
            else:
                exit()
        except Exception as e:
            print(f"Error: {e}")
            continue  # Retry on error

if __name__ == "__main__":
    Main_FUNC()