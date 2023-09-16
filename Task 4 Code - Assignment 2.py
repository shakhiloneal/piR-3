#import relevant external media
from tabulate import tabulate
import random

#initalise the list of rabbytes
    {"ID": 0, "Sex": "M", "Age": 0, "Dad": "", "Mom": "", "Pregnant": "No"},
    {"ID": 1, "Sex": "F", "Age": 1, "Dad": "", "Mom": "", "Pregnant": "No"},
    {"ID": 2, "Sex": "M", "Age": 2, "Dad": "", "Mom": "", "Pregnant": "No"},
    {"ID": 3, "Sex": "F", "Age": 3, "Dad": "", "Mom": "", "Pregnant": "No"},
    {"ID": 4, "Sex": "M", "Age": 4, "Dad": "", "Mom": "", "Pregnant": "No"},
    {"ID": 5, "Sex": "F", "Age": 5, "Dad": "", "Mom": "", "Pregnant": "No"},
    {"ID": 6, "Sex": "M", "Age": 6, "Dad": "", "Mom": "", "Pregnant": "No"}
]

#define classes/functions
def mainmenu():
    print("==================================")
    print("Enter your choice:")
    print("1. List Rabbytes.")
    print("2. Breed a Rabbit.")
    print("3. Wait 1 year.")
    print("0. Quit.")
    print("==================================")

def print_rabbytes():
    headers = ["ID", "Sex", "Age", "Dad", "Mom", "Pregnant"]
    data = [[r["ID"], r["Sex"], r["Age"], r["Dad"], r["Mom"], r["Pregnant"]] for r in rabbytes]
    print(tabulate(data, headers, tablefmt="simple"))

def menuoption1():
    print_rabbytes()

def menuoption2():
    print_rabbytes()

    #begin loop, only repeats if checks failed
    while True:
        print("Which rabbytes do you want to breed?")
        
        print("First parent:")
        first_parent_id = int(input(""))
        
        print("Second parent:")
        second_parent_id = int(input(""))

        #perform checks
        #iterate user entered parent id's through the list to ensure a match
        parent_one = next((rabbyte for rabbyte in rabbytes if rabbyte["ID"] == first_parent_id), None)
        parent_two = next((rabbyte for rabbyte in rabbytes if rabbyte["ID"] == second_parent_id), None)

        if not parent_one or not parent_two:
            print("Rabbit not found. Try again.")
            continue

        if parent_one["Age"] == 0:
            print("Rabbit too young.")
            continue

        if parent_one["Sex"] == parent_two["Sex"]:
            print("Rabbit cannot be of the same sex.")
            continue

        if parent_two["Pregnant"] == "Yes":
            print("Rabbit cannot be pregnant.")
            continue

        #terminate loop if checks pass
        break
    #end of loop

    #begin code for breeding between rabbytes and adds to list of rabbytes
    new_rabbyte = {
        "ID": len(rabbytes),  # Assign a new unique ID
        "Sex": random.choice(["M", "F"]),  # Randomly assign sex
        "Age": 0,  # Newborn rabbyte
        "Dad": first_parent_id,  # Update dad ID
        "Mom": second_parent_id,  # Update mom ID
        "Pregnant": "No"
    }

    #update pregnant status
    parent_one["Pregnant"] = "Yes"
    parent_two["Pregnant"] = "Yes"

    #using global dictionary
    rabbytes.append(new_rabbyte)

def menuoption3():
    #Initialise kitten_sex with a default value
    kitten_sex = ""
    #loop which iterates over all dictionaries found in rabbytes list and increments value of "Age" by 1
    for rabbit in rabbytes:
        rabbit["Age"] += 1

    #kitten born if rabbyte is pregnant, determine sex of kitten
    if rabbit["Pregnant"] == "Yes":
            if rabbit["Dad"] < rabbit["Mom"]:
                kitten_sex = "M"  # Male
            else:
                kitten_sex = "F"  # Female
    
    new_rabbyte = {
        "ID": len(rabbytes),  # Assign a new unique ID
        "Sex": kitten_sex,
        "Age": 0,  # Newborn rabbit
        "Dad": rabbit["Dad"],  # Update dad ID
        "Mom": rabbit["Mom"],  #Update mom ID
        "Pregnant": "No"
    }

    rabbytes.append(new_rabbyte)

    rabbit["Pregnant"] = "No"

#begin main
#declare loop condition
loop = True

#begin loop
while loop:
    mainmenu()
    userinput = int(input(""))
    
    #user selects menu option 1 which invokes function accordingly
    if userinput == 1:
        menuoption1()
    
    #user selects menu option 2 which invokes function accordingly
    if userinput == 2:
        menuoption2()
    
    #user selects menu option 3 which invokes function accordingly
    if userinput == 3:
        menuoption3()

    #user selects option 4 which ceases the loop and terminates the program
    if userinput == 0:
        loop = False