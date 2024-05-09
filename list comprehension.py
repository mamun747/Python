numbers = [10, 20, 30, 40, 50, 60]
# for i in numbers:
#     print(i * 2)

double = [i * 2 for i in numbers]
print(double)

# copy a list
nums = [10, 20, 30, 40, 50, 60]
num = nums.copy()
print(num)

# join two list
extend = ["a", "b", "c", "d"]
extends = [1, 2, 3, 4, 5]
extend.extend(extends)
print(extend)

# sorting a list
# it works at alphabetically
list = [1, 2, 4, 10, 5, 8, 9, 0]
list.sort()
print(list)

# reverse list
alpha = ["b", "d", "a", "f", "e", "o"]
alpha.reverse()
print(alpha)

alpha1 = ["b", "d", "a", "f", "e", "o"]
alpha1.sort(reverse = True)