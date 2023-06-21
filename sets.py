# Sets are used to store items in a single variable
# they are unchangeable but items can be removed or added

set1 = {"rice", "Matooke", "Irish"}
print(set1)

# Duplicates in sets
set2 = {"rice", "Matooke", "rice"}
print(set2)

''' Exercise:
find the length of a set
find the data type of the set
Accessing items in the set
Adding items in the set
Adding two sets together 
'''
# Length of a set
print(len(set1), " this is the length of the set")

# Datatypes of the set
print(type(set1), " this is the datatype of the set")

# Accessing items in the set
for item in set1:
    print(item)

# Adding items in the set
set1.add("chapat")
print(set1)

# Adding two sets together
set1.update(set2)
print(set1)

# Also this works well when updating the set
set3 = set1.union(set2)
print(set3)
