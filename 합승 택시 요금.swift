import Foundation

let maxV = 1000000
// let maxV = 999

func solution(_ n:Int, _ s:Int, _ a:Int, _ b:Int, _ fares:[[Int]]) -> Int {
    // 지점의 갯수 n, 출발지 s, A도착지, B도착지, 지점 사이의 가격
    // fares = [c지점, d지점, 요금f]
    
    // (n+1)*(n+1)
    var board = Array(repeating: Array(repeating: maxV, count: n+1), count: n+1)
    for i in (1...n) {
        board[i][i] = 0
    }
    
    for fare in fares {
        // 양방향이라서
        board[fare[0]][fare[1]] = fare[2]
        board[fare[1]][fare[0]] = fare[2]
    }
    
    for k in 1...n { // 거쳐가는 곳
        for i in 1...n { // 시작
            for j in 1...n { // 끝
                if board[i][j] > board[i][k] + board[k][j] {
                    board[i][j] = board[i][k] + board[k][j]
                }
            }
        }
    }
    
    var result = board[s][a] + board[s][b]
    
    for k in 1...n {
        if result > board[s][k] + board[k][a] + board[k][b] {
            result = board[s][k] + board[k][a] + board[k][b]
        }
    }
    
    return result
}
