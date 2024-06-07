a1 = {3,5,5,63,23,2,3,63}
a2 = {3,5,63,666,7777,8888}

a3 = set() #creating the Empty Set
print(type(a3))

# a1.clear()

# list and set ->  we cannot access items using indexes as we do in lists.
# A Set in Python programming is an unordered collection 
# data type that is iterable, mutable and has no duplicate
# elements. 

print(a1.pop())
a1.add(44)
print(a1.union(a2))
print(a1.intersection(a2))
print(a1.issuperset(a2))
print(a1.issubset(a2))
print(a1)
print(a2)