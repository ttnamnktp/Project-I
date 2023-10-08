SoDien = int(input())


def GiaDienCu(SoDien):
    if SoDien <= 50:
        return SoDien * 1.728 * 1.1
    elif SoDien <= 100:
        return (50 * 1.728 + (SoDien - 50) * 1.786) * 1.1
    elif SoDien <= 200:
        return ( 50 * 1.728 + 50 * 1.786 + (SoDien - 100) * 2.074 ) * 1.1
    elif SoDien <= 300:
        return (50 * 1.728 + 50 * 1.786 + 100 * 2.074 + (SoDien - 200) * 2.612 ) * 1.1
    elif SoDien <= 400:
        return (50 * 1.728 + 50 * 1.786 + 100 * 2.074 + 100 * 2.612 + (SoDien - 300) * 2.919 ) * 1.1
    else:
        return (50 * 1.728 + 50 * 1.786 + 100 * 2.074 + 100 * 2.612 + 100 * 2.919 + (SoDien - 400) * 3.015) * 1.1


def GiaDienMoi(SoDien):
    if SoDien <= 100:
        return SoDien * 1.728 * 1.1
    elif SoDien <= 200:
        return (100 * 1.728 + (SoDien - 100) * 2.074 ) * 1.1
    elif SoDien <= 400:
        return (100 * 1.728 + 100 * 2.074 + (SoDien - 200) * 2.612 ) * 1.1
    elif SoDien <= 700:
        return (100 * 1.728 + 100 * 2.074 + 200 * 2.612 + (SoDien - 400) * 3.111) * 1.1
    else:
        return (100 * 1.728 + 100 * 2.074 + 200 * 2.612 + 300 * 3.111 + (SoDien - 700) * 3.457) * 1.1

chenhLech = (GiaDienMoi(SoDien) - GiaDienCu(SoDien))*1000
print(f"{chenhLech:.2f}")
