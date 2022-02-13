from unicodedata import name


# """
# © https://sudipghimire.com.np

# Dictionary Exercises

# Please read the note carefully and try to solve the problem below:

# """

# """
# 1. Create a dictionary of a person that contains key value pair of
#     - name: str
#     - age: int
#     - profession: str
#     - married: bool

#     a. print the value of 'name' from the dictionary
#     b. add the age of the dictionary be 10 and print the dictionary items in formatted string
#         Eg: {name} will be {new_age} at 2031 AD.
#     c. Try getting the value of 'employed' from the dictionary.
#         - If exception occurs, note it and check what the excption says.
#     d. try `get()` method instead of large brackets [] in the previous question (1.c)
#     e. try `get()` method with second parameter: False and see what is printed.
#         Eg: person.get('employed', False)
# """
# # Answers:

# a_person = { 
#     'name': 'diva',
#     'age': '200',
#     'profession': 'woost',
#     'married': True
# }
# # 1.a
# print(f'The name of the person is', a_person['name'],'.')
# # 1.b
# a_person['age'] = 10
# print(f'The new age of', a_person['name'], 'is', a_person['age'],'.' )
# # 1.c
# print(a_person['employeed']) #ANS = KeyError: 'employeed'
# # 1.d
# print(a_person.get('employeed'))#ANS = NONE
# # 1.e
# print(a_person.get('employed', True))

# """
# 2. create a dictionary <car> with 3 keys and values (brand, model, price).
#     a. add a new key 'engine' and set some random value in car.
#     b. add 3 more dictionary keys with `update` method. (color, no_of_seats, transmission).
#     c. remove the key 'color' from the dictionary.
#     d. try using `popitem()` method in the dictionary and see what changes in dictionary
#     e. use for loop to iterate through all keys from a dictionary.
#     f. use for loop to iterate through all keys from a dictionary using `keys()` method.
#     g. use for loop to iterate through all values from a dictionary using `values()` method.
#     h. use for loop to iterate through all keys, values from a dictionary using `items()` method.
# """
# Answers:
car = {
    'brand': 'suzuki',
    'model': 'yeah yeah',
    'price': 'needbase'
}
# 2.a
car.update({'engine': 'we'})
print(f'The new car details are:{car}')
# 2.b
car.update({'color': 'grenn', 'no_of_seats': 44, 'transmission':  'idk'})
print(f'The updated car details {car}.')
# 2.c
print(car.pop('color'))
# 2.d
print(car.popitem())
# 2.e
for key in car:
    print(f'These are the keys: {key}.')
# 2.f
print(car.keys())
# 2.g
for value in car.values():
    print(value)

# 2.h
for keys, values in car.items():
    print(keys, values)


"""
3. Create a nested dictionary named yoda with following properties
    - age: 910
    - species: Yodas
    - gender: male
    - affilitions: ['Jedi', 'Galactic Republic']
    - master: <dict>
        - name: Qui-Gon Jinn
        - age: 48
        - affiliations: ['Jedi', 'Galactic Republic', 'Heliost Clan']
        - master: <dict>
            - name: Dooku
            - age: 83
            - affiliations: ['House Serenno', 'Jedi']

    a. print the value of the first affiliation of `Dooku` from the dictionary
    b. add new affiliation 'Sith' to Dooku
    c. pop the key 'master' from the dictionary

"""
# Answer 3
yoda = {
    'age': 910,
    'species': 'Yodas',
    'gender': 'male',
    'affilitions': ['Jedi', 'Galactic Republic'],
    'master': {
        'name': 'Qui-Gon Jinn',
        'age': 48,
        'affiliations': ['Jedi', 'Galactic Republic', 'Heliost Clan'],
        'master': {
            'name': 'Dooku',
            'age': 83,
            'affiliations': ['House Serenno', 'Jedi']
        }}
}   


   
# 3.a. print the value of the first affiliation of `Dooku` from the dictionary
print(yoda['master']['master']['affiliations'][0])

# 3.b. add new affiliation 'Sith' to Dooku
add = 'Sith'
print(yoda['master']['master']['affiliations'].append(add))
print(yoda)
# 3.c. pop the key 'master' from the dictionary
print(yoda.pop('master'))
