"""
Assignment 2, Task 5.
This task continues upon the basis of what was constructed in Task 4.
Here, there if further functionality implemented by adding a menu option designed to find siblings of a particular rabbit.
Additonally, there is another menu option added to locate a specific rabbit's step siblings.
"""

#import relevant external media
"""
Importing the tabulate module enables the correct formatting and display of the rabbytes table in the console.
"""
from tabulate import tabulate

#initalise the list of rabbytes
rabbytes = [
    """
    This list is initalised at the beginning of the program containing information for seven rabbits.
    Each rabbit is stored in the list as item with its information being stored in a dictionary containing key value pairs relating to its details.
    The list is later modified as the rabbits breed and newborns are added.
    """

    {"ID": 0, "Sex": "M", "Age": 0, "Dad": None, "Mom": None, "Pregnant": "No", "Parent_Info": None},
    {"ID": 1, "Sex": "F", "Age": 1, "Dad": None, "Mom": None, "Pregnant": "No", "Parent_Info": None},
    {"ID": 2, "Sex": "M", "Age": 2, "Dad": None, "Mom": None, "Pregnant": "No", "Parent_Info": None},
    {"ID": 3, "Sex": "F", "Age": 3, "Dad": None, "Mom": None, "Pregnant": "No", "Parent_Info": None},
    {"ID": 4, "Sex": "M", "Age": 4, "Dad": None, "Mom": None, "Pregnant": "No", "Parent_Info": None},
    {"ID": 5, "Sex": "F", "Age": 5, "Dad": None, "Mom": None, "Pregnant": "No", "Parent_Info": None},
    {"ID": 6, "Sex": "M", "Age": 6, "Dad": None, "Mom": None, "Pregnant": "No", "Parent_Info": None}
]

#define classes/functions
class Rabbit:
    """
    This class inherites the parental ID's of a pregnant rabbit so that the parents' information is passed down with the newborn. 
    The methods include an intialising an instance of the Rabbit class with the ID (integer) value of the Dad and Mom's ID.
    Two further methods exist to the return their values, respectively.
    """
    def __init__(self, dad_id, mom_id ):
        self.dad = dad_id
        self.mom = mom_id

    def getDad(self):
        return self.dad
        
    def getMom(self):
        return self.mom

def mainmenu():
    """
    A basic function representing the main menu of the program, with a design implementation for neat representation in the console.
    """
    print("==================================")
    print("Enter your choice:")
    print("1. List Rabbytes.")
    print("2. Breed a Rabbit.")
    print("3. Wait 1 year.")
    print("4. Find siblings.")
    print("5. Find step-siblings.")
    print("0. Quit.")
    print("==================================")

def print_rabbytes():
    """
    Function that lists the rabbits in an appropriate table format. 
    It also utilises the tabulate module for appropriate representation in the console.
    """
    headers = ["ID", "Sex", "Age", "Dad", "Mom", "Pregnant"]
    data = [[r["ID"], r["Sex"], r["Age"], r["Dad"], r["Mom"], r["Pregnant"]] for r in rabbytes]
    
    #specify column alignments
    colalign = ["right", "left", "right", "left", "left", "left"]

    print(tabulate(data, headers, tablefmt="rst", colalign = colalign))

def menuoption1():
    """
    Function that lists the rabbits onto the console by calling the print_rabbytes function
    """
    print_rabbytes()

def menuoption2():
    """
    Function that breeds two rabbits through the implementation of a while loop. 
    Certain checks are performed to validate the user's input before impregnating a female rabbit and storing the parental information to be passed on to the newborn.
    If the user has entered an illegal option, a message is printed to the console explaining the reason for error.
    The pregnant status is also updated in the list.
    """
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
    """
    Function which ages all rabbits by one year. 
    Rabbits which are currently pregnant also give birth and the newborn/s are added to the list of rabbytes.
    """

    #intialise list of newborns for rabbits currently pregnant
    newborn_list = []

    #age all rabbits by 1
    for rabbit in rabbytes:
        rabbit["Age"] += 1
    
    #establish maxID in current list
    max_id = max(r["ID"] for r in rabbytes)

    #begin loop
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
#end menuoption3()       

