import Foundation

func solution(_ arr:[[Int]]) -> [Int] {
    var arr = arr
    var rows = arr.count // 2*n꼴
    var n = 0
    var count1 = 0
    var count0 = 0
    
    while rows != 1 {
        rows /= 2
        n += 1
    }
    
    func checkIsZippable(_ r1: Int, _ r2: Int, _ c1: Int, _ c2: Int) -> Void {
        var isZippable = true
        let midRow = (r1+r2)/2
        let midCol = (c1+c2)/2
        let num = arr[r1][c1]
        for r in r1...r2 {
            for c in c1...c2 {
                if arr[r][c] != num {
                    isZippable = false
                    break
                }
            }
        }
        
        if isZippable {
            if num == 1 {
                count1 += 1
            } else {
                count0 += 1
            }
        } else {
            checkIsZippable(r1, midRow, c1, midCol)   
            checkIsZippable(r1, midRow, midCol+1, c2) 
            checkIsZippable(midRow+1, r2, c1, midCol)  
            checkIsZippable(midRow+1, r2, midCol+1, c2) 
        }
    }
    
    // var n2 = 1 << n
    checkIsZippable(0, arr.count-1, 0 , arr.count-1)
    
    /*
    var n2 = 1 << n
    while n2 > 1 {
        if checkIsZippable(0, n2-1, 0, n2-1) == false {
            print("n2: \(n2) -> \(n2/2)")
            n2 = n2/2
            // mid = n2/2
            // checkIsZippable(0, n2-1, 0, n2-1)
            // checkIsZippable(0, n2-1, n2, n2*2-1)
            // checkIsZippable(n2, n2*2-1, 0, n2-1)
            // checkIsZippable(n2, n2*2-1, n2, n2*2-1)
            
        }
    }
    */
    
    return [count0,count1]
}
