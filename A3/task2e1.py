"""
A3 Task 2, e1.
"""
#def functions
def evaluate_exp1(exp1: list):
    term1 = exp1[1]
    term2 = exp1[2]

    result = term1 / term2
    return result

def evaluate_exp2(exp2: list):
    term1 = exp2[1]
    term2 = exp2[2]

    result = term1 + term2
    return result

#begin main
full_exp = ['*', ['/', 4, 2], ['+', 8, 7]]
exp1 = full_exp[1]
exp2 = full_exp[2]

#evaluatefull_exp[1]
exp1Result = evaluate_exp1(exp1)
#evaluatefull_exp[2]
exp2Result = evaluate_exp2(exp2)

#evaluate and print full sum
finalResult = exp1Result * exp2Result
print(finalResult)
