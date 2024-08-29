#Katarina Liedbeck ; Computer Science Program ; Assignment 19

#Here we define the function
def speed_check():

    #Here we prompt the user for the name, miles traveled, hours taken, speed limit
    #We also calculate the MPH
    name = input("What is your name?")
    milesTraveled = float(input("How many miles did you travel?"))
    hoursTaken = float(input("How many hours did it take to travel?"))
    speedLimit = int(input("What is the speed limit?"))
    mph = milesTraveled/hoursTaken
    print("you were travelling at", mph, "miles per hour")

    #Here we use if, elif and else to find out if the user will recieve a ticket or not. The first if, is for when the user is driving too slow.
    if mph <= (speedLimit-10):
        print("You are driving too slow, you are going atleast 10mph below the limit!")

    #Here we find out if the user is driving fast enough to recieve a ticket.
    elif mph >= (speedLimit+20):
             print("You are driving too fast, 20mph or more over the limit, you will recieve a ticket!")
             #Here we open a file with the file name of speeding ticket.txt
             fileName = name + " Speeding Ticket.txt"
             fileObject = open(fileName, "w+")
             #Here we create a list with 3 seperate strings 
             string1 = 'Dear ' + name + ','
             string2 = 'You have received a speeding ticket for driving at an average of ' + str(mph) + ' in an area with ' + str(speedLimit) + ' as a Speed Limit' + ','
             string3 = '-NYS' 
             ticketLanguage = [string1 , string2 , string3]
             #We use 'for' to ensure that the list will print out on each line and that it is in string format.
             for item in ticketLanguage:
                fileObject.writelines("%s\n" % item)
             #Here we make sure to read back the file and close it
             fileObject.seek(0)
             print(fileObject.read())
             fileObject.close()
    #Here we use elif to tell them they are driving too fast but not fast enough to recieve a ticket
    elif mph >= (speedLimit+10):
        print("You are driving too fast, you are going atleast 10mph over the limit!")
    #Here we use else for if they are not driving too slow nor too fast
    else:
        print("You are driving at a normal speed, keep it up!")
    
#Here we finally call the function to make it work.
speed_check()
