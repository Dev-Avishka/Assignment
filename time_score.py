import time

def time_question_answer(question):
    start_time = time.perf_counter()
    try:
        answer = int(input(f"Enter the answer to {question}: "))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return [answer,elapsed_time]
    except ValueError:
        elapsed_time = start_time
        return [None, elapsed_time]
