n = "Marry"
print(n)

name = 'Harry'
name1 = 'harry'
print(name[0 : 3]) # 0 to 3 slice
# print(name[a : b])  start from a goes to b-1

print(name[1:4])
print(name.upper())
print(name1.capitalize()) #capatilize 1 charecter only

print(name.count("H"))
print(name.count("a"))
print(name.count("Y"))

print(name.isalnum()) #alfabet + numeric

number = "7"
print(number.isnumeric())
print(name.isnumeric())

String1 = "GeeksForGeeks"
print("Initial String ", String1)
# print(String1[-3])
print(String1[-5])


string = "IamAnaghAngira"
print(string[-6])
print(string[2:9])
print(string[3 : -2])
# print(string[ : : -1]) Reverse the String

string = "".join(reversed(string))
print(string)

string2 = "Hello I'm a Geek"
print("Initial String")
print(string2)
# Deleting a character

print("Deleting the charecter from 2nd index")
# del string2[-2] Type Error
# print(string2)

print("Deleting the Entire String")
del String1
print("hello World")
print(string2)

