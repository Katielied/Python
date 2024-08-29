#Katarina Liedbeck ; Computer Science Program ; Assignment 27

class Course:

    #Constructor Method:
    def __init__(self, ID, Name, Professor, Seats, Seatsleft):
        self.ID = ID
        self.Name = Name
        self.Professor = Professor
        self.Seats = Seats
        self.Seatsleft = Seatsleft

#Here we create a function in order to return it as a string
    def __str__(self):
        return('Course ID: {}\nCourse Name: {}\nProfessor Name: {}\nTotal Seats: {}\nTotal Seats Left:{}\n'.format(self.ID, self.Name, self.Professor, self.Seats, self.Seatsleft))

#Here we create a function in order to determine wether the class is full or not
    def classFull(self):
        if self.Seatsleft > 0:
            return "There are seats left"
        else:
            return "The class is full"

#Here we state the different class ids, course names, professors, seats and seats left
c1 = Course("0952-110-013", "First Year Seminar: Race,Class,Gender and Justice", "Anna Zinko", 25, 0)
c2 = Course("0145-190-004", "Computer Science Orientation Seminar", "Kees Leune", 30, 4)
c3 = Course("0122-107-020", "Art & Craft of Writing", "Michelle Bermudez", 25, 0)
c4 = Course("0145-171-003" , "Introduction to Computer Programming (Lecture)", "Liam Owens", 30, 2)
c5 = Course("0145-171-030", "Introduction to Computer Programming (Lab)", "Liam Owens", 30, 4)
c6 = Course("0501-101-008", "General Psychology", "Jessica Gruenstein", 40, 8)


#Finally we print the courses, along with the function on wether or not the class is full. We do not have to print it, as it already returns it, however I have chosen to print it.
print(c1.classFull())

print(c1)

print(c2.classFull())

print(c2)

print(c3.classFull())   

print(c3)

print(c4.classFull())             

print(c4)

print(c5.classFull())           

print(c5)

print(c6.classFull())

print(c6)





    
