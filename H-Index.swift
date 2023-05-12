import Foundation

func solution(_ citations:[Int]) -> Int {
    // n 편중 h번 이상 인용된 논문이 h편 이상 -> 이때 h가 H-Index
    // h번 이하 인용된 논문이 나머지
    var arr = citations.sorted() // 내림차순 정렬
    arr.reverse()
    
    let n = arr.count
    var answer = 0

    for i in 0..<n {
        if arr[i] >= (i + 1) { // i번째의 값 = h -> h이상의 갯수 == i+1(자신 포함)
            answer = i+1
        }
    }
    
    return answer
}