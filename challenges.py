# Double Char 8 kyu
# Given a string, return a string in which each character (case-sensitive) is repeated once.
# Example double_char("String") == > "SSttrriinngg"
# Example double_char("Hello World") == > "HHeelllloo  WWoorrlldd"
# Example double_char("1234!_ ") == > "11223344!!__  "

def double_char(str):
    wow = map(lambda i: i+i, str)
    return ''.join(wow)

print(double_char("1234!_ "))

# Sum of positive 8 kyu
# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20


def positive_sum(arr):
    retval = [i for i in arr if i > 0]
    return sum(retval)

print(positive_sum([1, -4, 7, 12]))
# Minimum Steps 7 kyu
# Given an array of N integers, you have to find how many times you have to add up the smallest numbers in the array until their Sum becomes greater or equal to K.
# minimumSteps([1, 10, 12, 9, 2, 3], 6)  ==>  return 2
def minimum_steps(numbers, value):
    return 'Your Answer'
