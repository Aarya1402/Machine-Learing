name = "Aarya"  # strings are immutable
print(len(name))
print(name.upper())  # string will remain unchanged it will make a another copy which consist of upper string of name and that new string will be printed
print(name)
print(name.lower())
print(name)
name1 = "!!!aarya!!!"
# removes trailing character. it will not remove ! leading character
print(name1.rstrip("!"))
print(name.replace("Aarya", "jonh"))  # replaces all occurance of a string
# all aarya will be replaced with jonh
print(name)
name2 = "aarya anant tulsi"
print(name2.split(" "))  # converts string to list from specified character
heading = "introduction TO python"
# turns the first character to uppercase and remaining charcters to the lower case
print(heading.capitalize())
# alligns the string to the center as per the parameters(total characters to be printed)
print(heading.center(50))
print(len(heading))
# adds total-len(str) whitespaces at the begining
print(len(heading.center(50)))
print(name.count("Aarya"))  # counts frequency of aarya
print(name.count("a"))  # counts frequency of a
# checks whether sting ends with given string and returns boolean data type
print(heading.endswith("python"))
# checks whether sting ends with given string and returns boolean data type
print(heading.endswith("hon"))
# checks whether sting ends with given string and returns boolean data type
print(heading.endswith("p"))
print(heading.endswith("duction", 0, 12))  # endeith()+slicing
print(heading.startswith("intro"))  # same as endwith
# finds first occurance of the string and returns its starting value if not fund then returns -1
print(heading.find("TO"))
# finds first occurance of the string and returns its starting value if not fund then returns -1
print(heading.find("to"))
# print(heading.index("to"))#same as find but gives error if string not found
# check whether string consist of any character except alphabet and digit and returns boolean
print(name.isalnum())
print(heading.isalnum())  # flase as string consist whitespace
# checks whether string consist of any character except alphabet
print(name.isalpha())
# checks whether string consist of any character except digit
print(name.isdigit())
print(name1.islower())  # all characters must be on lowercase
name3 = "aarya\naastha"
print(name.isprintable())  # all characters must be printable
print(name3.isprintable())  # here '\n' is not printable
# returns true if string consist all characters as whitespace, otherwise false
print(heading.isspace())
space = "      "
print(space.isspace())
print(heading.istitle())  # returns true if all words are capitalized
print(heading.title())  # capitalizes all words
print(heading.swapcase())  # lower to upper and upper to lower
