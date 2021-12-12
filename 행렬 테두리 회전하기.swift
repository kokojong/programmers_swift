
// [행렬 테두리 회전하기](https://programmers.co.kr/learn/courses/30/lessons/77485)


import Foundation

func solution(_ rows:Int, _ columns:Int, _ queries:[[Int]]) -> [Int] {
    var result: [Int] = []
    var board: [[Int]] = []
    var num = 1
    
    for _ in 0..<rows {
        var row: [Int] = []
        for _ in 0..<columns {
            row.append(num)
            num += 1
        }
        board.append(row)
    }
    
    // 일단 하나만 해보자
    // var query: [Int] = queries[0] // x1, y1, x2, y2
    
    // 전체에 적용
    for query in queries {
    var x1 = query[0]
    var y1 = query[1]
    var x2 = query[2]
    var y2 = query[3]
    
    var totalList: [Int] = []
    // [x1-1][y1-1 ... y2-2] (위에서 오른쪽 하나 빼고)
    var top: [Int] = []
    for i in y1-1...y2-2 {
        top.append(board[x1-1][i])
    }
    totalList.append(contentsOf: top)
    // [x1-1...x2-2][y2-1] (오른쪽 맨아래 빼고)
    var righ: [Int] = []
    for i in x1-1...x2-2 {
        righ.append(board[i][y2-1])
    }
    totalList.append(contentsOf: righ)
    // [x2-1][y2-1...y1] (왼쪽 맨아래 빼고)
    var bottom: [Int] = []
    for i in y1...y2-1 {
        bottom.append(board[x2-1][i])
    }
    bottom.reverse()
    totalList.append(contentsOf: bottom)
    // [x2-1...x1-2][y1-1]
    var lef: [Int] = []
    for i in x1...x2-1 {
        lef.append(board[i][y1-1])
    }
    lef.reverse()
    totalList.append(contentsOf: lef)
    // print(totalList)
    // rotate (맨뒤의 것을 맨 앞으로 옮김)
    totalList.insert(totalList.removeLast(), at:0)
    
    // 최솟값을 추가
    result.append(totalList.min()!)
    
    // change element
    
    // top
    for i in y1-1...y2-2 {
        board[x1-1][i] = totalList.removeFirst()
    }
    // right
    for i in x1-1...x2-2 {
        board[i][y2-1] = totalList.removeFirst()
    }
    // left
    for i in x1...x2-1 {
        board[i][y1-1] = totalList.removeLast()
    }
    // bottom
    for i in y1...y2-1 {
        board[x2-1][i] = totalList.removeLast()
    }
        
    }

    return result
}
