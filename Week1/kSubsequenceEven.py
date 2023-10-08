Num = input().split()
N = int(Num[0])
k = int(Num[1])

Array = input().split()

countEven = 0
sumSub = 0

for i in range(0, k):
    sumSub += int(Array[i])
if sumSub % 2 == 0:
    countEven += 1

for i in range(1, N - k + 1):

    sumSub -= int(Array[i - 1])
    sumSub += int(Array[i + k - 1])
    if sumSub % 2 == 0:
        countEven += 1

print(countEven)
