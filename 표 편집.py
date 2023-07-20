class Node:
    def __init__(self):
        self.up = None
        self.down = None


def solution(n, k, cmds):
    answer = ['O'] * n
    # linked list 처럼 구현..?

    deletedQueue = []  # 스택으로 사용 [(now, dic[now])]
    dic = {}

    for i in range(n):
        node = Node()

        if i == 0:
            node.down = i + 1
        elif i == n-1:
            node.up = i - 1
        else:
            node.up = i - 1
            node.down = i + 1
        dic[i] = node

    now = k

    for cmd in cmds:
        if cmd[0] == 'Z':
            idx, q = deletedQueue.pop()
            # print("q, node", idx, q)
            answer[idx] = 'O'  # 복구
            u = dic[idx].up
            d = dic[idx].down

            if u == None:
                dic[d].up = idx
            elif d == None:
                dic[u].down = idx
            else:
                dic[u].down = idx
                dic[d].up = idx

        elif cmd[0] == 'C':
            answer[now] = 'X'
            if dic[now].down == None:  # 끝이라면 바로 윗행을 선택
                deletedQueue.append((now, dic[now]))

                d = dic[now].down  # 현재의 down
                u = dic[now].up  # 현재의 up

                dic[u].down = None
                now = u  # 커서 업데이트

            elif dic[now].up == None:
                deletedQueue.append((now, dic[now]))

                d = dic[now].down  # 현재의 down
                u = dic[now].up  # 현재의 up

                dic[d].up = None
                now = d

            else:
                deletedQueue.append((now, dic[now]))  # 삭제 목록에 넣어주고 연결 끊어주기

                d = dic[now].down  # 현재의 down
                u = dic[now].up  # 현재의 up

                dic[u].down = d
                dic[d].up = u
                now = d

        elif cmd[0] == 'U':
            x = int(cmd.split(' ')[1])
            for _ in range(x):
                now = dic[now].up
        elif cmd[0] == 'D':
            x = int(cmd.split(' ')[1])
            for i in range(x):
                now = dic[now].down

    # for i in range(n):
    #     print(i, dic[i].up, dic[i].down)

    return ''.join(answer)
