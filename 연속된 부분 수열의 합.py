def solution(sequence, k):
    #     sums = [0]

    #     tmp = 0
    #     for s in sequence:
    #         tmp += s
    #         sums.append(tmp)

    # n = len(sequence)
    # for l in range(1, n): # k: 배열의 길이
    #     for i in range(0, n-l+1):
    #         s = sums[i+l] - sums[i]
    #         # print(s, i)
    #         if s == k:
    #             return [i, i+l-1]

    results = []
    n = len(sequence)

    l = 0
    r = 0
    tmp = 0

    while True:
        if tmp < k:  # r을 한칸 증가
            if r < n:  # 아직 맨끝이 아니라면
                tmp += sequence[r]
                r += 1
            else:
                break

        else:  # tmp >= k
            if l < n and l <= r:
                tmp -= sequence[l]
                l += 1
            else:
                break

        if tmp == k:
            results.append([l, r-1])
    # print(results)

    results.sort(key=lambda x: (x[1] - x[0], x[0]))
    return results[0]
