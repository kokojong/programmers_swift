import Foundation

func solution(_ n: Int) -> Int {
    let board: [Int] = Array(repeating: -1, count: n) // 한 행에는 하나만 가능하니까 어디에 놓였는지 체크용
    var answer: Int = 0
    
    dfs(board: board, depth: 0, n: n, answer: &answer)
    
    return answer
}

func dfs(board: [Int], depth: Int, n: Int, answer: inout Int) {
    if depth == n {
        answer += 1
        return
    }
    
    for i in 0..<n {
        if isValid(r: depth, c: i, board: board) {
            var bboard = board // 사본
            bboard[depth] = i // depth 행의 값은 i
            dfs(board: bboard, depth: depth + 1, n: n, answer: &answer)
        }
        
        
    }
}

func isValid(r: Int, c: Int, board: [Int]) -> Bool {
    for i in 0..<r {
        if board[i] == c { // 같은 열에 이미 배치
            return false
        }
        
        if abs(r - i) == abs(c - board[i]) { // 대각선 - 행의 차이, 열의 차이의 절댓값이 같으면
            return false
        }
    }
    
    return true
    
