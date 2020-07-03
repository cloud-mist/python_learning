# tuples used as records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('usa', '31195855'), ('bra', 'ce342567'), ('esp', 'xda20')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country,_ in traveler_ids:
    print(country)
    
'''    
----Result----
bra/ce342567
esp/xda20
usa/31195855
usa
bra
esp
'''