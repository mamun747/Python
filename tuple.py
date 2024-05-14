# Checking the tlype of data
a = ("Mango", "Kiwi", "Jack-Fruit", "Watermelon", "Lichi")
print(type(a))

# Charactersticks of Tuple data type
# Tuple is immutable 

# Updating data of Tuple Data Type
b = ("Mango", "Kiwi", "Jack-Fruit", "Watermelon", "Lichi")
c = list(b)
# Checking the tlype of data
print(type(c))
# changing it
c.append("Banana")
# converting in tuple
d = tuple(c)
print(c)

# Tuple unpack data type

fruits = ("Mango", "Kiwi", "Orange", "Watermelon", "Lichi")
(a, d, o, w, l) = fruits
print(d)

fruits1 = ("Mango", "Kiwi", "Orange", "Watermelon", "Lichi")
(*m, d, w, o) = fruits1
print(m)