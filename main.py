import os
import sys


def print_tree(path: str, posit: list, icon_mode: int):
    contain = []
    for i in os.scandir(path):
        contain.append(i)

    for node in contain:
        head = [" ┃" if i else "  " for i in posit]
        head.append(" ┗ " if node == contain[-1] else " ┣ ",)
        if icon_mode is 1:
            head.append("\N{file folder} " if node.is_dir() else "\N{scroll} ")

        print(*head, node.name, sep="")

        if node.is_dir():
            print_tree(node.path, posit + [contain[-1] != node], icon_mode)


if __name__ == '__main__':
    base_path, mode = "", 0

    if len(sys.argv) is 3:
        base_path, mode = sys.argv[1:3]
    else:
        base_path = input("원하는 경로를 입력하세요 : ")
        mode = input("원하는 모드를 입력하세요 (0= 아이콘없이, 1= 심플아이콘, 2= 다양한아이콘(html) : ")

    base_head = "\N{package} " if mode in '12' else "",
    base_name = base_path.split("\\")[-1]
    print(base_head, base_name, sep="")

    print_tree(base_path, [], int(mode))
