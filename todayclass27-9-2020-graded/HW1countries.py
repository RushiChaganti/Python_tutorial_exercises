# All ok, but check for the string type before applying upper. 

def convert_countries_to_upper(countries):
    upper_countries = []
    for country in countries:
        if type(country) == str:
            upper_countries.append(country.upper())
    return upper_countries

countries = [ "india" , "england" , "usa" , "albania" , "afghanistan", 2 ]
upper_countries = convert_countries_to_upper(countries)
print(upper_countries)


