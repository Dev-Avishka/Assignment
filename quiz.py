import random
from questions import *
from time_score import time_question_answer

def quiz(difficulty):
    score = 0
    min = 0
    max = 0
    if difficulty == "e":
        min = 1
        max = 5
    elif difficulty == "m":
        min = 4
        max = 10
    else:
        min = 10
        max = 20
    for i in range(5):
        question = create_question(min,max)
        time_answer = time_question_answer(question)
        answer = time_answer[0]
        c_answer = int(eval(question))
        if str(answer) == (c_answer):
            pass

