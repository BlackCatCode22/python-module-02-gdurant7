def computegrade(score):
    try:
        score = float(input('score: '))
        if score < 0 or score > 1:
            raise ValueError
    except:
        print('Error, please enter number between 0 and 1.')
        exit()

    grade = 'F'

    if score >= 0.9:
        grade= 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'

    print('Grade:', grade)

computegrade(80)