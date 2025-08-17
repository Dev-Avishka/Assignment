import random

def quiz(quiz_data):
    score = 0
    
    for item in quiz_data:
        print(f"\nQuestion: {item['question']}")
        try:
            if 'answer_list' not in item:
                print(f"ERROR: 'answer_list' key not found in item: {item}")
                continue
            
            all_answers = item['answer_list'] + [item['correct_answer']]
            random.shuffle(all_answers)
            
            print("Answers:")
            
            correct_answer = item['correct_answer']
            
            for answer in all_answers:
                print(answer)
            
            prompt_answer = input("Enter your answer: ")
            
            if prompt_answer == correct_answer:
                score += 1
                print(f"good job your score is now {score}")
            elif prompt_answer == "exit":
                exit()
            else:
                print("Incorrect No Points awarded" )
        
        except KeyError as e:
            print(f"ERROR: Missing key {e} in item: {item}")
    print(f"Your Final Score is {score} ")

