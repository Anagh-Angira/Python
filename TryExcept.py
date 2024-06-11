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