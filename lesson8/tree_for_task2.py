class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node[{self.value}]'

    def walk(self, code, acc):
        if self.left is None:
            code[self.value] = acc or "0"
        else:
            self.left.walk(code, acc + "0")  # пойти в левого потомка, добавив к префиксу "0"
        if self.right is None:
            code[self.value] = acc or "0"
        else:
            self.right.walk(code, acc + "1")  # затем пойти в правого потомка, добавив к префиксу "1"


class Tree:
    def __init__(self):
        self.root = None

    # функция для добавления узла в дерево
    def new_node(self, value):
        return Node(value, None, None)

    # функция для вычисления высоты дерева
    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    # функция для распечатки элементов на определенном уровне дерева
    def print_given_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root, end='')
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)

    # функция для распечатки дерева
    def print_level_order(self, root):
        h = self.height(root)
        i = 1
        while i <= h:
            self.print_given_level(self.root, i)
            print()
            i += 1
        # функция для вычисления ширины дерева

    def get_max_width(self, root):
        max_wdth = 0
        i = 1
        h = self.height(root)
        while i <= h:
            width = self.get_width(root, i)
            if width > max_wdth:
                max_wdth = width
            i += 1

        return max_wdth

    def get_width(self, root, level):
        if root is None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.get_width(root.left, level - 1) + self.get_width(root.right, level - 1)
        self.get_width(root.right, level - 1)

