#Katarina Liedbeck ; Computer Sci Progr<am ; Assignment 25


#First we name the function and give it the parameter "limit"
def mult_table(limit):
    #We state that it starts at 1 and runs through the input + 1 for both columns and rows.
    for columns in range(1, limit + 1):
        for rows in range(1,limit + 1):
            #We print the columns multiplied by the rows to create the multiplication table, and we add "end="\t"" in order to keep it on the same line with a tab in between
            print(columns*rows, end="\t")
        #Here we use print to print an extra space between each column
        print()
        #Here we use print to print an empty space in between each row
        print(" ")

        
 
#Here we make sure to define the parameter, which is the user input of how big they would like the table. We use "\n" to let the user give their input on the next line.
limit = int(input("How big would you want your multiplication table? Please choose a positive integer:" "\n"))
#We print an exmpty space before calling the function so that it prints on the next line with a space.
print()
#We print a brief description of how big their desired table is.
print("Your multiplication table runs 1 through", limit, ":")
#We print 2 exmpty spaces before calling the function so that it prints on the next line with a space.
print()
print()
#Finally we call the function with the parameter to let it run.
mult_table(limit)







