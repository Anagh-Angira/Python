l1 = [3,5,232,1,433,546,"abc"]
l1[0] = "Angira"
print(l1)
l1.insert(4,999)
print(l1)
print(type(l1))
print(l1)

# String is immutable => if it will created
# then value is not change. list are mutable
# it will not return the new list it will
# modify the same list as well
# Lists are mutable, and hence, they can be altered even after their creation.

l1.remove(1)
print(l1)
l1.remove("abc")
l1.sort() #sort the existing list
print(l1)
l1.count(234)
print(l1)

l1.append(1234)
print(l1)
l1.pop()
print(l1)

l1.extend([12,13,14,15,99])
print(l1)
print(l1.index(232))

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
#  7-3 = 3
print(List[-3])
#  7 - 5 = 2
print(List[-5]) 
print(len(List))

# Taking the List as a User Input

str = input("Enter element (Space-Separated)")
lst = str.split()
print('The List is ',lst)

my_lst = [1,2,3,4,5]
print(my_lst[0:3])
lst_rev = list(reversed(my_lst))
print(lst_rev)

lst.remove(4)
print(lst_rev)

List = ['G', 'E', 'E', 'K', 'S', 'F',
        'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List: ")
print(List)

Sliced_List = List[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List)

Sliced_List = List[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_List)

Sliced_List = List[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List)
