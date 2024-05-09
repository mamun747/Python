# int type data
hablu = 420
print(hablu)
print(type (hablu))

# floating type data
gablu = 40.2
print(type (gablu))

# complex type data
kodu = 420j
print(type (kodu))

# str type data
Yourname = "mamun"
print(Yourname)

myName = "Mamun"
print(Yourname + myName)

print("my name is " + myName)

# bool data type
bool = True
print(type (bool))

num1 = 20
num2 = 50
print(f"this is my super number {num1 + num2}")

name = "mamun"
roll = 14
print(f"my name is {name} $ my class roll is {roll}")


nam = "Mutasir"
number1 = 10
print(f"My name is  {nam} and my class role is {number1}")

age = 18
print(f"I am {age} years old")

# PYTHON CONDITIONAL STATEMENT
if age >= 18:
    print("you are perfect to driving")
else:
    print("thats not a right discition")    


# PYTHON FUNCTION
def firstTime(x, y):
    return x * y

result = firstTime(3, 4)
print(result)

# BINARY TYPE DATA BYTE
byte = [1, 4, 121, 255]
# bytes minimum range is 0 - 256
b = bytes(byte)
print(type(b))

# byte is immutable
# b[0] = 10

# BINARY TYPE DATA BYTEARRAY
bytearr = [1, 4, 121, 255]
# byte minimum range is 0 - 256
b2 = bytearray(bytearr)
print(type(b2))

# bytearray is mutable
b2[0] = 100
print(b2[0])

# none type data
x = None
print(type(x))

# list(JavaScript array) type data
# List is mutable
listType = ["potato", "garlic", "Tomato", "Cucumber", "carrot", "Fish", "Chicken"]
print(listType)

# tuple type data
# Tuple is immutable
tupleType = ("potato", "garlic", "Tomato", "Cucumber", "carrot", "Fish", "Chicken")
print(tupleType)

# range type data
rangeType = (6)
rangeData = range(6)
print(rangeData)

for i in rangeData:
    print(i)

name = "mamun"
name += " is my name"
print(name) 

name1 = "mamun";
age = 14;
passion = "the codeexpert on front-end development and the code master"
life = "royal";
hobby = "billionaire"

print(f"my name is {name1} my age is {age} and i am {passion} i wish my life is {life} and my hobby i will make me a {hobby} in 2024 - 2030 thats my target")