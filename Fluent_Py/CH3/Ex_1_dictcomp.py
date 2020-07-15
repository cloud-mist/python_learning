# the use of dictcomp to buid two dict from the same list of tuples
DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'USA'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]
# a list of pairs can be used directly with the dict constructor

country_code = {country: code  for code, country in DIAL_CODES}
print(country_code)
# {'China': 86, 'India': 91, 'USA': 1, 'Indonesia': 62, 'Brazil': 55, 
# 'Pakistan': 92, 'Bangladesh': 880, 'Nigeria': 234, 'Russia': 7, 'Japan': 81}

code2 = {code: country.upper() for country, code in country_code.items() 
         if code < 66}
print(code2)    # {1: 'USA', 62: 'INDONESIA', 55: 'BRAZIL', 7: 'RUSSIA'}