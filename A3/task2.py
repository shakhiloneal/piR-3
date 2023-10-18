def evaluate_expression_iter(expr_list: list) -> float:
    #raise NotImplementedError
    
    #initalise stack, store results from evaluating the sublists
    stack = []

    for j in expr_list:
        # If the element is a list, evaluate it and push the result onto sum.
        if isinstance(j, list):
            operator = j[0]
            operand_1 = j[1]
            operand_2 = j[2]

            if operator == '+':
                result = operand_1 + operand_2
            if operator == '-':
                result = operand_1 - operand_2
            if operator == '*':
                result = operand_1 * operand_2
            if operator == '/':
                result = operand_1 / operand_2
        
            #push result into stack
            stack.append(result)
        
        else:
            #If the element is an operator, apply it to the top two elements onto sum.
            operator = j
            operand_2 = stack.pop()
            operand_1 = stack.pop()

            if operator == '+':
                stack.append(operand_1 + operand_2)
            elif operator == '-':
                stack.append(operand_1 - operand_2)
            elif operator == '*':
                stack.append(operand_1 * operand_2)
            elif operator == '/':
                stack.append(operand_1 / operand_2)

    return stack[0]


if __name__ == "__main__":
    expr_lists = [['*', ['/', 4, 2], ['+', 8, 7]], 
                  ['-', ['+', 3, 4], ['*', ['+', 2, 5], ['*', 3, 3]]],
                    ['-', ['+', ['*', 3, 3], 4], ['*', ['+', ['+', 8, 7], 5], ['*', 3, 3]]],
                      ['+', 12, ['+', ['*', 4, 6], ['/', 12, 2]]]]
    count = 0
    while count < 4:
        print(evaluate_expression_iter(expr_lists[count]))
        count += 1