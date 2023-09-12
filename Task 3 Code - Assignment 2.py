# write your program here
# you'll need to import from table_data.py
import table_data
import copy
from tabulate import tabulate

Index = []
Columns = []
Rows = []
copyCounter = 1
createCounter = 1

def mainMenu():
    print("==================================")
    print("Enter your choice:")
    print("1. List tables.")
    print("2. Display table.")
    print("3. Duplicate table.")
    print("4. Create table.")
    print("5. Delete table.")
    print("6. Delete column.")
    print("7. Restore table.")
    print("0. Quit.")
    print("==================================")

def option1():
    global listTablesGlobal
    return listTablesGlobal

def option2():
    global Index
    tableIndexInput = int(input("Choose a table index (to display):\n"))
    while True:
        if tableIndexInput in Index:
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
        if tableCopyIndexInput in Index:
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
    addingTable()

def option4():
    tableCreateIndexInput = int(input("Choose a table index (to create from):\n"))
    while True:
        if tableCreateIndexInput in Index:
            break
        else:
            print("Incorrect table index. Try again.")
            tableCreateIndexInput = int(input("Choose a table index (to create from):\n"))
    columnsToKeep = input("Enter the comma-separated indices of the columns to keep:\n")
    columns = columnsToKeep.split(',')
    listOfColumns = []
    for i in columns:
        listOfColumns.append(int(i))
    global createCounter 
    newTable = [[row[i] for i in listOfColumns] for row in (table_data.tables[tableCreateIndexInput])]
    createdTableName = f"createdTable{createCounter}"
    globals()[createdTableName] = newTable
    table_data.tables.append(globals()[createdTableName])
    createCounter += 1 
    addingTable()

def option5():
    tableToDelete = int(input("Choose a table index (for table deletion):\n"))
    global Index 
    global Rows
    global Columns
    while True: 
        if tableToDelete in Index:
            break
        else: 
            print("Incorrect table index. Try again.")
            tableToDelete = int(input("Choose a table index (for table deletion):\n"))
    indexToRemove = Index.index(tableToDelete)
    #print(indexToRemove)
    Rows.pop(indexToRemove)
    Columns.pop(indexToRemove)
    Index.remove(tableToDelete)
    tableData = list(zip((Index), Columns, Rows))     
    headers = ["Index", "Columns", "Rows"]
    global listTablesGlobal
    listTablesGlobal = tabulate(tableData, headers, tablefmt="simple")
    return listTablesGlobal

def option6():
    global Index
    global Columns
    tableForColumnDelete = int(input("Choose a table index (for column deletion):\n"))
    while True:
        if tableForColumnDelete in Index:
            break
        else:
            print("Incorrect table index. Try again.")
            tableForColumnDelete = int(input("Choose a table index (for column deletion):\n"))
    columnToDelete = int(input("Enter the index of the column to delete:\n"))
    tableIndex = Index.index(tableForColumnDelete)
    Columns[tableIndex] -= 1

    for row in (table_data.tables[tableForColumnDelete]):
        if columnToDelete < len(row):
            row.pop(columnToDelete)
    tableData = list(zip((Index), Columns, Rows))     
    headers = ["Index", "Columns", "Rows"]
    global listTablesGlobal
    listTablesGlobal = tabulate(tableData, headers, tablefmt="simple")


def option7():
    global Index 
    global Rows
    global Columns
    global listTablesGlobal
    tableForRestoration = int(input("Choose a table index (for restoration):\n"))
    while True:
        if (0 <= tableForRestoration < len(table_data.tables)) and tableForRestoration not in Index:
            break
        else:
            print("Incorrect table index. Try again.")
            tableForRestoration = int(input("Choose a table index (for restoration):\n"))
    table_data.tables[tableForRestoration]
    Index.append(tableForRestoration)
    Index = sorted(Index)
    indexToAdd = sorted(Index).index(tableForRestoration)
    tableToRestore = table_data.tables[tableForRestoration]
    numColumns = len(tableToRestore[0])
    Columns.insert(indexToAdd, numColumns)
    numRows = len(tableToRestore)
    Rows.insert(indexToAdd, numRows)
    tableData = list(zip((Index), Columns, Rows))     
    headers = ["Index", "Columns", "Rows"]
    listTablesGlobal = tabulate(tableData, headers, tablefmt="simple")

def addingTable():
    global value
    Index.append(value)
    value += 1
    numColumns = len((table_data.tables[-1])[0])
    Columns.append(numColumns)
    numRows = len(table_data.tables[-1])
    Rows.append(numRows)
    global listTablesGlobal
    tableData = list(zip((Index), Columns, Rows))     
    headers = ["Index", "Columns", "Rows"]
    listTablesGlobal = tabulate(tableData, headers, tablefmt="simple")

value = 0
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
listTablesGlobal = tabulate(tableData, headers, tablefmt="simple")

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
    elif UserChoice == 4:
        option4()
    elif UserChoice == 5:
        option5()
    elif UserChoice == 6:
        option6()
    elif UserChoice == 7:
        option7()
    elif UserChoice == 0:
        break

