def printArray(n, arr):
    for i in range(n):
        print(arr[i], end='')
    print('')


def backtrack(n, arr, i):
    if i == n:
        printArray(n, arr)
        return

    arr[i] = 0
    backtrack(n, arr, i + 1)
    arr[i] = 1
    backtrack(n, arr, i + 1)


def main():
    n = int(input())
    arr = [0] * n
    backtrack(n, arr, 0)


if __name__ == "__main__":
    main()
