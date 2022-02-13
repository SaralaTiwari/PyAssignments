"""
© https://sudipghimire.com.np


String Exercise


Please read the note carefully and try to solve the problem below:


"""

"""
1. Create two variablrs first_name, and last_name and print the sentence in the format below:
   suppose first_name is John and last_name is Doe
   "My name is John Doe"

   a. use + operator to concatenate strings
   b. use format() method to achieve the same result
   c. use f-strings to achieve the same result
   d. use %s formatting method to achieve the same result
"""
# answer 1
first_name = "Mark"
last_name = "Horse"
# 1.a
print("My name is ", first_name +  " " + last_name + ".")

# 1.b
print("My name is {} {}.".format(first_name, last_name))


# 1.c
print(f"My name is {first_name} {last_name}.")

 
# 1.d

print("My name is %s %s." %(first_name, last_name))

"""
2. Assign a variable  pi and assign value 3.14159265
    a. use formatting strings to show pi with 3 digits after the decimal
    b. use formatting strings to show pi with 2 digits after the decimal but
       allocate 10 spaces for the variable
    c. use f-string to show the result in the following format:
        "The value of PIE is        3.14"

        hint: "%<a>.<b>f"
"""
# answer 2
pi = 3.14159265
# a
# print("The value of pi:%10:3f) #CONFUSED HERE
# b


# c
# print("the value is:%10.3f" % 44.2345345)
print(f"The value of PIE is:%10.2f"%pi)

"""
3. Use a function `input()`  to input the the name and age from the command line and
   display the formatted text as instructed below:

   a. use `input()` function to ask the name to the user. The console should show
      "What is your name?" to input the name
   b. similarly ask the user to input the age and assign it to another variable.

   c. Show a sentence describing the user name and age using different formatting methods.

      hint: Output would be a sentence similar to "Hello 20 years old John!!".
"""

# answer 3


# %%
#3a.
output = input("what is your name? ")
print(output)
#3b.
age = input("Lovely name! How old are you? ")
print(age)
age = 29
#3c.
print("Hello" + output + ", your name is lovely! and you are " + age + "years old") #Confused