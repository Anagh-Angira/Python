for i in range(5): #Range Function starts from 0 to n-1
    print(i, end=' ')

print()
    
lst = [3,4,599,34,88,56,109]

for lst1 in lst:
    print(lst1, end=' ')
    
print()
s = {3,4,599,34,88,120}

for st in s:
    print(st, end=' ')
    
print() 
i = 0

while(i <= 5):
    print(i+1, end=' ')
    i = i + 1
print("Programme is Finished Executing")

while(True) :
    num = int(input("Enter the Number : "))
    
    if(num == 5):
        break
    else:
        print(num)

print("Programme Breaks")