recus = [0] * 1000000

def power(x, y):
    if y == 0:
        recus[y] = 1
        return recus[y]
    if recus[y] != 0:
        return recus[y]
    recus[y] = power(x, y - 1) * x % 1000
    return recus[y]

def hashfunction(string):
    length = len(string)
    sum_val = 0

    for i in range(length):
        coe = power(7, length - 1 - i)
        sum_val += ord(string[i]) * coe

    return sum_val % 1000

class Node:
    def __init__(self):
        self.string = ""
        self.next = None

class HashTable:
    def __init__(self):
        self.buckets = [None] * 1000

def initHashTable(ht):
    for i in range(1000):
        ht.buckets[i] = None

def insert(string, ht):
    key = hashfunction(string)
    new_node = Node()
    new_node.string = string
    new_node.next = ht.buckets[key]
    ht.buckets[key] = new_node

def find(string, ht):
    key = hashfunction(string)
    temp_node = ht.buckets[key]
    while temp_node is not None:
        if temp_node.string == string:
            return 1
        temp_node = temp_node.next
    return 0

if __name__ == "__main__":
    string = ""
    ht = HashTable()
    initHashTable(ht)

    while string != "*":
        string = input()
        insert(string, ht)

    choice = ""
    step = []
    i = 0

    while choice != "***":
        choice = input().split()
        if choice[0] == "insert":
            test = choice[1]
            if find(test, ht) == 0:
                insert(test, ht)
                step.append(1)
                i += 1
            else:
                step.append(0)
                i += 1
        elif choice[0] == "find":
            test = choice[1]
            if find(test, ht) == 1:
                step.append(1)
                i += 1
            else:
                step.append(0)
                i += 1

    print(step)
