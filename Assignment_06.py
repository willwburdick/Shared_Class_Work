# -------------------------------------------------#
# Title: Working with functions and classes*
# Dev:   RRoot
# Date:  Sept 16, 2017
# ChangeLog: (Who, When, What)
#   RRoot, 09/16/2017, Created Script
#   WBurdick, 05/7/2018, Changed title and configured script to work with functions and classes
# -------------------------------------------------#
# Instructions: place the code you created for working with your To Do.txt file into Functions and a Class.
# ---------------------------------------------------------------------------------------------------------------------#

# Programming: Define the data
fileName = "D:\UW_Python_Class\Assignment06\ToDo.txt"  # This is where the original data resides
iD = None  # The ID for the items in the To Do list.
task = None  # A string that will be the user entered Task
priority = None  # A string that the will be the user entered Priority
dicRow = None  # The Dictionary that the data in the file will load into
toDoList = None  # The list that will make up the items in the dictionary
userChoice = None # Integer user will enter based on Menu Options
option1 = None  # Option 1 on menu
option2 = None  # Option 2 on menu
option3 = None  # Option 3 on menu
option4 = None  # Option 4 on menu
option5 = None  # Option 5 on menu
MenuText = ("""  
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)  # This is the list of options that is printed everytime the user continues the program
# ---------------------------------------------------------------------------------------------------------------------#

# Processing: Create the classes and functions with the variables
# 1st Class is the reading of the file and writing the data in that file to a dictionary
class ToDoDictionary(object):  # Read the file To Do.txt and write to a dictionary
    @staticmethod
    def dictRead(iD, task, priority,):
        fileOpen = open(fileName, "r")  # Open the file and set to read
        for line in fileOpen:  # Look at each line in the file
            strData = line.split(",")  # readline() reads a line of the data into 2 elements
            iD = 1  # Add an ID to each line...having trouble with this
            task = (strData[0].strip())  # strip the first item in the dictionary for the task
            priority = (strData[1].strip())  # strip the second item in the dictionary for the priority
        return strData, iD, task, priority  # return the values of each line
        fileOpen.close()  # Close the file
    print(dictRead())  # Print the dictionary of items

# 2nd Class is the user interactive portion of this script
class MenuProcessor(object):  # This is a class of functions that will return a value for each option per the menu above
    @staticmethod  # Static method per instructions
    def option1(List):  # Define the first option to see the list of tasks
        List = toDoList
        return List
    def option2(Item, Priority):  # Define the second option to add a task and a priority
        Item = raw_input("")
        Priority = raw_input("")
        return Item, Priority
    def option3(delItem):  # Define the third option to delete a task
        delItem =
        return
    def option4(save):  # Define the fourth option to save the list to a file
        save = File.write(str(toDoList))
        return save
    def option5(loopbreak):  # Define the fifth option to break close the program
        loopbreak =
        return loopbreak

# ---------------------------------------------------------------------------------------------------------------------#
print("This program keeps track of the To Do items for your household")  # Tell user program intent
print("Here are the items in your list:")  # Let user know what is already in the list from the To Do.txt file
print(toDoList)
# Presentation: Give the user the opportunity to interact
print(MenuText) # Print the Menu
MenuProcessor()  # Call the Class MenuProcessor
while userChoice != 5:  # If boolean is not equal to 5 loop will continue
    userChoice = int(input("Please choose from the Menu:"))
    if userChoice == 1:
     print(toDoList)
    elif userChoice == 2:
        NewId = (iD + 1)
        ItemName = raw_input("Please enter the New Item:")
        ItemPriority = raw_input("Please enter the Priority:")
        NewRow = [NewId, ItemName, ItemPriority]
        toDoList.append(NewRow)
        iD = NewId
        print (MenuText)
    elif userChoice == 3:
        #print(TaskList)
        #RowToRemove = int(input("Please enter the ID of the Task to remove:"))
        #for line in TaskList:
            #TaskList.remove([RowToRemove])
        #print (TaskList)
        print (MenuText)
        continue
    elif userChoice == 4:
        File = open("D:\UW_Python_Class\Assignment06\ToDo.txt", "w")  # Open/write file named To Do.txt
        File.write(str(toDoList))  # Write the Dictionary to the file
        File.close()  # Close the file
        print ("File saved")
        print (MenuText)
        continue
    elif userChoice == 5: # User enters n to end loop
        break  # Close loop
print ("Program Closed")
print("---------------------------------------------------------------------------------------------------------------")