# dictionary = A changeable, unordered collection of unique key:value pairs
            # Fast because they use hashing, allow us to access a value quickly


capitals={"Kenya": "Nairobi", "USA": "Washington DC", "India": "New Dehli" , "China": "Beijing", "Russsia": "Moscow"}

#Updates the dictionary with the elements from another dictionary

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Las Vegas"})

# Returns and removes the element with the given key
# capitals.pop("China")

# Removes all items from the dictionary
# capitals.clear()

# print(capitals["India"])

#Returns the value for the given key
# print(capitals.get("Germany"))

#Returns a view object that displays a list of all the keys in the dictionary
#print(capitals.keys())

#Returns a list of all the values available in a given dictionary
#print(capitals.values())

#Return the list with all dictionary keys with values
# print(capitals.items())

# for key, value in capitals.items():
#    print(key, value)