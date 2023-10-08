# Function to calculate the factorial of a number
MOD = 7 + 10 ** 9


def Combin(C, k, n):
    if n < k:
        return 0
    if k == n or k == 0:
        return 1
    if C[k][n] != -1:
        return C[k][n]
    C[k][n] = (Combin(C, k - 1, n - 1) + Combin(C, k, n - 1)) % MOD
    return C[k][n]


def main():
    k, n = map(int, input().split())
    C = [[-1 for _ in range(n + 1)] for _ in range(k + 1)]
    print(Combin(C, k, n))


if __name__ == "__main__":
    main()
