# create a list of student names and iterate over the list pringing all the names.

# for loop and if statement example
for grade in ['A','B','C']:
  if grade != 'B':
    print(grade)

students= ['Max','Jackey','Phillip','Zarian','Religious']
for student in students:
  print('.',student)

# create a counter variable that increases by 1 each time the for loop runs. Do some concatenation to add the counter to the beginning of the student name when it prints.
# range includes the number stated up to the number needed (1,100) gives you 1,99 and not 100 because it excludes the last digit.
counter= 1
for student in range(1,11):
  print(counter,'.',student)
  counter = counter +1

numbers = [1, 2, 3, 4, -4, 8, -2, 7, -1]

print(1 > 0)

# using what you know now about for loops, WAP (write a program) that only prints a number if it is a positive number.
# clue: you need a for loop. and you need to use a if statement.
for number in numbers:
  if number < 0:
    print(number)
# in statements like (if number < 0:) number already holds a value/variabe so you would only need to add the number that its going to.

# create a list to store the animals you find around Harbour Island. WAP to iterate over the list, only printing types of animals with names longer than or equal to 5 characters. Rember the len() built-in function checks the length of a collection. Look at the clue below:
animal = 'gorilla'
longer_than_3 = len(animal)
print(longer_than_3)

# print(*numbers,sep=' ') use this when you dont want to see the brackets in the code.
print(*numbers,sep=' ')
briland_animals= ['Chickens','Dogs','Cats','Snakes','Birds']
for animal in briland_animals:
  if len(animal)>= 5:
    print(animal)

animal = 'gorilla'
longer_than_3 = len(animal)
print(longer_than_3)
for letters in 'gorilla':
  if letters == 3:
    print(letters)

