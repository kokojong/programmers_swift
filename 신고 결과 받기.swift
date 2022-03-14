import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    
    // 동일 유저 신고는 1회처리
    // k번 이상 신고된 유저는 정지, 신고한 모든 유저에게 정지 사실을 이메일 발송
    // 신고 내용을 모두 취합후 한번에 발송
    
    // [신고 받은 사람 : 횟수]
    var dict: [String : Int] = [:]
    id_list.forEach {
       dict[$0] = 0
    }
    
    var setReport = Set(report)
    
    for rep in setReport {
        let splited = rep.components(separatedBy: " ")
        let reportFrom = splited[0]
        let reportTo = splited[1]
        dict[reportTo]! = dict[reportTo]!+1
    }
    
    var result: [Int] = Array(repeating: 0, count: id_list.count)
    
    for rep in setReport {
        let splited = rep.components(separatedBy: " ")
        let reportFrom = splited[0]
        let reportTo = splited[1]
        if dict[reportTo]! >= k { // 신고 받은 횟수가 k번 이상이라면
            result[id_list.index(of: reportFrom)!] += 1
        }

    }
    // print(result)
    // print(dict)
    
    return result
}
