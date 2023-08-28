name = "aarya,aastha"
print(name[0:5])  # prints from 0 to n-1(here, it is 4)
fruit = "mango"
l = len(fruit)  # length of the string
print("Mango is a ", l, "character word")
print(fruit[0:4])  # slicing of the string
print(fruit[:4])  # if you don't specify starting index, default will be zero
print(fruit[1:4])  # We can slice from any where
print(fruit[0:-3])  # Nagetive slicing
print(fruit[0:len(fruit)-3])  # Equivalent to line 9
# 5-1:5-3 -->4:2 doesn't make any sense and null string will be printed
print(fruit[-1:len(fruit)-3])
print(fruit[-3:-1])  # 5-3:5-1 -->2:4 It will print index 2 and 3


# quiz
nm = "Harry"
print(nm[-4:-2])  # 1:3