def menuoption4():
    """
    Function is called as a result of user selecting Option 4 in the menu.
    The user's specified rabbit is validated to ensure it is a valid choice from the list of rabbytes.
    The user indicated rabbit's siblings are detected (if any) and printed to the console.
    """
    while True:
        print("Rabbit to find siblings of:")
        user_inputSibling = int(input(""))
        
        #check to see if user has entered valid input
        validUserSibling = next((rabbyte for rabbyte in rabbytes if rabbyte["ID"] == user_inputSibling), None)
        if validUserSibling == None:
            print("Rabbit not found. Try again.")
            continue

        #establish parents of user selected rabbit
        dadID = validUserSibling["Dad"]
        momID = validUserSibling["Mom"]

        #find all rabbits which have the same Dad and Mom ID's
        detectSiblings = [rabbit["ID"] for rabbit in rabbytes if (rabbit["ID"] != validUserSibling["ID"] and rabbit["Dad"] != None and rabbit["Mom"] != None) and rabbit["Dad"] == dadID and rabbit["Mom"] == momID]

        #print the user selected rabbit's siblings if any
        print("The siblings of Rabbit", validUserSibling["ID"], "are:")
        for sibling in detectSiblings:
            print(sibling)
        #cease loop
        break
    #end loop
#end menuoption4()                   

def menuoption5():
    """
    Function is called as a result of the user selecting Option 5 in the menu.
    The design of this function is very similar to menuoption4().
    However, the distinguishing factor here being the step siblings of a user specified rabbit are detected and printed to the console.
    Similarly the previous function, certain validation checks are completed to ensure the user's input is legal.
    """
    while True:
        print("Rabbit to find step-siblings of:")
        user_enterStepsibling = int(input(""))
        
        #check user entered valid input
        validUserStepSibling = next((rabbit for rabbit in rabbytes if rabbit["ID"] == user_enterStepsibling), None)
        if validUserStepSibling == None:
            print("Rabbit not found. Try again.")
            continue

        #establish parents of user selected rabbit
        dadID = validUserStepSibling["Dad"]
        momID = validUserStepSibling["Mom"]

        detectSiblings = [rabbit for rabbit in rabbytes if (rabbit["ID"] != validUserStepSibling["ID"] and rabbit["Dad"] != None and rabbit["Mom"] != None) and rabbit["Dad"] == dadID and rabbit["Mom"] == momID]
        
        #find rabbit's half siblings
        halfSiblingslist = []
        for rabbit in rabbytes:
            if rabbit["ID"] != validUserStepSibling["ID"]:
                if rabbit["Dad"] == dadID or rabbit["Mom"] == momID:
                    if rabbit["ID"] not in detectSiblings:
                        halfSiblingslist.append(rabbit)
        
        #find rabbit's step siblings
        stepSiblingsList = []
        for rabbit in rabbytes:
            if rabbit["ID"] != validUserStepSibling["ID"]:
                    for halfSibling in halfSiblingslist:
                        if rabbit not in detectSiblings and rabbit not in stepSiblingsList and rabbit not in halfSiblingslist and (rabbit["Dad"] == halfSibling["Dad"] or rabbit["Mom"] == halfSibling["Mom"]):
                            stepSiblingsList.append(rabbit)
        
        #print the user selected rabbit's step-siblings if any
        print("The step-siblings of Rabbit", validUserStepSibling["ID"], "are:")
        for rabbit in stepSiblingsList:
            print(rabbit["ID"])

        #cease loop
        break

    #end loop
#end menuoption5()                   
#end class/function definitions

#begin main
"""
The main function of the program displays the list of options available to the user to interact with and select an option. 
It exists in a while loop which will indefinitely operate until the user chooses to terminate the program.
"""
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

    #user selects menu option 3 which invokes function accordingly
    if userinput == 4:
        menuoption4()

    #user selects menu option 3 which invokes function accordingly
    if userinput == 5:
        menuoption5()

    #user selects option 4 which ceases the loop and terminates the program
    if userinput == 0:
        loop = False
