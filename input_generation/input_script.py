from urllib.request import urlopen
import json
import math
import pandas as pd
import csv

 # format - YYYYMMDDHHMM
def create_input_file(start, end):

    #BLMM8, Lat - 46.82073, Lon - -114.10089
    with urlopen('https://api.synopticdata.com/v2/stations/timeseries?&token=6f15765b51fa4a69b6787cc3693da767&start='+str(start)+'&end='+str(end)+'&units=metric&network=2&stid=BLMM8&obtimezone=local&vars=air_temp,relative_humidity,solar_radiation,precip_accum,fuel_temp,fuel_moisture') as response:
        weather = json.load(response)
    df= pd.json_normalize(weather['STATION'])
    date_time = df['OBSERVATIONS.date_time'] #YYYY-MM-DDTHH:MM:SS
    air_temp = df['OBSERVATIONS.air_temp_set_1'] #Celsius
    humidity = df['OBSERVATIONS.relative_humidity_set_1'] # %
    fuel_temp = df['OBSERVATIONS.fuel_temp_set_1'] #Celsius
    start_fuel_temp = int(fuel_temp[0][0]) 
    fuel_moisture = df['OBSERVATIONS.fuel_moisture_set_1'] #gm
    start_fuel_moisture = int(fuel_moisture[0][0])/1000
    solar_rad = df['OBSERVATIONS.solar_radiation_set_1'] #W/m**2
    precip = df['OBSERVATIONS.precip_accum_set_1'] #Millimeters

    # This will need to change
    surf_humidity = humidity[0][0]/ 100


    # formatting year, month, date, hour, minute and second from date_time
    year = []
    month = []
    date = [] 
    hour = []
    minute = []
    second = []
    for i in date_time[0]:
        year.append(i[0:4])
        month.append(i[5:7])
        date.append(i[8:10])
        hour.append(i[11:13])
        minute.append(i[14:16])
        second.append(i[17:19])
    
    # formatting precipitation 
    precip_out = []
    for i in precip[0]:
        i_2 = i
        if i is None:
            i_2 = 0
        precip_cm = i_2/10
        precip_out.append(precip_cm)

    precip_diff = []
    previous = 0
    for i in range(len(precip[0])):
        if i == 0:
            precip_diff.append(0)
            previous = precip[0][i]
        else:
            if precip[0][i] is None:
                precip[0][i] = previous
            out = precip[0][i] - previous
            if out > 5:
                print(previous)
                print(precip[0][i])
                print(i)
            previous = precip[0][i]
            if out < 0:
                precip_diff.append(0)
            else:
                precip_diff.append(out)

    # formatting solar rad
    NaN = []
    solar_out = []
    for i in range(len(solar_rad[0])):
        if solar_rad[0][i] == None:
            NaN.append(i)
            solar_out.append(None)
        else:
            solar_out.append(solar_rad[0][i])

    
    # Calculating humidity in g/g (not sure if this is right)
    humidity_out = []
    for i in range(len(humidity[0])):
        try:
            rh = humidity[0][i]/100
            humidity_out.append(rh)
        except:
            rh = humidity[0][i]
            humidity_out.append(None)
            NaN.append(i)
    
    with open('input.txt', 'w') as f:
        for i in range(len(humidity_out)):
            if i in NaN:
                print(i) 
            else:
                if i == 0:
                    f.write(str(year[i])+' '+str(month[i])+' '+str(date[i])+' '+str(hour[i])+' '+str(minute[i])+' '+str(second[i])+' 0 '
                        +str(air_temp[0][i])+' '+str(humidity_out[i])+ ' '+str(solar_rad[0][i])+' '+str(precip_out[i])+' '
                        +str(start_fuel_temp)+' '+str(surf_humidity)+' '+str(start_fuel_moisture)+' \n')
                else:
                    f.write(str(year[i])+' '+str(month[i])+' '+str(date[i])+' '+str(hour[i])+' '+str(minute[i])+' '+str(second[i])+' 0 '
                        +str(air_temp[0][i])+' '+str(humidity_out[i])+ ' '+str(solar_rad[0][i])+' '+str(precip_out[i])+' \n')

    with open('precip.csv', 'w') as file:
        writer = csv.writer(file)
        for i in range(len(precip_diff)):
            if i in NaN:
                print(i)
            else:
                writer.writerow([precip_diff[i]/10])
        

create_input_file(202108010000, 202201010000)