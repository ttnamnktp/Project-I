N = int(input())
Numbers = input().split()

Odd = 0
Even = 0

for numbers in Numbers:
    if int(numbers) % 2 == 0:
        Even += 1
    else:
        Odd += 1

print(f"{Odd} {Even}")

