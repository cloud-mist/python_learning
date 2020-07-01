# Cartesian product in a generator expression
colors = ['black', 'white']
sizes = ['s', 'm', 'l']
for tshirt in ('%s %s' % (c, s) for c in colors 
        for s in sizes):
    print(tshirt)
'''
black s
black m
black l
white s
white m
white l
'''
