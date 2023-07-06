from itertools import permutations
from collections import defaultdict


def solution(user_id, banned_id):
    answer = []
    n = len(user_id)
    k = len(banned_id)

    # fr*d* -> frodo, fradi

    # dic = defaultdict(list)

    def checkPosible(user, banned):  # user, banned
        if len(user) != len(banned):
            return False

        for i in range(len(user)):
            u, b = user[i], banned[i]
            if u == b or b == "*":
                continue
            else:
                return False

        return True

    # for banned in banned_id:
    #     for user in user_id:
    #         c = checkPosible(user, banned)
    #         if c == True:
    #             dic[banned] += [user]
    #             # print(user, banned)

    for perm in permutations(user_id, k):
        isPosible = True
        for i in range(k):
            if checkPosible(perm[i], banned_id[i]) == False:
                isPosible = False

        if isPosible:
            if set(perm) not in answer:
                answer.append(set(perm))
    return len(answer)
