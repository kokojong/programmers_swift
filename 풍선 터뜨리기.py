def solution(arr):
    n = len(arr)
    answer = n
    maxV = 10**9
    # 해당 숫자의 좌 / 우를 살피고 둘다 K보다 작다면 불가능함

    minLefts = []
    minRights = []

    minLeft = maxV
    minRight = maxV

    for i in range(n):
        l = arr[i]
        minLeft = min(minLeft, l)
        minLefts.append(minLeft)

        r = arr[n-i-1]
        minRight = min(minRight, r)
        minRights.append(minRight)

    minRights.reverse()
    # print(minLefts)
    # print(minRights)

    for i in range(n):
        k = arr[i]

        left = minLefts[i]
        right = minRights[i]

        if k > left and k > right:
            answer -= 1  # 양쪽의 최소값이 둘다 나보다 작을때는 남길수 없음

    return answer
