import Foundation

// 틀리고나서 생각한 아이디어 -> 거의 1을 추가하면 1개나 2개의 비트가 다른수중에서 제일 작은수인데 예외(3,7등이 생긴다) -> 마지막이 11(2)로 끝나는 수인 4로 나눈 나머지가 3인 경우에만 검사를 해보는건?
func solution(_ numbers:[Int64]) -> [Int64] {
    var result: [Int64] = []
    
    for number in numbers {
        if number%4 != 3 {
            result.append(number+1)
            
        } else { // 나머지 일때만 검사하기?
            
         
        
        var numberBit = String(number, radix: 2)
        var newNumber = number
         
        while true {
            newNumber += 1
            let newNumberBit = String(newNumber, radix: 2)
            
            var cnt = 0 // 다른 비트의 개수 세기
            if numberBit.count == newNumberBit.count {
                for i in 0..<numberBit.count {
                    if cnt > 2 {
                        break
                    }
                    if numberBit[numberBit.index(numberBit.startIndex, offsetBy: i)] != newNumberBit[newNumberBit.index(newNumberBit.startIndex, offsetBy: i)] {
                        // print("다름1")
                        cnt += 1
                    }
                }
            } else { // 다른 비트수
                numberBit = "0" + numberBit
                for i in 0..<numberBit.count {
                    if cnt > 2 {
                        break
                    }
                   if numberBit[numberBit.index(numberBit.startIndex, offsetBy: i)] != newNumberBit[newNumberBit.index(newNumberBit.startIndex, offsetBy: i)] {
                        // print("다름2")
                        cnt += 1
                    }
                }
            }
            
            if cnt == 1 || cnt == 2 {
                break
            }
        }
        result.append(newNumber)
        // print(number,newNumber)
    }
        
    } // else
    
    return result
}
