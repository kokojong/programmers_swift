import Foundation

enum Commands: String{
    case Enter
    case Leave
    case Change
}

func solution(_ record:[String]) -> [String] {
    
    var dict: [String : String] = [:]
    var result: [String] = []
    
    for rec in record {
        var splited = rec.components(separatedBy: " ")
        // print(splited) // command, uid, name
        var command = splited[0]
        var uid = splited[1]
        var name = ""
        if splited.count>2 {
            name = splited[2]
        } else {
            name = dict["\(uid)"]!
        }
        
        switch command {
            case Commands.Enter.rawValue:
                result.append("\(uid)님이 들어왔습니다.")
                dict[uid] = name
            case Commands.Leave.rawValue:
                result.append("\(uid)님이 나갔습니다.")
            case Commands.Change.rawValue:
                dict[uid] = name
            default:
                print("error")        
        }
        
//         print(result)
    }
    
    var newResult: [String] = []
    result.forEach {
        var before = $0.components(separatedBy: "님") // uid, ~~습니다.
        newResult.append("\(dict[before[0]]!)님\(before[1])")
    }
        
    return newResult
}
