import time

# times the answer to a question

def time_question_answer(question,question_num):
    start_time = time.perf_counter()
    try:
        print(f"Question {question_num} out of 5")
        answer = int(input(f"Enter the answer to {question}: "))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return [answer,elapsed_time]
    except ValueError:
        elapsed_time = start_time
        return [None, elapsed_time]
