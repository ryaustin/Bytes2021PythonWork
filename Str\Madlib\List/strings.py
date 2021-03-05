#create a string
Name = "Ryan Austin"
print(Name)

#determine lengeth of string
print(len(Name))

#selects range within string
print(Name[0:4])

#multiples string
print(Name*3)

#starts a new line
new_line = "Ryan Austin \n 30"
print(new_line)

#creates a tab in the line
tab_line = "Ryan Austin \t 30"
print(tab_line)

#2 backslashes to producee one backslash
backslash_line = "Ryan Ausitn \\ 30"
print(backslash_line)

#uses r in front of the string
backslash_line2 = r"Ryan Austin \ 30"
print(backslash_line2)

#string methods

#converts lowercase to UPPERCASE
upper_name = Name.upper()
print(upper_name)

#replace a part of the string
replace_name = Name.replace('Ryan','Brian')
print(replace_name)

#find a substring, the argument is the substring you want to find. The output is the first character in the start of thee sequence. If it is not there output will be -1
print(Name.find('Au'))
print(Name.find('Bu'))