"""
A3 Task 2, e3
"""

#define functions
def evaluateInnerList1 (InnermostList: list):
    term1 = InnermostList[1]
    term2 = InnermostList[2]

    result = term1 * term2
    return result

def evaluateList1(list1: list):
    InnermostList = [list1[1]]
    InnermostListResult = evaluateInnerList1(InnermostList)

    result = InnermostListResult + list1[2]
    return result

#begin main
expr_lists = [['*', ['/', 4, 2], ['+', 8, 7]], ['-', ['+', 3, 4], ['*', ['+', 2, 5], ['*', 3, 3]]], ['-', ['+', ['*', 3, 3], 4], ['*', ['+', ['+', 8, 7], 5], ['*', 3, 3]]], ['+', 12, ['+', ['*', 4, 6], ['/', 12, 2]]]]
expression3 = expr_lists[2]
#print(expression3)

#split expression 3
list1 = [expression3[1]]
print(list1)
list1Result = evaluateList1(list1)
print(list1Result)
print("")
list2 = [expression3[2]]
print(list2)

