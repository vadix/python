def city_country(city, country):
    phrase = "\'" + city.title() + ", " + country.title() + "\'"
    return phrase
test1 = city_country("kiev", "ukraine")
test2 = city_country("minsk", "belarus")
test3 = city_country("moskow", "russia")
print(test1)
print(test2)
print(test3)