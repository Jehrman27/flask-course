# Function Tasks
#
#
# Let's see if you can solve these word problems by creating functions.
# The function "skeleton" has been set up for you to fill in below the problem
# description, as well as example outputs of what the function should return
# given certain inputs. Best of luck, some of these will be challenging!
#
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
#
#  Create a function that takes in two integers and returns
# a Boolean True if their sum is 10, False if their sum is something else.

def check_ten(n1, n2):
    if (n1 + n2 == 10):
        return True
    else:
        return False


print("4 + 6 ", check_ten(4, 6),
      "\n 4 + 5 ", check_ten(4, 5))


# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.

def check_ten_sum(n1, n2):
    sum = n1 + n2
    if (sum == 10):
        return True
    else:
        return sum


print("4 + 6 ", check_ten_sum(4, 6),
      "\n 4 + 5 ", check_ten_sum(4, 5))

# ## Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.


def first_upper(mystring):
    return mystring[0].upper()


print("fuss ", first_upper("fuss"))
print("house ", first_upper("house"))


# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)


def last_two(mystring):
    if len(mystring) >= 2:
        return mystring[-2:]
    else:
        return "Error"


print(last_two("house"))
print(last_two("g"))


# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.


def seq_check(nums):
    check_value = [1, 2, 3]
    check_index = 0
    for i in nums:
        if i == check_value[check_index]:
            check_index += 1
        else:
            check_index = 0
        if check_index == 3:
            return True

    return False


print(seq_check([0, 1, 2, 3, 4]))
print(seq_check([0, 1, 3, 3, 4]))
print(seq_check([1, 2, 3, 1, 2]))
print(seq_check([1, 2, 1, 1, 3]))


# ## Task 6
#
# Given 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**


def compare_len(s1, s2):
    diff = 0
    diff = len(s1) - len(s2)

    return abs(diff)


print("6 and 4 ", compare_len("houses", "boat"))
print("2 and 8 ", compare_len("it", "quickest"))

# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
# value in that list.


def sum_or_max(mylist):
    list_len = len(mylist)
    summax = 0
    if list_len % 2 == 0:
        for i in mylist:
            summax += i
    else:
        for i in mylist:
            if i > summax:
                summax = i

    return summax


print("1 2 3 4: ", sum_or_max([1, 2, 3, 4]))
print("12 24 34 4 4 4 0: ", sum_or_max([12, 24, 34, 4, 4, 0]))
print("1 2 3: ", sum_or_max([1, 2, 3]))
print("12 3 54 5 69: ", sum_or_max([12, 3, 54, 5, 69]))
