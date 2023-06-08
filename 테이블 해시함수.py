def solution(data, col, row_begin, row_end):
    answer = 0

    data.sort(key=lambda x: (x[col-1], -x[0]))
    for i in range(row_begin, row_end+1):
        # print(i, data[i-1])
        s = 0
        for d in data[i-1]:
            s += d % i
        answer = answer ^ s
    return answer
