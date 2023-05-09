import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    // queue에서 하나 꺼내기.
    // 대기중인것중에 우선순위가 더 높은게 있다면 꺼낸거 다시 집어넣음
    // 만약에 없다면 실행함.
    
    var answer = 0
    
    var queue: [(Int, Int)] = [] // location, 우선순위
    for i in 0..<priorities.count {
        queue.append((i, priorities[i]))
    }
    
    while true {
        var q = queue.removeFirst() // 맨 앞에 것
        let p = q.1 // 우선순위
        
        var isPopable = true
        for i in 0..<queue.count {
            if queue[i].1 > p { // 우선순위 높은게 있다면
                queue.append(q)
                isPopable = false
                break
            }
        }
        
        if isPopable { // pop 가능 -> 나보다 높은게 없음
            answer += 1
            if q.0 == location { break }
        }
    }
    
    return answer
}