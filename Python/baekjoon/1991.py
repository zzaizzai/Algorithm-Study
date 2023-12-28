
import sys

"https://www.acmicpc.net/problemset?sort=ac_desc&algo=120"
"https://www.acmicpc.net/problem/1991"

sys.stdin = open("1991_tree.txt", "r")

num_nodes = int(input())

nodes_list = []
for i in range(num_nodes):
    nodes_list.append(list(map(str, input().split(" "))))

class Node():

    def __init__(self, value: str) ->None :
        self.value = value
        self.right: Node = None
        self.left: Node = None

def insert(node: Node, value_list: list[str]) -> Node :
    if node is None:
        node_new = Node(value_list[0])
        node_new.left = Node(value_list[1])
        node_new.right = Node(value_list[2])
        return node_new
    
    def search_node(node: Node, value_list: list[str]) -> Node:
        value_target = value_list[0]
        if node is not None:
            if value_target == node.value:
                if value_list[1] != ".":
                    node.left = Node(value_list[1])
                if value_list[2] != ".":
                    node.right = Node(value_list[2])
                return node
            
            search_node(node.left, value_list)
            search_node(node.right, value_list)

        return node

    return search_node(node, value_list)


def preorder(node: Node):
    # Root, Left, Right
    if node is not None:
        print(node.value, end="")

        preorder(node.left)
        preorder(node.right)


def inorder(node: Node):
    # Left, Root, Right 
    if node is not None:
        inorder(node.left)
        print(node.value, end="")
        inorder(node.right)

def postorder(node: Node):
    # Left, Right, Root
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end="")




root = None
for i in range(num_nodes):
    root = insert(root, nodes_list[i])


preorder(root)
print()
inorder(root)
print()
postorder(root)