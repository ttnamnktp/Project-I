stack = []
pop_items = []

def main():
    while True:
        command = input().strip().split()
        if command[0] == "PUSH":
            stack.append(int(command[1]))
        elif command[0] == "POP":
            if len(stack) == 0:
                item = "NULL"
                pop_items.append(item)
            else:
                item = stack.pop()
                pop_items.append(item)
        elif command[0] == '#':
            break
    for item in pop_items:
        print(item)


if __name__ == "__main__":
    main()
