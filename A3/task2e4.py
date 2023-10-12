"""
A3 Task 2, e4
"""

#define functions
def evaluateExp1 (innermost: list):
    term1 = innermost[1]
    term2 = innermost[2]
    
    result = term1 / term2
    return result

def evaluateExp2 (Exp2: list):
    term1 = Exp2[1]
    term2 = Exp2[2]

    result = term1 * term2
    return result

#begin main
expr_lists = [['*', ['/', 4, 2], ['+', 8, 7]], ['-', ['+', 3, 4], ['*', ['+', 2, 5], ['*', 3, 3]]], ['-', ['+', ['*', 3, 3], 4], ['*', ['+', ['+', 8, 7], 5], ['*', 3, 3]]], ['+', 12, ['+', ['*', 4, 6], ['/', 12, 2]]]]
expression4 = expr_lists[3]

#Assign expression
expression4itemindex2 = expression4[2]

#Evaluate innermost expression, Expression 1
Exp1 = expression4itemindex2[2]
Exp1_result = evaluateExp1(Exp1)

#Evaluate next expression, working outwards, Expression 2
Exp2 = expression4itemindex2[1]
Exp2_result = evaluateExp2(Exp2)

#Evaluate next expression, working outwards, Expression 3
Exp3 = Exp1_result + Exp2_result

#Evaluate last expression, working outwards, Expression 4
Exp4 = expression4[1] + Exp3
print(Exp4)