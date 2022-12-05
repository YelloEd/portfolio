import string
def userinp(): #User input
    file = str(input("Enter the name of your text file ending with the file type extension\n")) #String input to reduce errors
    return(file) #REturns the user input


def createdicts(): #Creating the two dictionaries for the program
    count=0 #Line count
    counts=dict() #dictionary for word counter
    counta=dict() #dictionary for word line location
    for line in fhand: #searches line by line through the filehandle
        count+=1 #Increase line count by 1 for every line counted
        nline = line.translate(line.maketrans('','',string.punctuation)) #removes symbols
        nline = nline.strip() #removes newlines
        nline = nline.lower() #lowercases everything
        wordX = nline.split() #splits each word per line
        wordY = wordX #duplicates wordX as wordY
        for word in wordX: #checks every word in the line
            if word not in counts: #if the word isn't in word counter
                counts[word]=1 #word's count is 1
            else: #if the word is in word counter
                counts[word]+=1 #word's count is added by 1
        for theword in wordY: #checks every word in the line
            if theword not in counta: #if the word isn't in word line counter
                counta[theword]=count #word's count is the line number
            else: #if the word is in word line counter
                if str(counta[theword]).find(str(count))==-1: #checks if there is not a duplicate line number such as 2,2
                    counta[theword]=str(counta[theword])+", "+str(count) #the line number will have a comma with the added number
    return(counts,counta) #returns as both dictionaries

def common_word(): #Converts the dictionary of word counter to a list then lists it out in reverse order
    commonlist=list() #Creating the common list
    f.write("The 6 common words\n") # !writes in the file
    for k,v in list(dictionary[0].items()): #takes the first dictionary items (word counter)
        commonlist.append((v,k)) #creates it into a list with key-value pair
    commonlist.sort(reverse=True) #reverse order so it's highest number first (descending)
    for v,k in commonlist[:6]: #Takes the top 6 from this list in reverse key value pair due to previous output
        k=k+": " #Adds a colon and space to each key
        x=str(k)+str(v) #Creates a string variable of the key-value pair
        f.write(x+"\n") #!Write to file "words_index.txt"

def line_numbers(): #Converts the dictionary of line number count then lists it in alphabetical order
    linelist=list() #Creating the line number list
    f.write("\n\nWords and their line numbers in alphabetical order\n") #!writes in the file
    for k,v in list(dictionary[1].items()): #Takes the second dictionary items (line count)
        linelist.append((k,v)) #creates it into a list with key-value pair
    linelist.sort() #sorts alphabetically with key-value pair
    for k,v in linelist: #Takes the entire list in key-value pair
        k=k+": " #Adds a colon and space to every key
        x=str(k)+str(v) #Creates a string variable of the key-value pair
        f.write(x+"\n") #!Write to file "words_index.txt"

def main():
    print("Text File to be analyzed: "+str(file)) #Prints the file that is to be analyzed
    f.write("Text File to be analyzed: "+str(file)+"\n\n") #Writes the file that is to be analyzed
    common_word() #Begins common word sorting + write
    line_numbers() #Begins line number sorting + write
    print("File name, \"words_index.txt\" was created in the local directory")
    f.close() # Closed filehandle


print("This is a word analysis program")#Welcome message
x=True #Neeeded for while loop
while x==True: #Starting of while loop
    try: #Attempts to get user input
        file=userinp() #Calls function result
        fhand=open(file) #Opens the file handle
        x=False #Closes the loop
    except: #Failed
        print("This file does not exist") #More than likely due to incorrect file
f=open("words_index.txt","a") #Starts writing the file with append access; optimized for public use
dictionary = createdicts() #Creates the 2 dictionarys [0,1] 0 is the amount it showed, 1 is the line number for each word
main() # Main function is called
f.close() # Closed filehandle just incase a bug
