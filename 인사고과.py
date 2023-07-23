def solution(scores):
    answer = 1  # 1등부터 싲가
    # 임의의 사원보다 두 점수가 모두 낮은 경우가 한번이라도 있으면 인센티브를 못받게 된다 ㅜㅜ(흑흑) -> 최저점인 사람이 인센을 못받는다
    # 나머지에서는 두 점수의 합이 높은 순서대로 인세닡브가 차등 지급(같은 등수도 존재함)
    # scores[0] -> 완호
    wanho = [scores[0][0], scores[0][1]]  # s, c

    scores = sorted(scores, key=lambda x: (-x[0], x[1]))  # 앞에는 내림차순 뒤에는 오름차순

    maxC = 0  # 현재까지 나온 c중 최대값(뒤에꺼)
    for s, c in scores:
        if s > wanho[0] and c > wanho[1]:
            return -1  # 나가리

        if c >= maxC:  # 현재 나온거보다 크거나 같아야지 통과
            maxC = c  # 최댓값 갱신

            if s + c > sum(wanho):  # 나보다 총합이 높은 사람이 있다면 순위 밀림
                answer += 1

    return answer
