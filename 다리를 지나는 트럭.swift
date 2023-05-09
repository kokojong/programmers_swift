import Foundation

func solution(_ bridge_length:Int, _ weight:Int, _ truck_weights:[Int]) -> Int {
    // bridge_length -> 다리의 길이(동시에 올라갈수 있는 트럭수)
    // weight -> 최대 무게
    
    var answer = 0
    var queue: [Int] = truck_weights
    var bridge: [Int] = Array(repeating: 0, count: bridge_length)
    var passed: [Int] = []
    var sum = 0 // bridge의 합
    while !(passed.count == truck_weights.count) { // passed에 모든 트럭이 올때까지
        answer += 1
        
        // bridge 먼저 이동
        let f = bridge.first! // 가장 오래된 것
        if f != 0 { // 비어있지 않으면
            passed.append(f)
        }
        sum -= bridge.removeFirst()
        
        let q: Int = queue.first ?? 0
        if sum + q > weight { // 너무 무거워서 못들어감
            bridge.append(0)
        } else {
            bridge.append(q)
            sum += q
            if q != 0 { queue.removeFirst() } 
        }
        
        // print("queue", queue)
        // print("bridge", bridge)
        // print("passed", passed)
        
    }
    
    return answer
}