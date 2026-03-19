from datetime import date
import matplotlib.pyplot as plt
import meteostat as ms

loc = ms.Point(24.264, 120.637, 113)

slists = ms.stations.nearby(loc, limit=2)
below50m = slists[slists['elevation'] <50]

print(below50m)