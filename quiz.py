import random
from time import sleep, time
from questions import *
from restart import Restart_The_Quiz
from time_score import time_question_answer
from scores import *


table = []


def Give_Quiz(difficulty):
    score_system = []
    score = 0
    min = 0
    max = 0
    table = []  # Initialize table locally to avoid global issues
    if difficulty == "e":
        min = 1
        max = 5
        score_system = easy
    elif difficulty == "m":
        min = 4
        max = 10
        score_system = mid
    elif difficulty == "h":
        min = 10
        max = 20
        score_system = hard
    else:
        print("invalid difficulty restarting ...")
        sleep(1)
        print("invalid difficulty restarting .")
        if Restart_The_Quiz():
            return

    for i in range(5):
        question = create_question(min, max)
        time_answer = time_question_answer(question, (i+1))
        answer = time_answer[0]
        c_answer = int(eval(question))
        time_to_answer = time_answer[1]
        time_to_answer = round(time_to_answer,0)
        if str(answer) == str(c_answer):
            c_score = 0
            for j in score_system:
                if time_to_answer <= float(j[0]):
                    c_score = j[1]
                    break
            print(f"Correct! you answered in {time_to_answer:.0f} second(s) - ({c_score}) points awarded")
            score += c_score  # Accumulate score
            table.append([(i+1), True, time_to_answer])
        else:
            print(f"Incorrect! you answered in {time_to_answer:.0f} second(s) - no points awarded")
            table.append([(i+1), False, time_to_answer])

    print("Breakdown")
    print("Question     Correct     Time")
    for d in table:
        print(f"{d[0]}          {d[1]}     {d[2]:.0f}s")
    print(f"Total Score: {score}")
    if Restart_The_Quiz():
        return