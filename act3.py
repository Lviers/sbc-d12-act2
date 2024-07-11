#words tokenization

input  = input("Enter yo number and alpha: ")
stwing = ""
mylist = []

for x in input + " ":  
	if x.isalpha() or x.isalnum() :
		stwing += x
	else:
		mylist.append(stwing)
		stwing = ""
print(mylist)


