from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)


def solution(enroll, referral, seller, amount):
    answer = []
    n = len(enroll)
    m = len(seller)
    dic = {}  # 부모 저장 -> center는 '-' 으로 표현
    result = defaultdict(int)

    for i in range(n):
        dic[enroll[i]] = referral[i]

    def dfs(child, money):
        if money == 0:  # 힌트 봄 ㅎ... 나눌 돈이 없으면 dfs 종료시키기
            return
        if child == '-':  # 더 이상 center 바로 아래의 부모인 경우
            result[child] += money
        else:
            # result[parent] += money//10
            result[child] += money - int(money//10)
            parent = dic[child]
            dfs(parent, money//10)

    for i in range(m):
        dfs(seller[i], amount[i] * 100)
    for i in range(n):
        answer.append(result[enroll[i]])

    return answer
