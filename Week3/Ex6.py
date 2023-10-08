class Member:
    def __init__(self, name):
        self.name = name
        self.children = []


def family_tree_dict(family_tree, parent, child):
    if parent not in family_tree:
        family_tree[parent] = Member(parent)
    if child not in family_tree:
        family_tree[child] = Member(child)
    family_tree[parent].children.append(child)
    return family_tree


def count_child(family_tree, parent):
    count = 0
    for child in family_tree[parent].children:
        count = count + 1 + count_child(family_tree, child)
    return count


def count_generation(family_tree, parent):
    generation = 0
    for child in family_tree[parent].children:
        generation = max(generation, 1 + count_generation(family_tree, child))
    return generation


if __name__ == "__main__":
    family = {}
    while True:
        command = input().split()
        if command[0] == "***":
            break
        else:
            child = command[0]
            parent = command[1]
            family = family_tree_dict(family, parent, child)
    output_command = []

    while True:
        command = input().split()
        if command[0] == "***":
            break
        elif command[0] == "descendants":
            output = count_child(family, command[1])
            output_command.append(output)
        elif command[0] == "generation":
            output = count_generation(family, command[1])
            output_command.append(output)
        else:
            continue
    for _ in output_command:
        print(_)
