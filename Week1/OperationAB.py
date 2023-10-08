import math

Numbers = input().split()
A = int(Numbers[0])
B = int(Numbers[1])
C = int(Numbers[2])
Delta = B**2 - 4*A*C

if Delta > 0:
    x1 = (-B - math.sqrt(Delta)) / 2 / A
    x2 = (-B + math.sqrt(Delta)) / 2 / A
    print(f"{x1:.2f} {x2:.2f}")
elif Delta == 0:
    x = -B / 2 / A
    print(f"{x:.2f}")
else:
    print("NO SOLUTION")