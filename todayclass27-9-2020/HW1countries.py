def convert_countries_to_upper(countries):
    upper_countries = []
    for country in countries:
        upper_countries.append(country.upper())
        
    return upper_countries

countries = [ "india" , "england" , "usa" , "albania" , "afghanistan" ]
upper_countries = convert_countries_to_upper(countries)
print(upper_countries)


