import heapq
from collections import defaultdict


def solution(operations):
    answer = []
    queue = []
    minH = []
    maxH = []

    for operation in operations:
        if operation[0] == "I":
            n = int(operation[2:])
            queue.append(n)
            heapq.heappush(maxH, -n)
            heapq.heappush(minH, n)

        elif operation == "D 1" and queue:
            while True:
                h = -heapq.heappop(maxH)
                # print("최대값", h)
                if h in queue:
                    queue.remove(h)
                    # print("qq", queue)
                    break

        elif operation == "D -1" and queue:
            while True:
                h = heapq.heappop(minH)
                # print("최소값", h)
                if h in queue:
                    queue.remove(h)
                    # print("qqq", queue)
                    break

    # print("queue", queue)
    # print("minH",minH)
    # print("maxH", maxH)
    queue.sort()
    if queue:
        answer = [queue[-1], queue[0]]  # [최대, 최소]
    else:
        answer = [0, 0]

    return answer
