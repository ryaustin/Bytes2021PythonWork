'''
MAD LIBS is one of the world’s fun word games. Some would even call it one of the ‘GREATEST WORD GAME”. If you enjoy playing around with words, then you probably agree with this phrase.
MadLibs is a phrasal template word game where one player prompts others for a list of words to substitute for blanks in a story/poem/rhyme before reading aloud. The game is frequently played as a party game or as a pastime(Wikipedia).
'''

'''
For this madlib we are going to import our words from a dictionary or list. So, we will create a list in python, then we will pull words from the list to create our madlib.
'''
school_students=["Religious","James","Zane","Zarian","Caleb","Max","John","Queen","Jackey","Aba"]
list_length= len(school_students) -1
print("The amount of students",list_length)
      #Generating random number list in Python 
#import random n = or random. or random() or print(n)
#import random randomlist = [] for i in range(0,5): n = random. randint(1,30) randomlist.
import random
randomInt = random.randint(0,list_length)
print(" The random num is",randomInt)

print("-------------THE ULTIMATE MADLIB VER. 1.0-------------------")
print("Today at school, I saw",school_students[randomInt])
print("Yesterday I saw ",school_students[-1])
print("I wish I also saw,",school_students[1:6])
print("Today was a good day",'I love the activities presented before me.')
print('I wish I also saw ',school_students[2:randomInt])
print("------------delete example--------------------")
del school_students[2]
print(school_students)


print("-------------count example-------------------")
james_count = school_students.count("James")
print("We found a total of", james_count, "James")

print("--------------extend example------------------")
#You can use () or {} or [] to include lists or strings.
new_school_students = ("Johnny","Bryan","Jannette")
school_students.extend(new_school_students)
randomInt = random.randint(0,list_length)
print(school_students)
print("Today at school, I saw",school_students[randomInt])
print("----------------END----------------")

# # vowels list
# vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# # count element 'i'
# count = vowels.count('i')

# # print count
# print('The count of i is:', count)

# # count element 'p'
# count = vowels.count('p')

# # print count
# print('The count of p is:', count)
# 
# languages list
languages = ['French', 'English']

# another list of language
languages1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
languages.extend(languages1)

# print('Languages List:', languages)