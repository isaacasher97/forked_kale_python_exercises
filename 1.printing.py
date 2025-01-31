
# 1. Using the print method, print "Hello World"
# print('Hello World')
# 2. Create variables for the data type below. 
# Data Types:
# Int
my_integer = 26;
# Float
my_float = 1.23;
# String
my_string = 'Hello World 2';
# Boolean 
my_boolean = True;
# Boolean (The other boolean value)
my_other_boolean = False;
# Lists ( 4 items in list min.)
my_list = [1, 2, 3, 4]
# Dictionaries  ( 4 key/value pairs min.)
my_dictionary = {
    "name": "Isaac",
    "age": 26,
    "city": "New York City",
    "country": "USA"
}
# 3. For each of the variables, use the print method for each variable. To print each varible
#int
# print(my_integer)
#float
# print(my_float)
# string
# print(my_string)
#boolean
# print(my_boolean)
#other_boolean
# print(my_other_boolean)
#lists
# print(my_list)
#dictionaries
# print(my_dictionary)
# 4. Backtick ` in JS are used for Template literals. In a JS file a variable called intVariable and stringVariable exist.
# They are equal to the int and string variables on step 2.
# What is the python equvalent for: console.log(`int: ${intVariable}, string ${stringVariable}`)
# print(f'int: {my_integer}, string: {my_string}')
# 5. Comment out all print statements up to this point

# 6. Write a FOR LOOP in python that prints "David Rocks" 5 times
# Hint: type this into google "loop range python"
# for i in range(5):
    #print("David Rocks")

# 7. Declare a function what print "Alex Rocks". Invoke that function 5 times. 
#define
# def alex_rocks():
    # print("Alex Rocks")

#invoke 5 times
# for i in range(5):
    # alex_rocks()


# 8. Declare a function that takes in 2 parameters. 
# It will print "P1(your parameter1) and P2(your parameter2) Rocks"
# def my_function(param1, param2):
    # print(f"{param1} and {param2} Rock")
# Now call that function using "Kyle" and "Winston" as the arguments
# my_function("Kyle", "Winston")
# invoke that function 4 more times
# for i in range(4):
    # my_function("Kyle", "Winston")

# Definitions:  
# P is for Placeholder. P is for Parameters.
# These 2 start w/ the letter P 
# A parameter is variable in the declaration of the function - The place holder

# A is for actual value. A is for aguement.
# These 2 start w/ the letter A
# Arguement is are the values when calling the function - The actual value

# 9. Remember the list variable in step 2. 
# a. Print the index at 3. Then comment it out
#print(my_list[3]) #Output => 4
# b. Now print the index at 100. Does this error? comment it out
#print(my_list[100]) #Output => IndexError: list index out of range 
# e. Now print the index at -1 index. Observe what it prints. Then comment it out
#print(my_list[-1]) #Output => 4
# f. Now print the index at -100.  Does this error? comment it out
#print(my_list[-100]) #Output => IndexError: list index out of range 
# 10. Write a FOR LOOP in python that prints each item in the list variable in step 2.  
# The staring number MUST be a negative number. The ending number MUST be postive number
# Looking to get each item printed once in order and then a second time in order
# Loop to print each item in order
# for i in range(-len(my_list), len(my_list)):
    # print(my_list[i])

# Loop to print each item in order again
# for i in range(-len(my_list), len(my_list)):
    # print(my_list[i])

# 11. Write a WHILE LOOP in python that does the same thing as 10. 
#set the index to = the first negative index
# index = -len(my_list)

# while index < len(my_list):
    # print(my_list[index])
    # index += 1

#reset the index
# index = -len(my_list)
#repeat the process
# while index < len(my_list):
    # print(my_list[index])
    # index += 1
# 12. For loops.
# Write a FOR LOOP in python that prints each item in list variable in step 2.  
# Hint: type this into google "loop python"
# for item in my_list:
    # print(item)
# 13. Repeat step 12 but instead of the list variable, use the dictionary variable. 
# Print each key
# for key in my_dictionary:
    # print(key)
# 14. Repeat step 13. Instead of printing each key, print each value
# Hint: google "dictionary values python"
for key in my_dictionary:
    value = my_dictionary[key]
    print(value)