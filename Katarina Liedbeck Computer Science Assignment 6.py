#Katarina Liedbeck Computer Science Assignment 6

#First we ask the user how many times per week they go to buy coffee from Starbucks
ammountOfCoffeePerWeek = int(input("How many times do you buy coffee from Starbucks in a week?"))
priceOfCoffee = []
total = 0

#Here we ask the user the prices for each trip to Starbucks
#By using append we add an element to a preexisting list, here we are adding it to the previous prices.
for i in range(0, ammountOfCoffeePerWeek):
    price = float(input(("How much did you spend on trip #{} at Starbucks?: ".format(i+1))))
    priceOfCoffee.append(price)
    total += priceOfCoffee[i]

#f strings are string which are expressions that are evaluated while the module runs, used a lot for float numbers.
#.2f specifies 2 digits after the decimal point, where "f" is used to help represent the floating point number.
#Here we add all the trips together to display the total money spent per week at Starbucks
print(f"The total amount of money you spend in a week is: {total:.2f}")

#Here we calculate the average price and then display it
#The command "len" is used to return the length of a string, here we are returning it to the amount of times we asked for the price.
averagePrice = total / len(priceOfCoffee)
print(f"The average amount of money you spend for coffee at Starbucks each week is: {averagePrice:.2f}")

#Here we calculate the total cost per month and then display it
totalPriceInAMonth = total * 4
print(f"The total amount of money you spend for coffee at Starbucks in a month is: {totalPriceInAMonth:.2f}")

#Here we calculate the total cost per year and then display it. 
totalPriceInAYear = total * 52
print(f"The total amount of money you spend for coffee at Starbucks in a year is: {totalPriceInAYear:.2f}")


                                   
