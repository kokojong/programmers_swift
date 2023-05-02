import Foundation

func solution(_ N:Int, _ road:[[Int]], _ k:Int) -> Int {
    var answer = 0
    // 1번에서 시작함!
    
    // road 내에서 [Int]: [a,b,c] -> a에서 b까지 가느데 c가 걸린다.
    // dp로 해서 1번 마을에서 이어진 애들부터 해서 가면서 최단 시간을 구하자!
    // 최단 거리를 나타낸 dp
    var dp: [Int] = Array(repeating: 50*10000, count: N+1) // index 0 미사용
    // lines i와 연결된 마을들의 배열
    let maxV = 50 * 100000
    var graph: [[Int]] = Array(repeating: Array(repeating: maxV, count: N+1), count: N+1)
    
    // 1인 경우 처리
    if N == 1 {
        return 1
    }
    
    dp[1] = 0 // 자기자신
    
    for r in road {
        let start = r[0]
        let end = r[1]
        let dis = r[2]
        // 직접 연결된 것중 가장 작은거로 초기화(a,b를 연결하는 도로가 여러개가 있을 수 있어서 가장 짧은걸 택함)
        graph[start][end] = min(graph[start][end], dis)
        graph[end][start] = min(graph[end][start], dis)
    }
    // print(graph)
    
    var queue: [(Int, Int)] = [(1,0)] // 마을, 거리 - 자기자신꺼 먼저 넣음
    var index = 0 // 직접 삭제하면 오래걸려서 index를 이동
    
    while index < queue.count {
        let q = queue[index] // 가장 앞에꺼(처럼 쓰이는 것)
        index += 1 // 다음 칸으로 이동
        
        for i in 1...N { // 범위 주의!! 1..<N 이아님!! (0 index 미사용!)
            if graph[q.0][i] != maxV { // 연결된게 있을 때만!
                
                let dis = graph[q.0][i] + q.1
                if dis < dp[i] { // 최소거리여야함
                    dp[i] = dis // dp 갱신
                    queue.append((i, dis)) // queue에 추가
                }
            }
        }
        
    }
    
    answer = dp.filter{ $0 <= k }.count
    return answer
}
