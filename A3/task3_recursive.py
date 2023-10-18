def evaluate_expression_rec(expr_list: list) -> float:
    if isinstance(expr_list, (int, float)):
        return expr_list
    
    operation = expr_list[0]
    
    if operation not in ['+', '-', '*', '/']:
        return float(operation)
    
    if operation == '+':
        return evaluate_expression_rec(expr_list[1]) + evaluate_expression_rec(expr_list[2])
    if operation == '-':
        return evaluate_expression_rec(expr_list[1]) - evaluate_expression_rec(expr_list[2])
    if operation == '*':
        return evaluate_expression_rec(expr_list[1]) * evaluate_expression_rec(expr_list[2])
    if operation == '/':
        return evaluate_expression_rec(expr_list[1]) / evaluate_expression_rec(expr_list[2])

if __name__ == "__main__":
    print(evaluate_expression_rec(['*', ['/', 4, 2], ['+', 8, 7]])) 
    print(evaluate_expression_rec(['-', ['+', 3, 4], ['*', ['+', 2, 5], ['*', 3, 3]])) 
    print(evaluate_expression_rec(['-', ['+', ['*', 3, 3], 4], ['*', ['+', ['+', 8, 7], 5], ['*', 3, 3]])) 
    print(evaluate_expression_rec(['+', 12, ['+', ['*', 4, 6], ['/', 12, 2]]))
    # The expected printed output:
    # 30.0
    # -56.0
    # -167.0
    # 42.0
