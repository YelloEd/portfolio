import random #importing random
Choices = ("Rock","Paper","Scissors") #Listed choices
playerselect=0 #player input choice
Count= {"Win":0,"Loss":0,"Draw":0} #setting a dictionary of Win, Loss, Draw
TotalCount = Count["Loss"]+Count["Win"]+Count["Draw"]

def selection(): #selection function
    if type(inp)==str: #as long as input is string...
        if inp.lower()==Choices[0].lower(): return 0 #Chose rock
        elif inp.lower()==Choices[1].lower(): return 1 #Chose paper
        elif inp.lower()==Choices[2].lower(): return 2 #Chose scissors

def winner(x,y): #winner function
    if x==y: #if same thing then draw...
        return "Draw" #draw text
    elif (x,y)==(0,1): return "Loss"#rockVpaper
    elif (x,y)==(0,2): return "Win"#rockVscissors
    elif (x,y)==(1,0): return "Win"#paperVrock
    elif (x,y)==(1,2): return "Loss"#paperVscissors
    elif (x,y)==(2,0): return "Loss"#scissorsVrock
    elif (x,y)==(2,1): return "Win"#scissorsVpaper
    elif (x)=="close": exit()#closed program
    else: #bug test print statement
        print("what\n\n") #broke

def countin():#display count
    try:
        print("Win Count: "+str(Count["Win"])+" ("+str(Count["Win"]/TotalCount*100)[:4]+"%)") #Win Count print statement
        print("Loss Count: "+str(Count["Loss"])+" ("+str(Count["Loss"]/TotalCount*100)[:4]+"%)") #Loss Count print statement
        print("Draw Count: "+str(Count["Draw"])+" ("+str(Count["Draw"]/TotalCount*100)[:4]+"%)") #Draw Count print statement
        print("Total Count: "+str(TotalCount)) #Total Count print statement
    except: #bug check
        print("You need to play at least once") #would give an error due to dividing by 0

print("Type \"Close\" to close the program\n")
print("Type \"Count\" to see your statistics")
while True: #forever while loop
    inp = input("Select \"Rock\" \"Paper\" or \"Scissors\"\n") #User input
    playerselect = selection() #selection
    botselect = random.randint(0, 2) #random integer between 0,1,2
    if inp.lower()=="close": exit() #close if close input
    elif inp.lower()=="count": countin() #count prints if count input
    else: #Decides winner else it prevents an error
        try:
            print("Player selected " + Choices[playerselect] + "\n" + "Bot selected " + Choices[botselect]) #player selected print statemnet
            x = winner(playerselect,botselect) #setting the variable of Win, Draw, or Loss by function winner with both variables plaerselect and bot select
            print(x) #printing the Win Draw or Loss variable
            TotalCount+=1 #Increasing total count by 1 for success
            if x=="Win": Count["Win"]+=1 #if win, win+1
            elif x=="Loss": Count["Loss"]+=1 #if loss, loss+1
            elif x=="Draw": Count["Draw"]+=1 #if draw, draw+1
            else: print("How'd you make it here?") #no idea how this could error out
        except: #anything other than exit, count, rock, paper, or scissors
            print("Please only use \"Rock\" \"Paper\" or \"Scissors\"\n") #print statement of error