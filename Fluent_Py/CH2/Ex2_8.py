# Unpacking nested tuples to access the longitude
metro_areas = [
    ('tokyo', 'jp', 36.933, (35.689, 139.691)),
    ('delhi ncr', 'in', 21.935, (28.613, 77.20)),
    ('mexico', 'mx', 20.142, (19.433, -99.133)),
    ('new york', 'us', 20.104, (40.808, -74.020)),
    ('sao paulo', 'br', 19.649, (-23.547, -46.635)),
]

print('| {:^12} | {:^9} | {:^9}'.format('city.', 'lat.', 'long.'))
fmt = '| {:12} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))


'''         *******Result*******
|    city.     |   lat.    |   long.
| mexico       |   19.4330 |  -99.1330
| new york     |   40.8080 |  -74.0200
| sao paulo    |  -23.5470 |  -46.6350
'''