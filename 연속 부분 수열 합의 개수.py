def solution(elements):
    answer = []
    arr = elements + elements
    n = len(elements)
    for i in range(n):
        for j in range(1,n+1):
            tmp = sum(arr[i:i+j])
            # print(arr[i:i+j])
            # print(tmp)
            # if tmp not in answer:
            answer.append(tmp)
    return len(set(answer))