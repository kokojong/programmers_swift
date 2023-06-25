def solution(genres, plays):
    answer = []
    # 장르 : 총갯수
    # 장르 : [ (횟수, 고유번호), (횟수, 고유번호)]

    count = {}
    items = {}

    n = len(genres)

    for i in range(n):
        genre = genres[i]
        play = plays[i]

        if genre in count:
            count[genre] += play
            tmp = items[genre]
            tmp.append([play, i])
            items[genre] = tmp
        else:
            count[genre] = play
            items[genre] = [[play, i]]

    # print(count)
    # print(items)

    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    # first = sorted_count[0] # 'a', 500
    # first_genre = items[first[0]] # 가장 많이 들은 장르의 plays
    # first_genre = sorted(first_genre, key = lambda x: (-x[0], x[1]))[:2]
    # for f in first_genre:
    #     answer.append(f[1])

    for sc in sorted_count:
        first_genre = items[sc[0]]  # 가장 많이 들은 장르의 plays
        first_genre = sorted(first_genre, key=lambda x: (-x[0], x[1]))[:2]
        for f in first_genre:
            answer.append(f[1])

    # if len(sorted_count) > 1:
    #     second = sorted_count[1]
    #     second_genre = items[second[0]] # 두번째로 많이 들은 장르의 plays
    #     second_genre = sorted(second_genre, key = lambda x: (-x[0], x[1]))[:2]
    #     for s in second_genre:
    #         answer.append(s[1])

    return answer

# ["pop", "pop", "pop", "rap", "rap"]
# [45, 50, 40, 60, 70]
# 답: [1, 0, 4, 3]
