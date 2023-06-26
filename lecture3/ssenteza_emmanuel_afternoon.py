# # Assignment for the afternoon session

# Individual Assignment
# Exercise1 (Lists)
# 1. Create a list with 5 items (names of people) and write a python program to output the 2nd
# item.
myList = ["Emma", "John", "Joan", "Peter", "Derrick"]
print(myList[1])

# 2. Write a python program to change the value of the first item to a new value
myList[0] = "Emmanuel"

# 3. Write a python program to add a sixth item to the list
myList.append("Zahara")
# 4. Write a python program to add “Bathel” as the 3rd item in your list
myList.insert(2, "Bathel")
# 5. Write a python program to remove the 4th item from the list
del myList[3]
# 6. Use negative indexing to print the last item in your list
print(myList[-1])

# 7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
newList = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig", "Grapes"]
print(newList[2:5])
# 8. Write a list of countries and make a copy of it.
countries = ["USA", "Canada", "France", "Germany", "Japan"]
countries_copy = countries.copy()

# 9. Write a python program to loop through the list of countries
for country in countries:
    print(country)


# 10. Write a list of animal names and sort them in both descending and ascending order.
animal_names = ["Lion", "Tiger", "Elephant", "Giraffe", "Monkey"]
animal_names.sort()  # Ascending order
print(animal_names)

animal_names.sort(reverse=True)  # Descending order
print(animal_names)


# 11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them
for name in animal_names:
    if 'a' in name.lower():
        print(name)

# 12. Write two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ["John", "Emma", "Michael"]
last_names = ["Smith", "Johnson", "Williams"]
full_names = first_names + last_names
print(full_names)

# Exercise2 (Tuples)

# 1. Consider the tuple below;
# x = (“samsung”, “iphone”, “tecno”, “redmi”)
# Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
favorite_phone_brand = x[1]
print(favorite_phone_brand)

# 2. Use negative indexing to print the 2nd last item in your tuple.
print(x[-2])

# 3. Using the phones list above, write a python program to update “iphone” to “itel”
updated_tuple = list(x)
updated_tuple[1] = "itel"
x = tuple(updated_tuple)
print(x)

# 4. Write a python program to add “Huawei” to your tuple.
x = x + ("Huawei",)
print(x)

# 5. Write a python program to loop through the tuple above.
for item in x:
    print(item)

# 6. Write a python program to remove/delete the first item in your tuple.
x = x[1:]
print("the first item is removed here")
print(x)

# 7. Using the tuple() constructor, create a tuple of the cities in Uganda.
uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Gulu"])
print(uganda_cities)

# 8. Write a python program to unpack your tuple.
(a, b, c, d) = x
print(a, b, c, d)

# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
print(uganda_cities[1:4])

# 10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("John", "Emma", "Michael")
last_names = ("Smith", "Johnson", "Williams")
full_names = first_names + last_names
print(full_names)

# 11. Create a tuple of colors and multiply it by 3.
colors = ("red", "blue", "green")
multiplied_colors = colors * 3
print(multiplied_colors)

# 12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print(count_8)


# Exercise3 (Sets)

# 1. Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["coffee", "tea", "juice"])

# 2. Use the correct method to add 2 more items to the beverages set.
# beverages.add("water")

items_to_add = ["soda", "milk"]
beverages.update(items_to_add)
print(beverages)

# 3. Given the set below;
mySet = {"oven", "kettle", "microwave", "refrigerator"}
# Check if "microwave" is present in the set.
if ("microwave" in mySet):
    print("Microwave already present")
else:
    print("Microwave not present")

# 4. Write a python program to remove "kettle" from the set above.
mySet.remove("kettle")
print(mySet)

# 5. Write a python program to loop through the set above.
for item in mySet:
    print(item)

# 6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
set1 = {1, 2, 3, 4}
list1 = [5, 6]
set1.update(list1)
print(set1)

# 7. Write two sets, one containing your ages and the other your first names. Join the two sets.
ages = {25, 30, 35}
first_names = {"John", "Emma", "Michael"}
combined_set = ages.union(first_names)
print(combined_set)

# Exercise4 (Strings)

# 1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
num = 10
string = "The number is " + str(num)
print(string)

# 2. Consider the example below;
txt = " Hello, Uganda! "
# Output the string without spaces at the beginning, in the middle and at the end.
txt = txt.strip()
print(txt)

# 3. Write a python program to convert the value of 'txt' to uppercase.
txt = txt.upper()
print(txt)

# 4. Write a python program to replace character 'U' with 'V' in the string above.
txt = txt.replace("U", "V")
print(txt)

# 5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd, and 4th position.
y = "I am proudly Ugandan"
print(y[1:4])

# 6. The piece of code below will give an error when output;
# x = "All "Data Scientists" are cool!"
# Write a python program to correct it.
x = 'All "Data Scientists" are cool!'
print(x)

# Exercise5 (Dictionaries)

# 1. With reference to the dictionary below, write a python program to print the value of the shoe size.
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])

# 2. Write a python program to change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"

# 3. Write a python program to add a key/value pair "type": "sneakers" to the dictionary.
Shoes["type"] = "sneakers"

# 4. Write a python program to return a list of all the keys in the dictionary above.
keys_list = list(Shoes.keys())
print(keys_list)

# 5. Write a python program to return a list of all the values in the dictionary above.
values_list = list(Shoes.values())
print(values_list)

# 6. Check if the key "size" exists in the dictionary above.
if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")

# 7. Write a python program to loop through the dictionary above.
for key, value in Shoes.items():
    print(key, value)

# 8. Write a python program to remove "color" from the dictionary.
del Shoes["color"]

# 9. Write a python program to empty the dictionary above.
Shoes.clear()

# 10. Write a dictionary of your choice and make a copy of it.
myDictionary = {"name": "John", "age": 25}
copyDictionary = myDictionary.copy()

# 11. Write a python program to show nested dictionaries.
nestedDictionary = {
    "person1": {"name": "John", "age": 25},
    "person2": {"name": "Emma", "age": 30}
}
print(nestedDictionary)
