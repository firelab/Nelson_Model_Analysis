import csv

#BLMM8, Lat - 46.82073, Lon - -114.10089
fires = []
filename_in = 'modis_2021_United_States.csv'
filename_out = 'modis_2021_Blue_Mountain.csv'
header = ['Lat', 'Lon', 'Date']

with open(filename_in, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    next(datareader)
    for row in datareader:
        lat = float(row[0])
        lon = float(row[1])
        date = row[5]
        # checks a 69 by 55 mile square for fires 
        if (lat > 45.82073 and lat < 47.82073) and (lon > -115.10089 and lon < -113.10089):
            out = (lat, lon, date)
            fires.append(out)

        
with open(filename_out, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in fires:
        writer.writerow(row)
    f.close()
