time = input()


def checkTime(time):
    if time[2] != ":":
        return False
    elif time[5] != ":":
        return  False
    Hour = int(time[0]) * 10 + int(time[1])
    Min = int(time[3]) * 10 + int(time[4])
    Sec = int(time[6]) * 10 + int(time[7])
    if Sec > 59:
        return False
    elif Min > 59:
        return False
    elif Hour > 23:
        return False
    return True


if checkTime(time):
    Hour = int(time[0]) * 10 + int(time[1])
    Min = int(time[3]) * 10 + int(time[4])
    Sec = int(time[6]) * 10 + int(time[7])
    print(Hour*3600 + Min*60 + Sec)
else:
    print("INCORRECT")
