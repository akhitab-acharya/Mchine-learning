https://cs231n.github.io/python-numpy-tutorial/
Python & Numpy Tutorial by Stanford -  It's really great and covers things from the ground up.

#Quicksort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))


# Prints "[1, 1, 2, 3, 6, 8, 10]"

-----------------------------------------

#LIST COMPREHENSION:

nums = [1, 2, 3, 4]
num_squares = [x**2 for x in nums]
print(num_squares)


# list comprehension with conditions:

num_even_square = [x**2 for x in nums if x % 2 == 0]
print(num_even_square)

------------------------------------------------------------

# DICTIONARY COMPREHENSION:

nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)  # Prints "{0: 0, 2: 4, 4: 16}"

--------------------------------------------------------------------------------------
s = "hello"
print(s.capitalize())  # Capitalize a string; prints "Hello"
print(s.upper())       # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))      # Right-justify a string, padding with spaces; prints "  hello"
print(s.center(7))     # Center a string, padding with spaces; prints " hello "
print(s.replace('l', '(ell)'))  # Replace all instances of one substring with another;
                                # prints "he(ell)(ell)o"
print('  world '.strip())  # Strip leading and trailing whitespace; prints "world"
------------------------------------------------------------------------------------------

# EX. OF ENUMERATE:

animals = {'cat', 'dog', 'cow'}
for idx, animal in enumerate(animals):
    print('#%d %s' % (idx + 1, animal))

# Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line

-------------------------------------------------------------------


