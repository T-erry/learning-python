# slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

# name = "Terry Wachuka"

# first_name = name[:5]
# last_name = name[5:]
# funky_name = name[::3]
# reversed_name =name[::-1]

# print(reversed_name)
 # slice() function is used to create a slice object, which represents a range of indices that can be used to extract a portion of a sequence (such as a list, tuple, or string). 
# The general syntax for the slice() function is:

website1 = "http://google.com"
website2 = "http://wikipedia.com"
# Create a slice object
slice = slice(7,-4)
print(website1[slice])
print(website2[slice])
