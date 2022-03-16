import Foundation

func isPrimeNum(_ n: Int) -> Bool {
    if n == 2 || n == 3{
        return true
    } else if (n != 2 && n%2 == 0) || n == 1 {
        return false
    } else {
        let sqrtInt = Int(sqrt(Double(n)))
        
        for i in 3...sqrtInt {
            if n%i == 0 {
                return false
            }
        }
        return true
    }
    
}

func solution(_ n:Int, _ k:Int) -> Int {
    
    // case1 0P0
    // case2 P0
    // case3 0P
    // case4 P
    
    let converted: String = String(n, radix: k)
    
    let splited = converted.components(separatedBy: "0")
    
    var result = 0
    
    splited.forEach {
        // ""은 0으로 처리
        let num = Int($0) ?? 0
        if isPrimeNum(num) {
            result += 1
        }
    }
    
    return result
}
