import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.data = None
        self.index = None


def preOrder(root, arr):
    if root == None:
        return arr

    arr.append(root.index)
    preOrder(root.left, arr)
    preOrder(root.right, arr)

    return arr


def postOrder(root, arr):
    if root == None:
        return arr

    postOrder(root.left, arr)
    postOrder(root.right, arr)
    arr.append(root.index)

    return arr


def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    # 더 높은 레벨(부모)가 앞으로 오도록 정렬
    nodeinfo = sorted(nodeinfo, key=lambda x: x[1], reverse=True)

    answer = [[]]
    # x, y -> y는 레벨, x는 위치(값)

    n = len(nodeinfo)
    root = None

    for i in range(n):
        node = Node()
        node.index = nodeinfo[i][2]
        node.data = nodeinfo[i]

        if root == None:
            root = node
        else:
            current = root
            while True:

                if current.data[0] > node.data[0]:  # 내가 더 작음 -> 왼쪽으로 들어가야함
                    if current.left == None:
                        current.left = node
                        node.parent = current
                        break  # 위치를 찾은경우(왼쪽에
                    else:
                        current = current.left  # 현재 위치를 옮겨줌

                else:  # 오른쪽으로 들어가야함
                    if current.right == None:
                        current.right = node
                        node.parent = current
                        break
                    else:
                        current = current.right

    answer = [preOrder(root, []), postOrder(root, [])]
    return answer
