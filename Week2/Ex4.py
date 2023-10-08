def printArray(n, arr):
    for i in range(n):
        print(arr[i], end=' ')
    print('')


def check(v, k, arr):
    for i in range(k):
        if arr[i] == v:
            return False
    return True


def backtrack(n, arr, k):
    for v in range(1, n+1):
        if (check(v, k, arr)) is True:
            arr[k] = v
            if k == n - 1:
                printArray(n, arr)
            else:
                backtrack(n, arr, k + 1)


def main():
    n = int(input())
    arr = [0] * n
    backtrack(n, arr, 0)


if __name__ == "__main__":
    main()
