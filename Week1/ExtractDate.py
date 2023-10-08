date = input()


def checkDate(date):
    if date[4] != '-':
        return False
    elif date[7] != '-':
        return False
    month = int(date[5]) * 10 + int(date[6])
    day = int(date[8]) * 10 + int(date[9])
    if month > 12:
        return False
    elif day > 31:
        return False
    return True

if checkDate(date):
    month = int(date[5]) * 10 + int(date[6])
    day = int(date[8]) * 10 + int(date[9])
    new_date = []
    for i in range(0,4):
        new_date.append(date[i])
    new_date.append(' ')
    new_date.append(str(month))
    new_date.append(' ')
    new_date.append(str(day))
    print(''.join(new_date))
else:
    print('INCORRECT')