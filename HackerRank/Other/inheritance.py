
# class Person:
# 	def __init__(self, firstName, lastName, idNumber):
# 		self.firstName = firstName
# 		self.lastName = lastName
# 		self.idNumber = idNumber
# 	def printPerson(self):
# 		print("Name:", self.lastName + ",", self.firstName)
# 		print("ID:", self.idNumber)

# class Student(Person):
#     def __init__(self, firstName, lastName, id, scores):
#         id 
        


#     #   
#     #   Parameters:
#     #   firstName - A string denoting the Person's first name.
#     #   lastName - A string denoting the Person's last name.
#     #   id - An integer denoting the Person's ID number.
#     #   scores - An array of integers denoting the Person's test scores.
#     #
#     # Write your constructor here
    

#     #   Function Name: calculate
#     #   Return: A character denoting the grade.
#     #
#     # Write your function here

# line = input().split()



















class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.testScores = scores
		
    def calculate(self):
        average = 0
        for i in self.testScores:
            average += i

        average = average / len(self.testScores)
		
        if(average >= 90):
            return 'O' # Outstanding
        elif(average >= 80):
            return 'E' # Exceeds Expectations
        elif(average >= 70):
            return 'A' # Acceptable
        elif(average >= 55):
            return 'P' # Poor
        elif(average >= 40):
            return 'D' # Dreadful
        else:
            return 'T' # Troll