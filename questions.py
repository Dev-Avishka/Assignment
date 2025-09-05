import random as r # this will allow for the use of r.randint rather than random.randint

#function to create the question
def create_question(min_val,max_val):
    int_1 = r.randint(min_val,max_val) 
    int_2 = r.randint(min_val,max_val)
    operation = select_operation()
    question = (f"{int_1} {operation}  {int_2}")
    return question


#function to select the operation
def select_operation():
    randnum = r.randint(1,2)
    operation = ""
    if randnum == 1:
        operation = "+"
    elif randnum == 2:
        operation = "-"
    return operation

