
#Tuples are an ordered sequence, written as comma-speerated elements within paarenteses.
Ratings = (10, 9, 6, 5, 10, 8, 9, 6, 2)
print(Ratings)
print(Ratings[0])
print(Ratings[-1])
Ratings = Ratings +(4,5,"Ryan")
print(Ratings)
#Tuples can contain other tuples as well.
NT = (1,2,("pop","rock"),(3,4))

#print an element in the tupple
print(NT[2])

#print an element in the nested tupple
print(NT[2][1])

#print the character (rember strings are a kind of tupple)
print(NT[2][1][0])
