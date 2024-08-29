#Katarina Liedbeck ; Computer Science Program ; Assignment 18

#First we define and create the function - and we give it the two parameters
def file_create(file_name, message):

# Here we open the file and use 'w+' to ensure we can write and read the file 
    fileObject = open(file_name, "w+")

#Here we use the '.write' to wrte the message in the file
    fileObject.write(message)

#Here we use the '.seek(0)' to read from the beginning of the file 
    fileObject.seek(0)

#Here we use the print fileObject.read to read the file and print it back in the shell.
    print(fileObject.read())

#Here we must remember to close the file.
    fileObject.close()


#We finally finish by calling the function, and adding in our own parameters.
file_create("confession.txt", "Computer science turned out to be more fun than what I thought it was going to be :)")
