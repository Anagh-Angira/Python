try:
    num = int(input("Enter the Number : "))
    print(num)
    print("Hii")
    
except:
    print("Some Error Occuerd")

print("Hello")

try:
    f = float(input("Enter the Float Value : "))
    print(f)
    print("Hello")
    
except Exception as e:
    print("Some Error Occuerd ", e)

print("Hello")

x = 5
y = "hello"
try:
    z = x + y

except TypeError:
    print("Error cannot add an int to str")
    

a = [1,2,3]
try:
    print("Second Element = %d" %(a[1]))
    print("Second Element = %d" %(a[2]))

except:
    print("An Error Occurred")
    

def fun(a):
    if a < 4:
        
        b = a/(a - 3)
    print("Value of b = ", b) 

try: 
    fun(3)
    fun(5)

except ZeroDivisionError:
    print("ZeroDivisionError Occured and Handled")

except NameError :
    print("Name Error Occured and Handled") 
    
    
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)   