import Foundation

var answer: [[Int]] = []

func solution(_ n:Int) -> [[Int]] {
    
    hanoi(n,1,3,2)
    
    return answer
}

func hanoi(_ n: Int, _ from: Int, _ to: Int, _ via: Int) {
    if n == 1 {
        answer.append([from, to])
    } else {
        hanoi(n-1, from, via, to)
        answer.append([from,to])
        hanoi(n-1, via, to, from)
    }
    
}
