# Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['s', 'm', 'l']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)  # !! arranged by color, then size.
#result [('black', 's'), ('black', 'm'), ('black', 'l'), ('white', 's'), ('white', 'm'), ('white', 'l')]

for color in colors:
    for size in sizes:
        print((color, size))
'''
RESULT:
('black', 's')
('black', 'm')
('black', 'l')
('white', 's')
('white', 'm')
('white', 'l')
'''

tshirts2 = [(color, size) for size in sizes
                          for color in colors]
print(tshirts2)     # arranged by size, then color.
# [('black', 's'), ('white', 's'), ('black', 'm'), ('white', 'm'), ('black', 'l'), ('white', 'l')]


