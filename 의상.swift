import Foundation

func solution(_ clothes:[[String]]) -> Int {
    // idea: (갯수+1)씩을 곱하고 -1해주기(아무것도 안입은 경우)
    var answer = 1
    var dict: [String : Int] = [:] // 카테고리명 : 갯수
    for cloth in clothes {
        let category = cloth[1]
        var cnt: Int = dict[category] ?? 0
        dict[category] = cnt + 1
        
    }
    dict.forEach { k, v in
        answer *= (v+1)
    }
    answer -= 1 // 아무것도 안입는 경우
    return answer
}