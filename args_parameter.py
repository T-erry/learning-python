# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amoutn of arguments


def add(*num):
    sum = 0
    for i in num:
        sum += i
    print(sum)

add(3, 5)
add(4, 5, 6, 7)
add(1, 2, 3, 5, 6)
