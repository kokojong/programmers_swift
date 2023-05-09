import Foundation

func solution(_ n:Int, _ words:[String]) -> [Int] {
    var answer: [Int] = [0, 0] // 탈락자 번호, 차례
    var dict: [String: Bool] = [:]
    
    let w = words.count // words의 갯수
    var last = words.first!.suffix(1)
    dict[words.first!] = true
    
    for i in 1..<w {
        if words[i].prefix(1) == last && dict[words[i]] == nil {
            dict[words[i]] = true // 끝말잇기가 가능한 경우
            last = words[i].suffix(1)
            // print(words[i].prefix(1), words[i].suffix(1))
        } else { // 탈락한 경우 - 끝 글자와 같지 않거나 dict에 있는거면
            answer = [i%n + 1, i / n + 1]
            break
        }
        
    }
    
    return answer
}