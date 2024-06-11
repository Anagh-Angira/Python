def greet() :
    print("Hello Anagh")
    print("Danger")
greet()
print("Hello Aman")

def greetA(name, ending):
    print("Hello "+name)
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")
    print(ending)
print("Ending the Fuction")
greetA("Anagh", "Thankyou")
greetA("Abnav", "Thankyou")
print("Done")

def generator(name, date):
    st = f"Hello mam My name is {name} and i will not able to come school on {date}"
    print(st)

generator("Amit", "19-09-2002")
generator("Soham", "17-09-2002")

def average(a, b):
    return (a+b)/2

print(average(10,30))


# The Python pass statement is a null statement. But the difference between pass and comment is that comment is ignored by the interpreter whereas pass is not ignored. 

n = 5
for i in range(5):
    
    # pass can be used as placeholder
    # when code is to added later   
    pass
    print(i) 
    

def fun():
    pass

a = 10
b = 20
 
if(a<b):
  pass
else:
  print("b<a")