#   Purpose: List the NBNA champions in descending order based on their wins between 1947 to 2022. Then ask the user which year they'd like to know the winning team. Then we will display the wincount for the user
#   .lower() used throughout the program to reduce errors
#   .strip() was also used throughout the program to prevent read errors due to the new lines in the .txt file provided

import time #importing timer
WinCount = dict() #Key = TeamName; Value = number of times team won
Yearly = dict() #Key = Year from 1947 to 2022; Value = Name of the team that won that year
names = list() #List for list of names in raw text

def OutputSort():
    OutputSort=list() #Created an output sorted list
    for num,name in WinSorting: #We are now reversing the WinSorting list to be be the correct Key Value pair before printing
        OutputSort.append((name,num)) #Key = TeamName; Value = number of times team won
    print(*OutputSort,sep='\n') #Printing each team and number of wins by descending order based on their wins

def close():
    print("closing.") #printing close confirmation
    time.sleep(1) #1 second timer
    print("closing..") #continuing close
    time.sleep(1) #1 second timer
    print("closing...") #continuing close
    time.sleep(1) #1 second timer
    print("\n\n\nPress cancel to cancel close\n\n\n") #cancel to stop close
    exit() #closing
def PrintLine():
    print("\n----------------------------\n") # Line text for uniformity
    

def inputting(): #Created input function to loop
    inp=input("Please enter a year in the range of 1947 through 2022, otherwise type \"close\" to close the program\n") #Gathering input from user, with "exit" as closing the program
    try: # 1. this will trigger if it can be converted to an integer
        inp=int(inp) #integer conversion
        string=str(inp) #string created from the input
        if inp > 1946: #checking if integer is greater than 1946
            if inp < 2023: #checking if integer is less than 2023
                print("In the year "+string+" the "+Yearly[string]+" won the NBNA champion, and they have won a total of "+str(WinCount.get(Yearly[string]))+" times.\n\n") #printing results
            else: print("*Error*: Number is Greater than 2022, please try again\n\n") #Number was greater than 2023
        else: print("*Error*: Less than 1946, please try again\n\n") #Number was less than 1946
    except: # 1. this will trigger if it cannot be converted to an integer
        try: #2. this will trigger if the input is a string that can be lowercased
            if inp.lower()=="close": #checking if input is "close" to close the program
                close() #closing
            else:
                print("*Error*: Please only use whole numbers between 1947 and 2022\n\n")
        except: #2. if all else fails, likely the user inputted anything other than a number between 1947-2022 and was not any variation of "close"
            print("*Error*: Please only use whole numbers between 1947 and 2022\n\n")

    
fhand = open("NBA_champ_1947_2022.txt") #Opening file
for line in fhand: #checking each line in file
    if line.startswith("Year "): #Finding lines that start with "Year "
        TeamL = line.find(': ') #Finding where the line starts for ": "
        Yearly[line[5:9]]=line[TeamL+2:].strip() #Taking the year as the key, and the name of the team as the value
        names.append(line[TeamL+2:].strip()) #Adding each name of the team to the list "names"

for name in names: # Counting for each name in WinCount
    WinCount[name] = WinCount.get(name,0)+1 # Team name set as the key, and the count of each win as the value

WinSorting=list() #Assigning a list for sorting the wins
for k,v in WinCount.items(): #Adding the key value pair in reverse to be opposite of WinCount
    WinSorting.append((v,k)) #Value = TeamName; Key = number of times team won
WinSorting.sort(reverse=True) #Sorting it by highest amount of wins

print("Team Name, Winning Times") # Header text
PrintLine() #printing line
OutputSort() #Outputting the sorted strings
PrintLine() #printing line again
while True: #looping
    inputting() #accepting input from user
