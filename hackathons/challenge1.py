"""Exercise 1 (and Solution)
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
# # Variables cannot start with numbers.
# # create a variable to store name 
name = input("Enter YOUR name:")
age = int(input("Enter your age:"))

# # create a new var to store 100 minus the users age.
birthday_100= 100 - age # how much years you have until you turn 100 

# # create a new variable to add Birthday_100 variable to the current year.
fortune_teller= birthday_100 + 2021


# # print a nicely formated output to the user telling them what year they will be 100.
message = "Hey",name,"you will be 100 in",fortune_teller
print(message)

# # Great work, now extend your program:  Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)

# #ask the person to give you another number.
print("Now I need you to give me another age, please. :) ") #have to be nice 

# # Create a new variable to store \ another number 
repeat_message = int(input("Enter a random number:")) #no errors 



# #you would like to right it in a for loop?
# #print(" repeat_message \n" * 100)
# #

# #Use range(stop) to create a range of 0 to stop where stop is the number of lines desired. Use a for-loop to iterate through this range. In each iteration, concatenate the string to itself by the number of times desired and print the result.

# print(message * repeat_message) 

# #3.  Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

class_attendees = "Caleb, Nora & Zarian"

print (4 * "")

for x in range(0, repeat_message):
   print(message)

records=["Legend","Big Time Rush","Splash FM","Fine Line","Abbey Road","xyz"]

records.append("Recking Ball")
print(records.index("Big Time Rush"))
for record in records:
  print(".",record)

# writing pass in the body of a for loop or if test allows you to skip completion of that code until later. Otherwise if you don't compleete the code you will get an error when trying to test.

# here is an alternate way
for record in records:
  print('{0}. {1}'.format(records.index(record),record))






