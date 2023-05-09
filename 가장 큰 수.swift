import Foundation

func solution(_ numbers:[Int]) -> String {
    // idea: 배열의 원소 맨 앞에 숫자가 젤 큰거 기준으로 정렬하기
    
    var answer = ""
    var arr = numbers
    arr = arr.sorted {
        let s1 = String($0)
        let s2 = String($1)
        // print(s1+s2, s2+s1)
        return Int(s1 + s2)! > Int(s2 + s1)! // 순서를 바꾼것 중 어떤게 더 큰지 비교
    }
    answer = arr.map{ String($0) }.joined()
    if arr.reduce(0, +) == 0 { answer = "0"}
    return answer
}