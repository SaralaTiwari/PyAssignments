"""
© https://sudipghimire.com.np

Lists Exercises

Please read the note carefully and try to solve the problem below:

"""

"""
1. Write a program to create an empty list named `my_list` and

    a. add numbers 5 and 9 to the list using `append()` method

    b. ask the user to input any number in the console and add the number to the list.
        - you can use int() to change the type from string to integer if you want.

    c. create another list `more_items` with 3 items on it and extend the list `my_list`
        using `extend` method.

    d. now find the length of the list and print the length of list describing it in a sentence.
        - you can always use string formatting for better outputs.

    e. now remove the second item using `pop()` method and see if the item exists in the list
        - you can print the list before and after using the `pop()` method.
"""
"""
# answer 1
my_list = [] #DONE

# a
my_list.append(5)
my_list.append(9)
print(my_list) #DONE


# b
user_input = input("Pick a number! ") #DONE
my_list.append(user_input) 
print(my_list) #DONE BUT WHY DOES THE NUMBER PICKED BY USER COME INSIDE ''?

# c
more_items = [2, 22, 42]
my_list.extend(more_items)
print(my_list) #DONE

# d
print("There are ", my_list.__len__(), "elements in this list.") #DONE

# e

my_list.pop(2)
print(my_list) #DONE  """
"""
2. Write a program to add 5 different wild animals to a list named `wild`.
    - tiger, lion, deer, bear, zebra

    a. sort them in ascending using the `sort()` method.
    b. reverse the list using the `reverse()` method.
    c. now add 3 more animals to the list `wild`.  ['leopard', 'elephant', 'rhino']
    d. find the position of `leopard` using the `index()` method and remove  it using `the pop()` method.
        - pop should have the index value returned using the `index()` method.
        - do not hard-code the position of leopard by manually counting it from the list.
        - check whether the leopard is removed from the list or not by `index()` method again.
          if the value error occurs, you have successfully removed it from the list.
          otherwise, try to do it again.
        - you can then comment the line that gives exception to continue to the next question.
    e. Now add `leopard` agin in the index 2 using `insert()` method.
    f. Again, remove `rhino` from the list using remove() method.

    note: you can print the values of list after each successful operations to see what is being changed.
"""
# answer 2
"""
wild = ["tiger", "lion", "deer", "bear", "zebra"]
# a
wild.sort()
print(wild) #DONE

# b
print(wild.reverse()) #WHY DOES THE RESULT COME AS 'NONE' ON THIS CODE?
wild.reverse()
print(wild) #DONE

# c
more_animals = ("leopard", "elephant", "rhino")
wild.extend(more_animals)
print(wild) #DONE

# d
print(wild.index("leopard"))
print(wild.pop(5))
#print(wild.index("leopard")) #DONE

# e

wild.insert(2, "leopard")
print(wild) #DONE

# f
wild.remove("rhino")
print(wild) #DONE
"""
"""
3. Try creating a multi-dimensional list or nested list `multi` of different numbers.
    eg: [[12,52,37],[46,51,16],[17,82,39]]

    a. access the number 51 from the list.
    b. access the number 82 using the negative indices.
    c. append another list [40, 61, 10] inside the list `multi`.
        the final list should be: [[12,52,37],[46,51,16],[17,82,39],[40, 61, 10]]
    d. use foreach in the list `multi` to print each list item to the console.
        - Bonus: try using nested foreach to access each item inside of the inner list
    e. finally clear the list `multi` using the `clear()` method and verify if the list is empty or not
"""
# answer 3

multi = [[12,52,37],[46,51,16],[17,82,39]]
print(multi) #DONE 
# a

print(multi[1][1]) #DONE
# b

print(multi[-1][-2]) #DONE
# c

multi.append([40, 61, 10])
print(multi) # AGAIN, WHY DOES IT RETURN NONE WHEN I PRINT IN THE FIRST LINE OF CODE?
# d

#for each item in multi:  #DON'T KNOW HOW TO DO THIS

# e

multi.clear()
print(multi)