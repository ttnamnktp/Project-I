def backtrack(n, M, current_sum=0, current_array=[]):
    if n == 0:
        if current_sum == M:
            for i in range(len(current_array)):
                print(current_array[i], end=' ')
            print('')
        return
    for i in range(1, M - current_sum + 1):
        backtrack(n - 1, M, current_sum + i, current_array + [i])


def main():
    Input = input().split()
    M = int(Input[1])
    n = int(Input[0])
    backtrack(n, M)


if __name__ == "__main__":
    main()
