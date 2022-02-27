"""
© https://sudipghimire.com.np

Function Exercises
"""

"""
1. Write a python function to find the largest out of 3 numbers
You should use comparison operator to find out the maximum of 3 numbers.
"""

# def vehicle_allowed(number):
#     if number%2==1:
#         print(f"{number}: allowed")
#     else:
#         print(f"{number}: not allowed")
# answer
# def num(a, b, c):
#     if  a >= b and a >= c:
#         return(f"{a} is the largest number.")
#     elif b >= a and b >= c:
#         return(f"{b} is the largest number.")
#     else:
#         return(f"{c} is the largest number.")
#     return(num)
# print(num(99,3,8))#DONE

"""
2. Write a python function that calculates the number of upper case characters, lower case characters
 and spaces in the string and returns them as a tuple.

for example

x = "A Quick Brown Fox Jumps Over The Lazy Dog."

Number of upper case characters: 9
Number of lower case characters: 14
Number of spaces: 8
"""
# Answer

# def sentence(x):
#     case = {'upper':0, 'lower': 0}
#     for letter in x:
#         if letter.isupper():
#             case['upper']=case['upper'] + 1
#         if letter.islower:
#             case['lower']=case['lower'] + 1
#     print("upper:'case['upper'])
s = "A Quick Brown Fox Jumps Over The Lazy Dog."
def count(x) :
    upperCase = 0
    lowerCase = 0
    space = 0
    for letter in x:
        if letter.isupper():
            upperCase += 1
        elif letter.islower():
            lowerCase += 1
        elif letter == ' ':
            space += 1
    return (upperCase, lowerCase, space)
# print(count(s))#DONE

'''
3.
Suppose you went to a coffee shop. A shopkeeper asked you to create a program that serves coffee
according to the customer's requirements.

The coffee machine should ask user to enter any numbers below that should make a coffee and serve it to the user.
Please use the `make_coffee()` function below to prepare a coffee and serve it.

Followings are the ingredients for coffee:

Sugar: no. of spoons
beans: no. of spoons
milk: volume in ml.

The total volume of coffee should be 250ml. The maximum volume of milk can be only upto  150ml. greater than that
should give the error saying not acceptable.

Finally print the line describing the coffee you prepared along with  milk and water composition.

'''
# answer
def make_coffe(sugar, beans, milk_ml):
    if(milk_ml > 150):
        print("Not acceptable")
    else:
        water_ml = 250 - milk_ml
        print(f'Your coffee contains {sugar} spoons of sugar, {beans} spoons of beans, {milk_ml} ml Milk, {water_ml} ml water')

# make_coffe(10, 15, 250)
# make_coffe(10, 15, 50)
# make_coffe(10, 15, 150)#DONE

"""
4.
Write a program to create a multiplication table of the given number.
The `mul_table()` function should have the following arguments:
- `number`: the number to print multiplication table of.
- `limit`: the number upto which multiples are printed which should have the default value of 10

Multiplication table for 13

| 13  X   1|    13|
| 13  X   2|    26|
| 13  X   3|    39|
| 13  X   4|    52|
| 13  X   5|    65|
| 13  X   6|    78|
| 13  X   7|    91|
| 13  X   8|   104|
| 13  X   9|   117|
| 13  X  10|   130|

"""
# Answer Here
def mul_table(number, limit):
    # number = 13
    for i in range (1, limit+1):
        #print(limit+1)
        mult = number * i
        print(f"{number} * {i} = {mult}")
    print()

# mul_table(13, 10)#DONE
"""
5.
Write a function that takes a string and checks whether the word is palindrome or not.
- A palindrome is a string that reads the same backward or forward.
- Examples: eve, dad, rotator

Your program should be able to ask user to enter the word and check whether it is palindrome or not.
The program should not end until user enters no.
The program should start with the
The output should show inside a box as shown below with text justified center.
Example Output:
=============================[ Palindrome Finder ]=============================
Enter a word: rotator

+-----------------------------------------------------------------------------+
|                   The word 'rotator' is a palindrome                        |
+-----------------------------------------------------------------------------+

The word 'rotator' is a palindrome word

Do you want to check again? [yes/no]: yes

Enter a word: dad

+-----------------------------------------------------------------------------+
|                     The word 'dad' is a palindrome                          |
+-----------------------------------------------------------------------------+


Do you want to check again? [yes/no]: no

=================================[ exiting now ]================================

"""
#Answer
from audioop import reverse

# def palindrom(word):
#     word = str(input('what is your word? '))
#     if word == word[::-1]:
#         print(f'{word} is palindrom.')
#     if word == 'no':
#         print("Good Bye!")
#     elif print(f'{word} is not palindrome.'):
#         return(word)
# print(palindrom('love'))



# def outer_box(value: str):
#     print('+', '-'* 60, '+', sep = '')
#     print('|', ' '* 60, '|', sep = '')
#     print('+', '-'* 60, '+', sep = '')

# def exit_bod(value:str):
#     print('=' * 30, '[ exiting now ]', '=' * 30 )
# print(outer_box('Sarala'))#Don't know how to merge these together as a single code.
"""
6.
Write a function that accepts words that are separated by hyphen returns the alphabetically sorted words
separated by hyphen.

Hint:
- split the words using string.split() method
- sort the list
- join the list to a string with string.join() method
"""
word = "cat-apple-dog-ball-ears-goose-fish"

def sentence(s):
    splited_word = s.split('-')
    sorted(s.split('-'), key = str.lower)
    return s
s = sentence(word)
# print(s) #Couldn't figure this out either.

"""
7.
Write a function that accepts a number x
- if x is a multiple of 2, it should return the value y = x**2 + 2x + 3
- if x is a multiple of 3, it should return the value y = x**3 + 4x + 5
- if x is a multiple of both 2 and 3, it should return the value y = x**3 + 4x**2 + 5x + 6
- in other cases it should return negative value of the given number
"""
# answer

def problemo(x):
    if x%2==0:
        y = (x**2) + (2*x + 3)
        print(f'The final value is {y}.')
    if x%3==0:
        y = (x**3) + (4*x + 5)
        print(f'The final value is {y}')
    if x%2==0 and x%3==0:
        y = (x**3) + (4*x**2 + 5*x +6)
        print(f'The final value is {y}')
    else:
        print(f'-{x}')
    return(x)

print(problemo(2)) #DONE I think.


"""
8.
Write a function that accepts any number of arguments
find out the sum of all numbers by multiplying by 2 if it is odd and dividing by 2 if the number is even.

Example if arguments are (5,6,7,8)

the result should be 31 [ 5*2 + 6/2 + 7*2 + 8/2 ]
"""
# answer
def any(*args):
    x = args
    if x%2 == 0:
        y = x%2
    if x%2 != 0:
        j = x*2
        return(y+j)
# print(any(2, 4, 5,53,2,4,56)) #Can't figure this one out too. Error:if x%2 == 0:TypeError: unsupported operand type(s) for %: 'tuple' and 'int'
