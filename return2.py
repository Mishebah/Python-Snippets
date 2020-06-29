"""A function returning a string and using a local variable
Come back and differenciate + and comma(,) when insertted at the result variable"""


def lastFirst(firstName, lastName):
    separator = ', '
    result = lastName + separator + firstName
    return result


print(lastFirst('Benjamin', 'Franklin'))
print(lastFirst('Andrew', 'Harrington'))
