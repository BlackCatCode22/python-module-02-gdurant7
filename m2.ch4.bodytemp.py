temp = float(input('Temperature: '))
hours = input('Hours: ')
deathTime = float((37-temp)/.78)
if (temp <= 0 or deathTime >= 80 or hours > 80 or deathTime + hours > 80):
    print ('Body temperature will not change')
elif (temp < 27.64 or 12 < deathTime < 82):
    print ('Hours since death is: ', 37-temp / .39 + 12)
    print ('Body temperature in ', hours, ' hours will be: ', temp - (hours*.39))
    print ('Body temperature in ', hours+1, 'hours will be: ', temp + ((hours+1)*.39))
else:
    print ('hours since death is: ', deathTime)
    print ('Body temperature in ', hours, ' hours will be: ', temp - (hours*.78))
    print ('Body temperature in ', hours+1, 'hours will be: ', temp + ((hours+1)*.78))
