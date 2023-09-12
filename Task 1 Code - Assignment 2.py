# write your program here
# you'll need to import from table_data.py\
import table_data
import copy
from tabulate import tabulate

Index = []
Columns = []
Rows = []
copyCounter = 1

def mainMenu():
    print("==================================")
    print("Enter your choice:")
    print("1. List tables.")
    print("2. Display table.")
    print("3. Duplicate table.")
    print("0. Quit.")
    print("==================================")

def option1():
    value = 0
    global Index
    global Columns
    global Rows
    Index.clear()
    Columns.clear()
    Rows.clear()
    for i in table_data.tables:
        Index.append(value)
        value += 1
    for i in table_data.tables: 
        numColumns = len(i[0])
        Columns.append(numColumns)
        numRows = len(i)
        Rows.append(numRows)
    tableData = list(zip(Index, Columns, Rows))
    headers = ["Index", "Columns", "Rows"]
    listTables = tabulate(tableData, headers, tablefmt="simple")
    return listTables

def option2():
    tableIndexInput = int(input("Choose a table index (to display):\n"))
    while True:
        if 0 <= tableIndexInput <len(table_data.tables):
            break
        else: 
            print("Incorrect table index. Try again.")
            tableIndexInput = int(input("Choose a table index (to display):\n"))
        

    tableToPrint = table_data.tables[tableIndexInput]
    printingTheTable = tabulate(tableToPrint[1:], headers=tableToPrint[0], tablefmt="simple")
    return printingTheTable

def option3():
    tableCopyIndexInput = int(input("Choose a table index (to duplicate):\n"))
    while True:
        if 0 <= tableCopyIndexInput <len(table_data.tables):
            break
        else: 
            print("Incorrect table index. Try again.")
            tableCopyIndexInput = int(input("Choose a table index (to duplicate):\n"))
    global copyCounter
    tableToCopy = table_data.tables[tableCopyIndexInput]
    copiedTableName = f"copiedTable{copyCounter}"
    globals()[copiedTableName] = copy.deepcopy(tableToCopy)
    table_data.tables.append(globals()[copiedTableName])
    copyCounter += 1

while True:
    mainMenu()

    while True: 
        try: 
            UserChoice = int(input(""))
            break
        except (ValueError, TypeError): 
            mainMenu()

    if UserChoice == 1:
        print(option1())
    elif UserChoice == 2:
        print(option2())
    elif UserChoice == 3:
        option3()
    elif UserChoice == 0:
        break

