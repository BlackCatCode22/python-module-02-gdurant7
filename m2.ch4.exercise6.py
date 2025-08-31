def computepay(hours, rate):
    try:
        hours = float(input('Hours worked?'))
        rate = float(input('Rate worked?'))
    except ValueError:
        print('Error, please enter a number.')
        exit()
    if (hours<=40):
        print('Pay:', hours*rate)
    else:
        print('Pay:', (40*rate)+((hours-40)*(rate*1.5)))

computepay(40, 'D')


