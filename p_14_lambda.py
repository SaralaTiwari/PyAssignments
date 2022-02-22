"""
© https://sudipghimire.com.np

Lambda Exercises
"""


"""
1.
Convert the following function to a lambda function
"""
# def odd_or_even(num):
#     if num%2==0:
#         return 'even'
#     else:
#         return 'odd'
#         do_something = lambda a,b: (a+b) * (a**b)
# answer
# odd_or_even = lambda num: num%2==0
# print(odd_or_even(7)) #DONE

"""
2.
Create a lambda that accepts a list of numbers and return the list of squares of them

hint:
you can use list comprehension to return the list of squares
"""
#answer
list_of_numbers= lambda x: x in list_of_squares
list_of_squares=[x**2 for x in range(10)]
print(list_of_squares) #Tried my best here. Don't know if this is correct.
"""
3.
create a lambda function that converts the length from meter to feet
"""
# answer
# values hypothetical.
feet = lambda meters:  13*0.666
print(feet(2))#DONE

"""
4.
Create a lambda function that takes an argument and finds out the square if it is even and cube if it is odd.
"""
# answer

even_or_odd = lambda x: x**2==0
print(even_or_odd(5)) #Not sure about this either.
"""
5.
Create a lambda function `get_date` that takes 3 arguments month, year, and day that
returns a single string in a "YY/MM/DD" format.
"""
# answer
get_date = lambda Y,M,D: Y/M/D
print(get_date(2001, 12, 14))
# uncomment below when you solve problems
# print(get_date(2001, 12, 14))    # "2001/12/14"
#

"""
6.
Create a lambda function that accepts a sentence that returns the sentence with spaces replaced by hyphens

example:
input => "A quick brown fox jumps over the lazy dog."
output => "A-quick-brown-fox-jumps-over-the-lazy-dog."

hint:
use string.replace() method
"""
with_spaces= lambda r: r.replace(' ','-')
print(with_spaces("A quick brown fox jumps over the lazy dog."))#DONE
# answer


"""
7.
Create a lambda function that checks whether the string provided is a number or not
"""
# answer

string_privided = lambda n: n.replace('.','',1).isdigit()
print(string_privided('34'))#DONE
"""
8. create a lambda function to count total number of even numbers in a list
"""
# answer
list_even=list(range(40))
even_numbers= lambda x: x%2==0 in list_even
print(even_numbers)#NOT SURE About this either.
