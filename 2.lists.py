

# 1. Write a program that sum of all elements:
one = [613, 955, 291, 497, 562, 483, 165, 210, 864, 789]
sum_result = 0

for number in one:
    sum_result += number

print("Sum of all elements:", sum_result)

# 2.  Write a program that find the largest element:
two = [386, 850, 274, 316, 526, 937, 998, 249, 269, 922]
max_result = max(two)

print(f"The largest number is: {max_result}")

# 3. Write a program that duplicates that doubles the value of each elements in the list:
# for example: [1,2,3] should result in [2,4,6]
three = [211, 36, 295, 455, 147, 977, 381, 253, 327, 617]
# Double the value of each element using a list comprehension
doubled_elements = [2 * x for x in three]

print("Original List:", three)
print("Doubled List:", doubled_elements)


# 4. Write a program that concatenates these two list into a single list:
four_a = [582, 427, 534, 143, 567, 604, 12, 48, 686, 825]
four_b = [357, 728, 406, 989, 380, 800, 201, 410, 452, 141]

#concatenate both lists
concatenated_list = four_a + four_b

print(f"Concatenated List: {concatenated_list}")
# 5. Write a program that removes a specific element from a list by its value.
five = [456, 942, 944, 762, 836, 451, 314, 559, 954, 211]

number_to_remove = 456
if number_to_remove in five:
    five.remove(number_to_remove)

print(f"List after removing {number_to_remove}: {five}")
# 6. Write a program that removes a specific element from a list by its index.
six = [993, 245, 896, 250, 226, 313, 918, 877, 793, 695]

index_to_remove = 4

if 0 <= index_to_remove < len(six):
    del six[index_to_remove]
    print(f"Number at index {index_to_remove} removed.")
else:
    print("Invalid Index")

print(f"List after removal: {six}")

# 7. Write a program that sorts a list of numbers in ascending order.
seven = [887, 106, 368, 603, 35, 455, 728, 449, 108, 47]

#sort the list in ascending order
seven.sort()

print(f"List sorted in ascending order: {seven}")


# 8. Write a program that filters out all elements in a list that are less than a specified value.
# use for loop and conditionals
eight = [309, 122, 27, 240, 453, 174, 193, 649, 804, 171]
threshold = 200

# Create a new list to store filtered elements
filtered_list = []

# Iterate through the elements in the original list
for number in eight:
    if number >= threshold:
        filtered_list.append(number)

print(f"Original List: {eight}")
print(f"Filtered List (elements >= {threshold}):", filtered_list)

# 9. Calculate and print the length (number of elements) of a given list.
nine = [679, 697, 657, 171, 503, 582, 656, 82, 724, 796]

# Calculate and print the length of the list
list_length = len(nine)

print("Length of the list:", list_length)

# 10. Write a program that take a list and print a subset of its elements by specifying a start and end index.
ten = [64, 800, 662, 185, 630, 612, 181, 210, 738, 12]
start_index = 1
end_index = 4

# 11. Write a program iterates the list and
# prints 'FizzBuzz' when divisable by 3 and 5.  
# prints 'Fizz' when divisable by 3 .  
# prints 'Buzz' when divisable by 5. 
eleven = [213, 927, 265, 39, 860, 421, 550, 884, 991, 1500]



# 12. Write a program that appends an element to the end of a list.
twelve = [36, 632, 155, 350, 746, 642, 113, 534, 9, 34]


# 13. Write a program that inserts an element at a specific position in a list.
thirteen = [191, 871, 990, 163, 687, 747, 606, 799, 373, 851]
element_to_insert = 4


# 14. Write a program that counts how many times a specific element appears in a list.
fourteen = [1, 1, 1, 2, 2, 1, 3, 3, 2, 1]
element_to_count = 1

# try using for loop and conditional
# and then try .count() method


# 15.  Write a program that extracts all even numbers from a list and stores them in even_only:
# use for loop and conditionals
fifteen = [267, 688, 88, 755, 680, 746, 559, 710, 283, 451]
even_only = []




# 16. Write a program that reverses this list but does not change the original sixteen variable:
# The answer is not sixteen.reverse(). 
sixteen = [378, 763, 856, 566, 847, 795, 313, 540, 67, 219]


# 17. Write a flattens this double nested listbelow:
# Result should be [1, 2, 3, 4, 5, 6, 7, 8]
# Hint: try a nested loop (2 for in loops) 
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]


# 18. Write a program that finds duplicates from the 2 lists below:
# Hint: try a nested loop (2 for in loops) and use equality
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

