import os


def print_emojis():
    print("\N{package}")
    print("\N{file folder}")
    print("\N{open file folder}")
    print("\N{page facing up}")
    print("\N{scroll}")
    print("\N{memo}")


def test_print_tree(path: str, posit: list):
    contain = []
    for i in os.scandir(path):
        contain.append(i)
    for node in contain:
        print(*["┃" if i else " " for i in posit],
              "┗" if node == contain[-1] else "┣",
              node.name, posit)
        if node.is_dir():
            test_print_tree(node.path, posit + [contain[-1] != node])


if __name__ == '__main__':
    test_print_tree(r"C:\Users\user\Documents\print_folder_as_tree\test_folder", [])
