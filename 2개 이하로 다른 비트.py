def solution(numbers):
    # x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
    # -> 비트로 교환했을 때 맨 뒤에 2개만 바꿔보기
    # 00 -> 01, 01 -> 00, 
    answer = []
    
#     for number in numbers:
#         i = 1
#         while True:
#             new = number + i
            
#             a = bin(number)
#             b = bin(new)
#             # print(a,b)
#             result = bin(int(a, 2) ^ int(b, 2))
#             if result.count('1') <= 2:
#                 answer.append(new)
#                 break
#             i += 1
#             # print(bin)
    for number in numbers:
        # 짝수이면 1만 더해주면 끝
        # 홀수이면 0의 위치 만큼 더하고 그 다음거 만큼 빼주기(2^k)
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            bi = "0" + bin(number)[2:]
            for i in reversed(range(len(bi))):
                if bi[i] == '0':
                    k = len(bi) - i - 2
                    # print("2 ** i", k, 2 ** k)
                    answer.append(number + (2 ** k))
                    break
            
    return answer