#to be updated

print("Dictionaries examples-->\n")
print("An unordered set of key: value pairs where keys are unique\n")

print("dict1={'one':1,'two':2,'three':3}  -->")
dict1={'one':1,'two':2,"three":3}
print("dict1 contents -->", dict1)
print("\ndict1['two']")
print(dict1['two'])

#deleting a key value pair
print("deleting a key value pair\n")
print("del dict1['three']-->")
del dict1['three']
print("\n",dict1)

#Listing keys only from a dictionary
print("\nListing keys only from a dictionary\n")
print("dict1.keys()-->\n",dict1.keys())

#sorting keys in dictionary
print("\nsorting keys in dictionary\n")
print("sorted(dict1.keys())-->\n",sorted(dict1.keys()))

#validate existence of the key
print("\nvalidate existence of the key\n")
print("'one' in dict1-->\n",'one' in dict1)
print("\n'nothing' in dict1-->\n",'nothing' in dict1)

