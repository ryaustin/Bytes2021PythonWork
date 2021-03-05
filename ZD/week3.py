#this is the way a variable should look.
name= "Zarian Dean"

namae = 'Zarian Dean' # this is a bad variable if you were refrering to the variable(name).
age= 42
'''
When you use a function in python, each function is followed by () brackets.
example print(), len(), etc.
'''
grades = ['A','A','B','C','B','B','b']

# to add to a list create a new variable and use the __add__ method. RA
more_grades = grades.__add__(['D','E',"A","B"])
print(more_grades)
print("length:", len(grades))

for grade in grades:
  print(grade)  

languages = ['python','java','c++']
for language in languages :
  print(language)

print('------')
# for(for loop)
# ! means is not
# ex. for grade in, includes the f=grades within the variable.
# iteration means to loop over a collection.
for grade in grades:
  if grade != 'B':
    print(grade)

for letter in "python":
  if letter == "p":
    print("you got a p")
  else:
    print('incorrect guess')


'''
Operator	Meaning	Example

>	Greater than - True if left operand is greater than the right	x > y

<	Less than - True if left operand is less than the right	x < y

==	Equal to - True if both operands are equal	x == y

!=	Not equal to - True if operands are not equal	x != y

>=	Greater than or equal to - True if left operand is greater than or equal to the right	x >= y

<=	Less than or equal to - True if left operand is less than or equal to the right	x <= y
'''