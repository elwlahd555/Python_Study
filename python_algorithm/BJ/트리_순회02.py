class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def DFS(node):
    global preAnswer
    preAnswer += node.item
    if node.left != '.':
        DFS(tree[node.left])
    global inAnswer
    inAnswer += node.item
    if node.right != '.':
        DFS(tree[node.right])
    global postAnswer
    postAnswer += node.item


if __name__ == "__main__":

    N = int(input())
    tree = {}
    preAnswer = ""
    inAnswer = ""
    postAnswer = ""
    for _ in range(N):
        node, left, right = map(str, input().split())
        tree[node] = Node(item=node, left=left, right=right)

    DFS(tree['A'])
    print(preAnswer)
    print(inAnswer)
    print(postAnswer)
