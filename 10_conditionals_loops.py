# """"
# © https://sudipghimire.com.np

# Conditional and loop Exercises
# """
# # from ast import Str
# # import math
# # import numbers
# # from this import s


# '''
# 1.  Write a program to input a number and check whether a number is an integer or not
#     hint: you can use isnumeric() function
# '''
# # Answer
# # number = print(input('Write a number: '))
# # if number.isnumberic():
# #     print(f'{number} is an integer.')
# # else:
# #     print(f'{number} is no an integer.')

# '''
# 3. from the list below, separate a list that are even and odd and put them into the respective variables

# the final output should be:

# Odd_numbers: [1, 5, 89, 167, 333, 5, 23]
# Even_numbers: [2, 32, 112, 20]

num = [1, 5, 2, 89, 32, 112, 167, 333, 20, 5, 23]
odd_num = []
even_num = []
for n in num:
    if n%2 == 0:
        even_num.append(n)
    else:
        odd_num.append(n) 
print(even_num) 
print(odd_num)  # DONE 
'''
4.  Write a program to input 2 different words and find out if the words are Palindrome or not.

    - A word is palindrome if reads the same from both backward and forward.

    Eg: EVE, HANNAH, BOB, ANNA, ROTATOR, REPAPER
________________________________________________________________________
The Output in the console should look like below
________________________________________________________________________
Enter a word: Hannah
Hannah is a palindrome word
________________________________________________________________________
'''
# answer here
    
from audioop import reverse

first_word = (input(('Do you have a word in mind? ')))
if first_word==(first_word[::-1]):
    print(f"{first_word} is a Palindrom.")
else:
    print("{first_word} is not a Palindrom.", end = " ")

# How do I break the first loop from repeating? Or how do I merge these two into one?
# I tried break but it shows error and used elif to merge the 4 lines of codes but unsuccessful. 
second_word = (input(('Do you have a word in mind? ')))
if second_word==(second_word[::-1]):
    print(f"{second_word} is a Palindrom.")
else: 
#     print("{second_word} is not a Palindrom.") # DONE


# # '''
# # 5.  Write a program to print the first 20 fibbonnaccii numbers

# #     The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is
# #     the sum of the previous two numbers in the sequence.
# #     eg: 1, 1, 2, 3, 5, 8, 13, ...

# #     hint: use for loop in range of 20, add a and b and update values of a, b and others if necessary
# # '''
"""fib_num =  20
a, b = 1, 1
sum = a + b
print(sum)
# # answer here
# while 
for n in range(0, 20):
    a = b
    b = a
    sum = a + b 
    print(sum + n)
print(sum, end =" ")"""

def fibonacci(i):
    if i == 0:
        return 0
    elif i ==1:
        return 1
    else:
        return fibonacci (i-2) + fibonacci (i -1)
for n in range (0, 20):
    print(fibonacci(n)) #DONE #Learnt this one from a youtube video but don't understand the (i-2, i -1) portion. 

# # 6.  Write a program to enter a month and day of birth and find out the horoscope of a person:

# # - Aries: Mar 21 - Apr 19
# # - Taurus: Apr 20 - May 20
# # - Gemini: May 21 - Jun 20
# # - Cancer: Jun 21 - Jul 22
# # - Leo: Jul 23 - Aug 22
# # - Virgo: Aug 23 - Sep 22
# # - Libra: Sep 23 - Oct 22
# # - Scorpio: Oct 23 - Nov 21
# # - Sagittarius: Nov 22 - Dec 21
# # - Capricorn: Dec 22 - Jan 19
# # - Aquarius: Jan 20 - Feb 18
# # - Pisces: Feb 19: Mar 20

# # ________________________________________________________________________
# # The Output in the console should look like below
# # ________________________________________________________________________
# # Enter your Month and Day of Birth [Eg: Oct 20]: Oct 20

# # Your Horoscopic Sign is:    Libra
# # ________________________________________________________________________

# # Hint:
# #     you can use `split()` function to split words from a string
# # '''
# # # date = 'Oct 20'
# # # month, day = date.split()
# # # day = int(day)
# # # print(month,'/', day)

# # # answer
from datetime import date

month_of_birth = input("What month were you born? ")
month_of_birth.lower()
day = int(input("What day were you born? "))
months = ['march', 'april', 'may', 'june', 'july', 'august', 'sep', 'oct', 'nov', 'dec', 'jan', 'feb']

if month_of_birth in months:
    if month_of_birth =='march':
        print(f"Your horoscope is Pisces." if (day<=21) else "Your horoscope is Aries")
    elif month_of_birth =='april':
        print(f"Your horoscope is Taurus." if (day<=20) else "Your horoscope is Gemini")
    elif month_of_birth =='may':
        print(f"Your horoscope is Gemini." if (day<=21) else "Your horoscope is Cancer")
    elif month_of_birth =='june':
        print(f"Your horoscope is Cancer." if (day<=22) else "Your horoscope is Leo")
    elif month_of_birth =='july':
        print(f"Your horoscope is Leo." if (day<23) else "Your horoscope is Virgo")
    elif month_of_birth =='august':
        print(f"Your horoscope is Virgo." if (day<22) else "Your horoscope is Libra")
    elif month_of_birth =='sep':
        print(f"Your horoscope is Libra." if (day<22) else "Your horoscope is Scorpio")
    elif month_of_birth =='oct':
        print(f"Your horoscope is Scorpio." if (day<21) else "Your horoscope is Sagittarius")
    elif month_of_birth =='nov':
        print(f"Your horoscope is Sagittarius." if (day<21) else "Your horoscope is Capricorn")
    elif month_of_birth =='dec':
        print(f"Your horoscope is Capricorn." if (day<19) else "Your horoscope is Aquarius")
    elif month_of_birth =='jan':
        print(f"Your horoscope is Aquarius." if (day<18) else "Your horoscope is Pisces")
    elif month_of_birth =='feb':
        print(f"Your horoscope is Pisces." if (day<18) else "Your hosroscope is ")
    




