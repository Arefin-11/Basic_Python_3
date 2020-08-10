"""Sort the continent name according to the number of country's name having 'a' in the name"""

"""Continent name with some of its countries"""
continents = {"Asia":["Bangladesh","China","India","Pakistan"],
           "Africa":["South Africa","Kenya","Zimbabwe","Egypt"],
           "North America":["Canada","United States","Mexico"],
           "Europe":["France","Portugal","Spain","Germany"]}

"""Finding the number of countries having 'a' in their name"""
def nt_a(names):
    ct=0
    for name in names:
        if 'a' in name.lower():
            ct+=1
    return ct

"""function of the key parameter"""
def num_country_a(continent):
    countries=continents[continent]
    return nt_a(countries)

print(sorted(continents,key=num_country_a))
print(".........Now with lambda function method........")
print(sorted(continents,key=lambda continent:nt_a(continents[continent])))