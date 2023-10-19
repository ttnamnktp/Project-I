# tim uoc chung nho nhat
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# Luon do binh 1 vao binh 2
def pouringProc(firstJugCap, secondJugCap, c):
    # Khoi tao buoc dau
    stepsDetails = []
    step = 0
    firstJug = firstJugCap
    secondJug = 0

    while firstJug != c and secondJug != c:
        # tim luong nuoc toi da co the do tu 1st jug sang 2nd jug
        pouringWater = min(firstJug, secondJugCap - secondJug)

        # pouring
        firstJug -= pouringWater
        secondJug += pouringWater
        step += 1

        # lam day binh thu nhat neu no rong
        if firstJug == 0:
            firstJug = firstJugCap
            step += 1

        # lam rong binh thu hai neu no day
        if secondJug == secondJugCap:
            secondJug = 0
            step += 1

    return step


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    if c % gcd(a, b) != 0:
        print(-1)
    else:
        print(min(pouringProc(a, b, c), pouringProc(b, a, c)))
