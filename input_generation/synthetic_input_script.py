
# rain for 2 weeks (336 hours)
# dry for 1 week (168 hours)
# rain for 2 weeks (336 hours)
# Total = 840

i = 1
year = 2022
month = 1
date = 1
hour = 0
precip = 0


with open('input.txt', 'w') as f:
        while i <= 840: 
            print(str(year) +' '+ str(month)+ ' '+str(date)+ ' '+ str(hour)+ ' '+ str(precip))
            if i == 1:
                f.write(str(year)+' '+str(month)+' '+str(date)+' '+str(hour)+' 01 00 0 21 .01 200 '+str(precip)+' 19 .01 .01 \n')
            elif i < 337 and i > 1:
                f.write(str(year)+' '+str(month)+' '+str(date)+' '+str(hour)+' 01 00 0 21 .01 200 '+str(precip)+ '\n')
            elif i < 505 and i > 336:
                f.write(str(year)+' '+str(month)+' '+str(date)+' '+str(hour)+' 01 00 0 21 .9 200 '+str(precip)+ '\n')
                precip = precip+1
            elif i > 504:
                f.write(str(year)+' '+str(month)+' '+str(date)+' '+str(hour)+' 01 00 0 21 .01 200 '+str(precip)+ '\n')
            i = i + 1
            hour = hour + 1
            if hour > 23:
                hour = 0
                date = date +1
            if date > 30: 
                month = month + 1
                date = 1