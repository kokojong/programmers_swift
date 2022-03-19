import Foundation

func solution(_ n:Int, _ times:[Int]) -> Int64 {
    
    var left =  1
    var right = times.max()! * n  // 가장 오래 걸리는 경우 - 가장 오래걸리는데 n명
    
    while left != right {
        var mid: Int = (left + right) / 2 // 임시의 시간
        var person: Int = 0 // 이 시간 내에 가능한 인원
        
        for t in times {
            person += mid / t // 가능 인원을 계산
        }
        
        if person >= n { // 가능하다면 -> 시간이 남는걸지도? -> right 내림
            right = mid
        } else { // 가능한 인원이 적다면 -> 시간이 적었다 -> left 올림
            left = mid+1
        }
        
    }
    
    return Int64(left)
}
