from datetime import date
import matplotlib.pyplot as plt
import meteostat as ms
"""
    ms.Point( lat , long )  緯度 , 經度
"""
# Specify location and time range
POINT = ms.Point(24.264, 120.637, 113)  # Try with your location
START = date(2025, 1, 1)
END = date(2025, 12, 31)

# Get nearby weather stations
stations = ms.stations.nearby(POINT, limit=5)

# Get daily data & perform interpolation
ts = ms.daily(stations, START, END)
print("-------------- Time Serie ------------")
print( ts )
print("-------------- Time Serie ------------")

# df --> sql server database 存放 ---> power bi
# df --> power bi 做分析 ( df to_csv  --> import power bi)
df = ms.interpolate(ts, POINT).fetch()
df.to_csv(r'C:\Projects\Weather_parser\weather_data.csv', index=True)

print("-------------- Time Serie ------------")
print( df )
print("-------------- Time Serie ------------")
# Plot line chart including average, minimum and maximum temperature
df.plot(y=[ms.Parameter.TEMP, ms.Parameter.TMIN, ms.Parameter.TMAX])
plt.show()