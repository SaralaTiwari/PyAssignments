"""
© https://sudipghimire.com.np

Pattern Generation Exercises
"""

# Write programs to generate following patterns

"""
Pattern 1
*
*   *
*   *   *
*   *   *   *
*   *   *   *   *
"""
# Answer Here
# no_rows = int(input("Enter your value: "))
# for row in range(1, no_rows+1 ):
#     for column in range(1, row+1):
#         print("*", end = ' ')
#     print() #Done

"""
Pattern 2
1
1   3
1   3   5
1   3   5   7
1   3   5   7   9

"""
# Answer Here
# for row in range (6):
#     for col in range(0,row):
#         print((col*2) +1, end=" ")
#     print() #DONE
"""
Pattern 3
1
2   2
3   3   3
4   4   4   4
5   5   5   5   5
"""
# Answer Here
# for row in range(5):
#     for col in range(row+1):
#         print(row+1, end=" ")
#     print() #DONE

"""
Pattern 4
1
2   1
3   2   1
4   3   2   1
5   4   3   2   1


"""
# Answer Here
# for row in range(5):
#     for col in range(row+1):
#         print(row-col+1, end= " ")
#     print() #DONE
"""
Pattern 5

1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25

"""
# Answer Here
# for row in range(5):
#     for col in range(5):
#         print((col+1)*(row+1), end=" ")
#     print() #DONE
'''
Pattern 6

A
A   P
A   P   P
A   P   P   L
A   P   P   L   E

'''
# word = "APPLE"
# # Answer here
# for row in range(5):
#     for col in range(row+1):
#         print(word[col], end=" ")
#     print() #DONE

"""
Pattern 7

                *
            *   *
        *   *   *
    *   *   *   *
*   *   *   *   *

"""
# Answer Here
# n = 5
# for row in range(n):
#     for col in range(row, n):
#         print(" ",end=" ")
#     for col in range(row +1):
#         print('*', end=' ')
#     print() #Done
"""
Pattern 8

                1
            1   3
        1   3   5
    1   3   5   7
1   3   5   7   9

"""
# Answer Here
# n =5
# for i in range(n):
#     for j in range(i, n):
#         print(' ', end=" ")
#     for j in range(i+1):
#         print((j*2)+1, end=' ')
#     print() #DONE

'''
Pattern 9

                A
            A   P
        A   P   P
    A   P   P   L
A   P   P   L   E

'''
# word = "APPLE"
# # Answer here
# for i in range(5):
#     for j in range(i, 5):
#         print(' ', end=' ')
#     for j in range(i +1 ):
#         print(word[j], end=" ")
#     print()#DONE



"""
Pattern 10  (Bonus Exercise)
                1
            1   2   1
        1   2   3   2   1
    1   2   3   4   3   2   1
1   2   3   4   5   4   3   2   1


"""
# Answer Here
for i in range(5):
    for j in range(i, 4):
        print(' ', end=" ")
    for j in range(i):
        print((j-1)+2, end=' ')
    for j in range(i+1):
        print((i-j)+1, end=' ')

    print() #DONE



