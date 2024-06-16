#Writing in a file
s = "Hello My Name is Anagh Angira"

with open("test.txt", "w") as f:
    f.write(s)
    
#Method-2 to write the data in file
fp = open("text1.txt","w")
fp.write(s)
fp.close()


#Reading a File
with open("test.txt", "r") as f:
    s = f.read()
    print(s)

#Second way to implement
f = open("text1.txt", "r")
f.read()
print(s)
f.close()
#Appending to a file

with open("text1.txt", "a") as fb:
    fb.write("Hello The Name is Anagh")