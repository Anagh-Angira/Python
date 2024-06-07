# Introduction on f-string and doc string in python

# f-strings
letter = "Hello my name is {} and I am from {}"
name = "Anagh"
country = "India"
print(letter.format(name, country))
print(letter.format(country, name))


print(f"Hello my name is {name} and I am from {country}")
print(f"Hello my name is {{name}} and I am from {{country}}")

txt = "For only {price: .2f} dollars!"
print(txt.format(price = 47.0999)) #take only two value of decimal

price = 5464.904
print(f"For only {price: .2f} dollar")
print(type(f"{2 * 30}")) #output as a string


#Doc-Strings in Python PEP-8
def square(n) :
    '''Takes in a number n, returns the square of n'''
    print(n ** 2)
square(5)
print(square.__doc__) #print the docstrings not a comments


# Here the docstring cannot be printed because docstring is immediate after line come next to 
# the function declaration here docstring is not printed output None.
def square1(m) :
    print(m)
    '''Takes in a number m, returns the square of m'''
    print(m ** 3)
square1(3)
print(square1.__doc__)


# PEP-8 python Enhancement proposal how to write good maintainable code in python 

#Taking user input
# name = input("Enter name : ")
# print(name)

i = int(input("Enter Number i : "))
print(i+12)
b = bool(input("Enter the Bool value : "))
print(b)

name = input("Enter the Name : ")
print(name)

a1 = "anagh"
a2 = 'anagh'
# Multiline String
a3 = '''anagh is a good boy
he is from Ranchi 
and goes to destination early'''
print(type(a3))
print(a1, a2, a3)
    

