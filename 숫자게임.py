import heapq


def solution(A, B):
    answer = 0
    # A를 정렬함
    # B를 힙에 넣는다
    # 힙에서 꺼낸게 A의 가장앞보다 크면 그대로 진행(이김)
    # 같아도 그대로 진행(승점은x) -> 앞에거랑 같아도 다음거랑 비교해야함
    # A의 가장 앞보다 작으면 (A의 누구도 이길수 없음) A의 가장 뒤에사람이랑 붙임
    A.sort()
    heapq.heapify(B)

    while B:
        a = A[0]  # A에서 가장 작은것
        b = heapq.heappop(B)  # B에서 가장 작은것
        if b > a:
            A.pop(0)
            answer += 1
        # elif b == a:
        #     A.pop(0)
        #     answer += 0
        else:
            A.pop()
            answer += 0

    return answer
