tuples2 = ("Apple",90,"Orange",89,56)
tuples3 = ("sam", "dana", 94, 63)
for elements in tuples3:
    print(elements)

person = {
    'name': 'Spock',
    'age': 20,
    'married': False,
    'positions': ['Lieutenant', 'Captain', 'Commander'],
}

# %%
person['age']
for key in person:
    print(key)
    print(f"The keys and values of this list would be ", person[key])
# %%


hobbies = "\n\n1.\tsinging\n2.\tdancing\n3.\tcoding"
print(hobbies)
