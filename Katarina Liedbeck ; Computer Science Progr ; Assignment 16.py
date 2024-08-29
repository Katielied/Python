#Katarina Liedbeck, Computer Scie Program ; Assignment 16 ;


#Here we define the file name as "input.txt" so that it will work in both the try and except blocks;
fileName="input.txt"

#Within the try block we have written our coding
try:
    #Here we are opening the file which exists ("input.txt") And using w+ in order to both read and write it.
    fileObject = open(fileName, "w+")
    #Here we define plansForWeekend as the user input which they type
    plansForWeekend = input("What are your plans this weekend?")

    #Here we use ".write" to allow the user to write into the file 
    fileObject.write(plansForWeekend)

    #.seek is used to find and read the user input in the file starting from character 0 in the string.
    fileObject.seek(0)

    #Here we print what we have written/read in the file
    print(fileObject.read())

    #Here we close the file 
    fileObject.close()
    
#Here we write the except which is incase the file is not found 
except FileNotFoundError:
    #If the file is not found, we will print "input.txt" was not found
    print("The file ", fileName, " was not found")
