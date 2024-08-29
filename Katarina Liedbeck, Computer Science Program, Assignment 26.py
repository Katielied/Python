#Katarina Liedbeck ; Computer Science Program ; Assignment 26

#First we state the class
class Dog:

    #Constructor Method
    #Here we stste the different intiations, remembering to state the self
    def __init__(self, name, age, gender, breed, color):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.color = color

#Here we define self as a string
    def __str__(self):
        return 'Name: {}\nAge: {}\nGender: {}\nBreed: {}\nColor: {}'.format(self.name, self.age, self.gender, self.breed, self.color)

#Here we define the function which returns the age into human years.
#We must make sure to turn self.age into and integer, and multiply it by 7 to convert it into human years.
    def human_years(self):
        return int(self.age)*7

#Here we state what s1 of the dog is, and we state all of the different attributes.      
d1 = Dog("Loki", "2", "Male", "Dalmatian", "Black and White")


#Finally we print d1 and the d1.human years function
print(d1)
print("The dog's age in Human Years would be:" , d1.human_years())

