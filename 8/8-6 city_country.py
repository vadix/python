def city_country(city, country):
    phrase = "\'" + city.title() + ", " + country.title() + "\'"
    return phrase
test = city_country("minsk", "belarus")
print(test)