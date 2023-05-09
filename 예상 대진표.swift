import Foundation

func solution(_ n:Int, _ a:Int, _ b:Int) -> Int
{
    // 2^m = n
    // a가 각각 라운드에 몇번째 블록에 있는지 체크하기
    
    // n = 8일때
    // [1 2 3 4 5 6 7 8]
    // a = 4, b = 7 일때
    // a-1 / 2 -> 1
    // b-1 / 2 -> 3
    // 두개가다르므로
    // 다시  2*2로 나눈다
    // a-1 / 4 = 0
    // b-1 / 4 = 1
    // 두개 다르므로 다시 2^3으로 나눔
    // a-1 / 8 = 0
    // b-1 / 8 = 0 같음! -> 만남
    
    // 위와 원리는 비슷하나 세부 구현이 틀림!
    var answer = 0
    
    var a = a
    var b = b
    
    while true {
        if a == b {
            break
        } else {
            // a/2 가 안되는 이유 -> a가 1이면 0이 되어버림.. 잘 판단하고 해보기!
            // a = (a % 2 == 0) ? a/2 : (a+1)/2 // 홀수 짝수일때에 따라 다름
            a = (a+1) / 2
            b = (b % 2 == 0) ? b/2 : (b+1)/2
        }
        
        answer += 1
    }

    return answer
}