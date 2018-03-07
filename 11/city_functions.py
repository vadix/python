def get_formatted_city(city, country, population=''):
    """Строит отформатированную строку Santiago, Chile."""
    if population:
        formatted_city = city + ', ' + country + ' — population ' + population
    else:
        formatted_city = city + ', ' + country
    return formatted_city.title()