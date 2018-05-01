# ----------------------------------------------------------------------------------------------------------------------
# Title: Assignment 05
# Dev: William Burdick
# Date: 04/30/2018
# Description: Read and write a text file
# This project is like to the last one, but this time The To Do file will contain two columns of data (Task, Priority)
# which you store in a Python dictionary. Each Dictionary will represent one row of data and these rows of data
# are added to a Python List to create a table of data.
# ----------------------------------------------------------------------------------------------------------------------
# When the program starts, load each row of data from the To Do.txt text file into a Python dictionary.
# You can use a for loop to read a single line of text from the file and then place the data
# into a new dictionary object.

print("Hello, this program keeps track of the To Do items for your household")
#ToDoList = open("D:\UW_Python_Class\Assignment05\ToDo.txt", "r")  # Open the file To Do.txt
#print (ToDoList)
# for line in ToDoList:
# Task1 = ToDoList.readline(0)
# Task2 = ToDoList.readline(1)
# print (Task1)
# print (Task2)
print("Here are the items in your list:")
ToDoRow1 = {"ID": 1, "Task": "Clean House", "Priority": "Low"}
ToDoRow2 = {"ID": 2, "Task": "Pay Bills", "Priority": "High"}
ToDoDictionary = [ToDoRow1, ToDoRow2]
print(ToDoDictionary)
# ToDoList.close()
TableHeader = ["ID", "Task", "Priority"]
NewRow = "\n"  # Add the new dictionary row into a Python list object
TaskList = [TableHeader + ToDoDictionary]  # Now the data will be managed as a table).
# Allow the user to Add or Remove tasks from the list using numbered choices.
# Menu of Options
Menu1 = "#1 Show current data"
Menu2 = "#2 Add a new item"
Menu3 = "#3 Remove an existing item"
Menu4 = "#4 Save Data to File"
Menu5 = "#5 Exit Program"
print (Menu1)
print (Menu2)
print (Menu3)
print (Menu4)
print (Menu5)
ItemId = 2
UserChoice = 0
while UserChoice != 5:  # If boolean is not equal to 5 loop will continue
    UserChoice = int(input("Please choose from the Menu:"))
    if UserChoice == 1:
        print ("Current list:")
        print(TaskList)
    elif UserChoice == 2:
        NewId = (ItemId + 1)
        ItemName = raw_input("Please enter the New Item:")
        ItemPriority = raw_input("Please enter the Priority:")
        NewRow = [NewId, ItemName, ItemPriority]
        TaskList.append(NewRow)
        ItemId = NewId
        print (Menu1)
        print (Menu2)
        print (Menu3)
        print (Menu4)
        print (Menu5)
    elif UserChoice == 3:
        #print(TaskList)
        #RowToRemove = int(input("Please enter the ID of the Task to remove:"))
        #for line in TaskList:
            #TaskList.remove([RowToRemove])
        #print (TaskList)
        print (Menu1)
        print (Menu2)
        print (Menu3)
        print (Menu4)
        print (Menu5)
        continue
    elif UserChoice == 4:
        File = open("D:\UW_Python_Class\Assignment05\ToDo.txt", "w")  # Open/write file named To Do.txt
        File.write(str(TaskList))  # Write the Dictionary to the file
        File.close()  # Close the file
        print ("File saved")
        print (Menu1)
        print (Menu2)
        print (Menu3)
        print (Menu4)
        print (Menu5)
        continue
    elif UserChoice == 5: # User enters n to end loop
        break  # Close loop
print ("Program Closed")
print("---------------------------------------------------------------------------------------------------------------")