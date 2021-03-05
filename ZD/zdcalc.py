# name = input("Enter your name:")
input("Enter your name:")

print("\t Addition")
number1 = input("Enter number one:")
number2 = input("Enter number two:")
# cast the string into a integer
result = int(number1) + int(number2)
print(
    "When adding",
    int(number1),
    "+",
    int(number2),
    "the result is:",
)
print(result)
print("\t Multiplication")
number1 = input("Enter number one:")
number2 = input("Enter number two:")
number3 = input("Enter number three:")
result = int(number1) * int(number2) * int(number3)
print("When multiplying", int(number1), "x", int(number2), "x", int(number3),
      "the quotient is:")
print(result)
print("\t Division")
number1 = input("Enter number one:")
number2 = input("Enter number two:")
result = int(number1) / int(number2)
print("But when you divide", int(number1), "/", int(number2),
      "the resulting answer is:")
print(result)
