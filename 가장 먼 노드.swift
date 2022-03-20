import Foundation

var queue: [Int] = [1] // 몇 번 노드인지?
var connect: [[Int]] = []
var visited: [Bool] = []
var result: [Int] = []

func solution(_ n:Int, _ edge:[[Int]]) -> Int {
    
    connect = Array(repeating: [], count: n+1) // 0~n
    visited = Array(repeating: false, count: n+1)
    result = Array(repeating: 0, count: n+1)
    
    for ed in edge {
        let a = ed[0]
        let b = ed[1]
        connect[a].append(b)
        connect[b].append(a)
    }
    
    visited[1] = true
    
    while !queue.isEmpty {
        let q = queue.removeFirst() // 현재 노드
        bfs(q,result[q])
    }
    
    // print(result)
    let maxV = result.max()
    return result.filter { $0 == maxV}.count
    // result.filter { $0 == result.max()}.count로 했더니 틀림(할때마다 max를 계산하게 한다)
}

func bfs(_ f: Int, _ depth: Int) {
    let edges: [Int] = connect[f].filter { visited[$0] == false } // f에서 갈 수 있는 리스트
    
    for edge in edges {
        // if visited[edge] == false {
            queue.append(edge)
            visited[edge] = true
            result[edge] = depth+1
        // } 
    }
    
    
}
