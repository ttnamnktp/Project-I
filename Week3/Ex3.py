stack = []

def main():
    answer = 0
    Input = input()
    for each in Input:
        if each == '(' or each == '[' or each == '{':
            stack.append(each)
        elif each == ')' or each == ']' or each == '}':
            if (len(stack) == 0):
                answer = 0
                print(answer)
                return
            item = stack.pop()
            if (each == ')' and item == '(') or (each == ']' and item == '[') or (each == '}' and item == '{'):
                continue
            else:
                answer = 0
                print(answer)
                return
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    print(answer)


if __name__ == "__main__":
    main()
