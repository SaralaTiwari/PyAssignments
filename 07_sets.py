"""
© https://sudipghimire.com.np

Sets Exercises

Please read the note carefully and try to solve the problem below:

"""

"""
1. Write a program to create two different set of countries
    i.  rich: {'USA', 'China', 'Japan', 'Germany', 'France', 'Australia', 'Italy'}
    ii. europe: {'Germany', 'France', 'England', 'Switzerland', 'Italy', 'Portugal', 'Sweden'}

    Use the Set methods to find out:

    a. countries that are rich but not in Europe
    b. countries that are in Europe but not rich
    c. countries that are both rich and are in Europe
    d. countries that are either rich or in Europe, but not both
    e. all the countries in either of the sets. (Names must be unique)
    f. see if two sets are disjoint or not
    g. now remove the common countries from the `rich` set and check if two sets are disjoint or not.
        - hint: use `difference_update()` method. for more, please refer to python documentation
"""

# answer 1.
rich_country = {'USA', 'China', 'Japan', 'Germany', 'France', 'Australia', 'Italy'}
europian_country = {'Germany', 'France', 'England', 'Switzerland', 'Italy', 'Portugal', 'Sweden'}
# a
rich_non_europian = rich_country.difference(europian_country)
print(f'The countries that are rich but not in Europe are {rich_non_europian}.')
# b
poor_europian = europian_country-rich_country
print(f'The countries that are poor but in Europe are {poor_europian}.')
# c
rich_europian = europian_country-europian_country.difference(rich_country)
print(f'The countries that are rich and in Europe are {rich_europian}.')
# d
rich_only = rich_country.difference(europian_country) 
europian_only = europian_country.difference(rich_country) 
union_ab = rich_only.union(europian_only)
print(union_ab)
# e
print(rich_country.union(europian_country))
# f
print(rich_country.isdisjoint(europian_country))
# g
print(rich_only.isdisjoint(europian_only))
"""
2. Create two more sets
    i.  `asian_rich` and add {'China', 'Japan'} to it.
    ii. `american_rich` and add {'USA', 'Canada'} to it.
   and check whether:

   a. `asian_rich` is a subset of `rich` or not
   b. `rich` is a superset of `asian_rich` or not
   c. `american_rich` is a subset of `rich` or not
"""
# answer 2
asian_rich = {'China', 'Japan'}
american_rich = {'USA', 'Canada'}
# a
print(asian_rich.issubset(rich_country))
# b
print(rich_country.issuperset(asian_rich))
# c
print(american_rich.issubset(rich_country))