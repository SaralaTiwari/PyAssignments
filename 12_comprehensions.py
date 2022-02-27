"""
© https://sudipghimire.com.np

Comprehension Exercises
"""

'''
1. convert the following loop to list comprehension
'''
# list = []
# for x in range(10):
#     list.append(2*x+1)

# Answer Here
# list =[x*2+1 for x in range(10)]
# print(list) #DONE

'''
2.  Generate a dictionary from a list of first 10 numbers and it's square values
    using dictionary comprehension.
    Final value should be in format: {1:1, 2:4, 3:9, 4:16, ..., 10, 100}
'''
#Answer Here
# Trying with conding first
# from re import L
# l1=[]
# for key in list(range(1, 11)):
#     l2 = [key, key ** 2]
#     print(l1.append(l2))
# print(l1)
# into_dict = dict(l1)
# print(into_dict)
#=========================================================================================#
# var = {<key_expr>: <value_expr> for <element> in <iterable> if <condition>}
# var = {<key_expr>: <value_expr> for <element> in <iterable>}
# dict_comprehension = {key : key ** 2  for key in range(1, 11)} #DONE
# print(dict_comprehension)
'''
3.  Create the following pattern using list comprehension, `join()` method, and others if needed.
    Try to solve in a single line or single statement.

    1
    1   2
    1   2   3
    1   2   3   4
    1   2   3   4   5
'''
# Answer Here
# for r in range(1,6):
#     for c in range(1,r+1):
#         print(c, end = " ")
#     print()
# p1 = '\n'.join([' '.join([str(r) for c in range(c,1+1)])for r in range(1,6)])
# print(p1) #DONE
'''
4.  A mathematical function is defined by y = (4x ** 2) + (3 * x) - 6
    i. Create a generator function to generate first 1000 integers starting from -100 and store to a variable y.
    ii. Create a list using list comprehension to generate the same values
    iii. Compare the memory usage by those variables created in steps (i) and (ii) using __sizeof__() method.
    iv. Try to generate values of y for first million integers and compare memory usage as done in step (iii).
    To learn more about __sizeof__() method, please visit https://www.javatpoint.com/sizeof-in-python
'''
# Answers
# def mathm(x):
#     for i in range(-100,1000):
#         y = (4*x ** 2) + (3 * x) - 6
#         return i, i+1
# print(mathm(2)) #Can't figure this out.
'''
5.  Write a program to split a string 'Apple' into a dictionary of
    ASCII values of each characters using comprehension methods.

    To learn more about ASCII please refer to the site https://www.asciitable.com/

    Use the `ord()` method to find out the ASCII values

    final output should be: {'A': 65, 'p': 112, 'l': 108, 'e': 101}
'''
# Answer Here # Question to ask during revision class.

'''
6.  Write a program to generate a dictionary from the given nested tuple using dictionary comprehension.
'''
abbreviations = (
    ('ABC', 'Atanasoff Berry Computer'),
    ('BCD', 'Binary Coded Decimal'),
    ('CD', 'Compact Disc'),
    ('DVD', 'Digital Video Disc'),
    ('HTTP', 'Hyper Text Transfer Protocol'),
    ('WWW', 'World Wide Web'),
    )
abbre_comprehension = dict(abbreviations)
abbre_comprehension = {k : v for k, v in abbre_comprehension}
print(abbre_comprehension)
# print(abbre_comprehension)
# {key: value for key value in abbreviations}
# Answer Here
# var = {<key_expr>: <value_expr> for <element> in <iterable> if <condition>}
# var = {<key_expr>: <value_expr> for <element> in <iterable>}

'''
BONUS EXERCISES
7.  Try All of the pattern generation exercises (if possible) with list comprehension
'''
# ANSWERS HERE
