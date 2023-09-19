#import relevant external media
from tabulate import tabulate
import random

#initalise the list of rabbytes
rabbytes = [
    {"ID": 0, "Sex": "M", "Age": 0, "Dad": "", "Mom": "", "Pregnant": "No", "Parent_Info": None},
    {"ID": 1, "Sex": "F", "Age": 1, "Dad": "", "Mom": "", "Pregnant": "No", "Parent_Info": None},
    {"ID": 2, "Sex": "M", "Age": 2, "Dad": "", "Mom": "", "Pregnant": "No", "Parent_Info": None},
    {"ID": 3, "Sex": "F", "Age": 3, "Dad": "", "Mom": "", "Pregnant": "No", "Parent_Info": None},
    {"ID": 4, "Sex": "M", "Age": 4, "Dad": "", "Mom": "", "Pregnant": "No", "Parent_Info": None},
    {"ID": 5, "Sex": "F", "Age": 5, "Dad": "", "Mom": "", "Pregnant": "No", "Parent_Info": None},
    {"ID": 6, "Sex": "M", "Age": 6, "Dad": "", "Mom": "", "Pregnant": "No", "Parent_Info": None}
]

#define classes/functions
class Rabbit:
    def __init__(self, dad_id, mom_id ):
        self.dad = dad_id
        self.mom = mom_id

    def getDad(self):
        return self.dad
        
    def getMom(self):
        return self.mom

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
    print(tabulate(data, headers, tablefmt="rst"))

def menuoption1():
    print_rabbytes()

def menuoption2():
    print("Which rabbytes do you want to breed?")

    while True:
        error = False        
        #begin parent one loop. Take user input for parent one ID and perform checks
        while True:
            print("First parent:")
            first_parent_id = int(input(""))
            parent_one = next((rabbyte for rabbyte in rabbytes if rabbyte["ID"] == first_parent_id), None)
            if parent_one is None:
                print("Rabbit not found. Try again.")
                continue
            if parent_one["Age"] == 0:
                print("Rabbit too young. ", end="")
                error = True
            if parent_one["Pregnant"] == "Yes":
                print("Rabbit cannot be pregnant. ", end="")
                error = True

            if error:
                print("Try again.")
                error = False
                continue
            else:
                break
        #end parent one loop

        #reinitalise error before parent two loop
        error = False

        #begin parent two loop        
        #take user input for parent two ID and perform checks
        while True:
            print("Second parent:")
            second_parent_id = int(input(""))
            parent_two = next((rabbyte for rabbyte in rabbytes if rabbyte["ID"] == second_parent_id), None)
            if parent_two is None:
                print("Rabbit not found. Try again.")
                continue
            if parent_two["Age"] == 0:
                print("Rabbit too young. ", end = "")
                error = True
            if parent_one["Sex"] == "M" and parent_two["Sex"] == "M":
                print("Rabbit cannot be male. ", end = "")
                error = True
            if parent_one["Sex"] == "F" and parent_two["Sex"] == "F":
                print("Rabbit cannot be female. ", end = "")
                error = True
            if parent_two["Pregnant"] == "Yes":
                print("Rabbit cannot be pregnant. ", end = "")
                error = True

            if error:
                print("Try again.")
                error = False
                continue
            else:
                break
        #end of parent two loop

        #update pregnant status and store parent ID to pregnant rabbit
        if parent_one["Sex"] == "F" and parent_two["Sex"] == "M":
            parent_one["Pregnant"] = "Yes"
            parent_id_information = Rabbit(parent_two["ID"], parent_one["ID"])
            parent_one["Parent_Info"] = parent_id_information
        else:
            parent_two["Pregnant"] = "Yes"
            parent_id_information = Rabbit(parent_one["ID"], parent_two["ID"])
            parent_two["Parent_Info"] = parent_id_information
        
        #end of menuoption2 loop
        break

    #end menuoption2()


def menuoption3():
    #intialise list of newborns for rabbits currently pregnant
    newborn_list = []

    #age all rabbits by 1
    for rabbit in rabbytes:
        rabbit["Age"] += 1
    
    #establish maxID in current list
    max_id = max(r["ID"] for r in rabbytes)

    #iterate through rabbytes list to locate pregnant rabbit
    for rabbit in rabbytes:
        if rabbit ["Pregnant"] == "Yes":
            #assign newborn ID and increment max ID
            newborn_id = max_id + 1
            max_id += 1

            #establish dad and mom ID's
            dad_id = rabbit["Parent_Info"].getDad()
            mom_id = rabbit["Parent_Info"].getMom()
            
            #determine newborn rabbit sex
            if dad_id < mom_id:
                newborn_sex = "M"
            else:
                newborn_sex = "F"

            #create newborn
            newborn = {
                "ID": newborn_id,
                "Sex": newborn_sex,
                "Age": 0,
                "Dad": rabbit["Parent_Info"].getDad(),
                "Mom": rabbit["Parent_Info"].getMom(),
                "Pregnant": "No"
            }

            #update pregnant status of rabbit
            rabbit["Pregnant"] = "No"

            #add newborn details to newborn list
            newborn_list.append(newborn)

    #end of loop

    #add newborn list to rabbytes list
    rabbytes.extend(newborn_list)            

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