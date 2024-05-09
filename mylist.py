# change list item
# trick 1: append()
list = [1, 2, 3]
list.append("apple")
print(list[1])
print(list)

# trick 2: insert()
list.insert(4, "orrange")
print(list)

# delete or remove list item
#  method 1: remove()
firstList = ["apple", "tiger" "banana", "pineaple", "lichi", "mango"]
firstList.remove("apple")
print(firstList)

# meyhod 2: pop()
secondList = ["apple", "tiger" "banana", "pineaple", "lichi", "mango"]
secondList.pop(1)
print(secondList)

# method 3: del()
thirdList = ["apple", "tiger" "banana", "pineaple", "lichi", "mango"]
del thirdList[1]
print(thirdList)

# method 4: clear() that si remove all lists from the list
fourthList = ["apple", "tiger" "banana", "pineaple", "lichi", "mango"]
fourthList.clear()
print(fourthList)