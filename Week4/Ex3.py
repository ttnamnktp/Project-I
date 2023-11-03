n = int(input())  # Đọc số lượng phần tử
A = list(map(int, input().split()))  # Đọc dãy số nguyên

# Sử dụng một tập hỗ trợ để theo dõi các số đã xuất hiện
appearedNumbers = set()
output = []

if __name__ == "__main__":
    for i in range(n):
        if A[i] in appearedNumbers:
            output.append(1)
        else:
            output.append(0)
        appearedNumbers.add(A[i])

    # In ra kết quả
    for _ in output:
        print(_)
