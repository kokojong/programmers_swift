import Foundation

var num = 1
var board: [[Int]] = []
var n = 0
var result: [Int] = []

func solution(_ n:Int) -> [Int] {
    for i in 1...n {
        var tmp: [Int] = []
        for _ in 1...i {
            tmp.append(0)
        }
        board.append(tmp)
    }
    
    // 다음 동작을 정의(아래 오른쪽 위)
    board[0][0] = num
    if checkNextRow(0,0) {
        goDown(1,0)
    } else { // n = 1
        return [1]
    }
    
    // print(board)
    
    result = board.reduce(into: [Int]()) { $0.append(contentsOf: $1)}

    return result
}

func goDown(_ row: Int, _ col: Int) {
    num += 1
    board[row][col] = num
    
    if checkNextRow(row,col) {
        if board[row+1][col] == 0 {
            goDown(row+1,col)
        } else {
            if checkNextColumn(row,col) && board[row][col+1] == 0 {
                goRight(row,col+1)    
            }
        }
    } else { // 마지막 행까지 내려온 경우
        goRight(row,col+1)    
    }
   
}

func goRight(_ row: Int, _ col: Int) {
    num += 1
    board[row][col] = num
    
    if checkNextColumn(row,col) {
       if board[row][col+1] == 0 {
           goRight(row,col+1)
       } else {
           if checkUp(row,col) && board[row-1][col-1] == 0 {
                goUp(row-1,col-1) 
            }
       }
    } else { // 맨 아래 끝
        if board[row-1][col-1] == 0 {
            goUp(row-1,col-1)    
        }   
    }
}

func goUp(_ row: Int, _ col: Int) {
    num += 1
    board[row][col] = num
    
    if checkUp(row,col) {
        if board[row-1][col-1] == 0 {
            goUp(row-1,col-1)
        } else {
            if checkNextRow(row,col) && board[row+1][col] == 0 {
                goDown(row+1,col)    
            }
        }
    }
}

func checkNextRow(_ row: Int, _ col: Int) -> Bool {
    if row + 1 >= board.count {
        return false
    } else { return true }
}

func checkNextColumn(_ row: Int, _ col: Int) -> Bool {
    if col + 1 >=  board.count {
        return false
    } else { return true }
}

func checkUp(_ row: Int, _ col: Int) -> Bool {
    if row - 1 < 0 || col - 1 < 0 {
        return false
    } else { return true }
}
