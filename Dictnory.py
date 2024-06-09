dict1 = {}
print(dict1, type(dict1))

dict2 = {"aman":1, "soham":3, "ram":4,
         "arav": 5, "sammer":10
        }
print(dict2)
print(dict2["aman"])
marks = {"Azhar": 34, "Harry": 54, "Ranveer": 64,
         "Rohan": 88, "Sankalp": 77, "Sonia":88
        }
print(marks["Rohan"])

#Dictionary is mutable we can change
# A Python dictionary is a data structure that stores the value in key:value pairs.
marks["Priyanka"] = 90
print(marks)
marks.pop()
print(marks.get("Priyanka Chopra")) #None
print(marks.get("Priyanka")) #.get method help error free priyanka chopra 
# will give error

# print(marks["Priyanka Chopra"]) give error
print(marks.keys())
print(marks.values())
print(marks.items())

dict2 = {
        'Dict1' : {1: 'Geeks'},
        'Dict2' : {'Name': 'For'}
}
print(dict2['Dict1']) 
print(dict2['Dict1'][1])
print(dict2['Dict1']['Name'])

dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"} 
dict2 = dict1.copy() 
print(dict2) 
dict1.clear() 
print(dict1) 
print(dict2.get(1)) 
print(dict2.items()) 
print(dict2.keys()) 
dict2.pop(4) 
print(dict2) 
dict2.popitem() 
print(dict2) 
dict2.update({3: "Scala"}) 
print(dict2) 
print(dict2.values()) 
