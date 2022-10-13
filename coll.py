# There are four collections
# list
# tuples
# set
# dictionary
# list - collection of ordered and changeable


thislist = ["apples", "bananas", "cherry", 2, 1, 2, 4]
print(len(thislist))

if 2 in thislist:
    print("Yes")

thislist[4] = True

thislist.insert(2, "melons")
thislist.append("Mangoes")
thislist.remove(4)

print(thislist)

for listItem in thislist:
    print(listItem)

# Tuples - Ordered and unchangeable
thisTuple = ("cows", "goats", "sheep")
print(type(thisTuple))


# Sets - Unordered and unchangeable
thisSet = {"cows", "goats", "sheep"}
print(type(thisSet))

# Dictionary - Ordered and changeable, key:value pairs

thisDict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1964
}

print(type(thisDict))
print(thisDict)