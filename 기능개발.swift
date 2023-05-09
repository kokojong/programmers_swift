import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var answer: [Int] = []
    
    var progresses: [Int] = progresses // queue처럼 사용
    var speeds: [Int] = speeds // queue 처럼 사용
    
    while !progresses.isEmpty {
        for i in 0..<progresses.count {
            progresses[i] += speeds[i]
        }    
        
        var result = 0 // 하루에 배포되는 갯수
        // 100 이상이라면 두개 모드 removeFirst 해주고 result += 1
        while progresses.first ?? 0 >= 100 { 
            progresses.removeFirst()
            speeds.removeFirst()
            result += 1
        }
        
        if result > 0 { answer.append(result) }
        // print("progresses", progresses)
    }
    
    return answer
}