# # '''
# # BONUS QUESTION
# # 1.  Suppose you went to a coffee shop. A shopkeeper asked you to create a program that serves coffee
# #     according to the customer's requirements.

# #     The coffee machine should ask user to enter any numbers below that should make a coffee and serve it to the user.
# #     Please use the `make_coffee()` function below to prepare a coffee and serve it. below are the conditions:

# #     1. Espresso
# #         - price: $2
# #         - type: hard

# #     2. Americano
# #         - price: $2.5
# #         - type: mild

# #     3. Cappuccino
# #         - price: $3
# #         - type: soft

# #     The program should be able to ask user to input a number 1, 2 or 3 and display message according to the conditions above.

# # ________________________________________________________________________
# # The Output in the console should look like below
# # ________________________________________________________________________
# # Today's Menu:
# # 1. Espresso
# # 2. Americano
# # 3. Cappuccino

# # Enter Number:   1

# # Dear Customer, Your Espresso is ready. please pay $2 at the counter.

# # Quick fact: Espresso is a hard coffee.
# # ________________________________________________________________________
# # '''
# # # Answer
def complete_menu():
    {
    '1': 'Espresso',
    '2': 'Americano',
    '3': 'Cappuccino',
}
    make_coffee = int(input('Press number to pick your coffee: '))
    if make_coffee ==()

def more_options(): 
    {
    'Espresso': {'price': 2, 'type': 'hard'},
    'Americano': {'price': 2.5, 'type': 'mild'},
    'Cappuccino': {'price': 3, 'type': 'soft'},
}
# Couldn't do this. 

# # '''
# # BONUS QUESTION
# # 2. Write a program to check whether a number is a special number or not.

# #    If the sum of the factorial of digits of a number (N) is equal to the number itself,
# #    the number (N) is called a special number.

# # Eg: 145 is a special number where, 1! + 4! + 5! = 145

# # try it with numbers:    145, 1, 35

# # Hint 1: you can get each digit using a modulus and integer division of a number by 10 until the number is less than 10
# #     eg: 145
# #         145//10 = 14        145%10=5                    (5 is ones digit)
# #         14//10 = 1          14 % 10 = 4                 (4 is tens digit)
# #         at the end, 1 (which is less than 10)           (1 is hundreds digit)

# # hint 2: you can use `math.factorial()` to find out factorial of a number.

# # '''
# # # answer here

# # """
# # BONUS QUESTION
# # 3.  Hangman Game
# #     Create a Guessing game that gives you 3 chance for a person to make mistakes
# #     Use a word "Elephant" for now
# # ________________________________________________________________________
# # HANGMAN !!

# print("Welcome to the game of Hangman. You will be given 7 chances to complete the word.")
# print(input("What's the letter?"))
import random
def letter():
    letter = ['l', 'e', 'h', 'a']
    return random.coice(letter)
def play_game():
    word = letter()
    word_input = ['l', 'e', 'h', 'a']
    allowed_times = 7
    guessed_letter = False 

    print('The word contains', len(word), 'letter.')
    
# = "E _ _ p _ _ n t"
allowed_mistakes = 3
word = 'Elephant'
word_input = ['l', 'e', 'h', 'a']
user_input= []
while allowed_mistakes>3:
    letter = input("Welcome to the game of Hangman. You will be given 7 chances to complete the word.What's the letter?"))
    if letter in word_input:
        user_input.append(word_input)
        print("{user_input} is the first letter. Next letter?") 
        if len(user_input)==4 and user_input == word_input:
            print(f'Great job! the word is {word}.')
            break 
        else:
            print("Good going. Keep trying!")
    else:
        allowed_mistakes+=1
        print(f'The letter {user_input} is not the right one. Only {3-allowed_mistakes} left. \n')
# This one is confusing too. There's no output when I run the code. 






if word_input == ('l', 'e', 'h', 'a'):
    print("That's the first letter. Next letter?") 
    
    else "That's no the correct letter"
if word_input == ['l', 'e', 'h', 'a']:
    print("That's the second letter. Next letter?")
if word_input == ['l', 'e', 'h', 'a']:
    print("That's the third letter. Next letter?")
if word_input == ['l', 'e', 'h', 'a']
    print("That's the first letter. Next letter?")

            
# Enter the position, and character [eg: 2 l] to fill the blanks

#  E _ _ p _ _ n t    ( 0 / 3 mistakes ):     2 l
#  E l _ p _ _ n t    ( 0 / 3 mistakes ):     3 a

#  E l * p _ _ n t    ( 1 / 3 mistakes ):

#  Try your own logig, or ways. we'll be discussing answers for this game.
# ________________________________________________________________________
"""
# actual_word = 'Elephant'
# question = 'E _ _ p _ _ n t'
# remaining = 'leha'
# progress = 'E _ _ p _ _ n t'

# mistake = 0

# while mistake < 3:
#     next_word = input(f' {progress}\t( {mistake} / 3 mistakes ):\t')
#     # remaining answer here"""
