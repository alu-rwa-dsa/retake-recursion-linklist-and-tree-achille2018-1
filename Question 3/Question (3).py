# AUTHOR : ACHILLE TANWOUO SAGANG
# QUESTION3


class BinarySearchTree:

    def __init__(self, root=None):
        self.root = [None] * 100
        print(self.root)
        if root is not None and len(self.root) != 0:
            self.root[0] = root
        else:
            # raise ValueError('The root already exist')
            print('The root already exist')

    def insert_node_left(self, parent, node):
        """ """
        if self.root[parent] is not None:
            self.root[(parent * 2) + 1] = node
            print("successfuly added a node at index {}".format((parent * 2) + 1))
        else:
            print("Could not add a node a that position because parent doesn't exist")

    def inser_node_right(self, parent, node):
        if self.root[parent] is not None:
            self.root[(parent * 2) + 2] = node
            print("successfuly added a node at index {}".format((parent * 2) + 2))
        else:
            print("Could not add a node a that position because parent doesn't exist")

    def find_data(self, index):
        if self.root[index] is not None:
            print(f"Node found at index {index} found")
            return self.root[index]
        else:
            print(f"The node at index {index} is not found")

    def remove_node(self, index):
        if self.root[index] is not None:
            self.root[index] = None
            print("Node removed")
        else:
            print(f"The node at index {index} is not found")

    def print_tree(self):
        for i in range(10):
            if self.root[i] != None:
                print(self.root[i], end="")
            else:
                print("-", end="")
        print()
#
#
# # Driver Code
binary = BinarySearchTree('A')
binary.insert_node_left(0, 'B')
binary.inser_node_right(0, 'C')
binary.insert_node_left(1, 'D')
binary.inser_node_right(1, 'E')
binary.inser_node_right(2, 'F')
binary.print_tree()
node = binary.find_data(2)
print(f'node found has value {node}')
binary.remove_node(2)
binary.print_tree()