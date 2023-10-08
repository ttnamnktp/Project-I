import queue


def main():
    q = queue.Queue()
    pop_array = []
    while True:
        Input = input().split()
        if Input[0] == "#":
            break
        elif Input[0] == "PUSH":
            q.put(Input[1])
        elif Input[0] == "POP":
            if q.empty() is True:
                item = "NULL"
                pop_array.append(item)
            else:
                item = q.get()
                pop_array.append(item)
    for item in pop_array:
        print(item)


if __name__ == "__main__":
    main()
