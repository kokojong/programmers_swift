import Foundation

func solution(_ number:String, _ k:Int) -> String {
    var arr = number.map { Int(String($0))! }
    // 예제 2에서 k = 1이라면 1을 없앨때 231234 > 123234
    // 즉, 숫자는 앞에서 부터 없애야한다.
    
    var target = 0 // 0으로 부터 제거 시작
    
    while arr.count != number.count - k {    
        var isIn = false
        for i in 0..<arr.count {
            if arr[i] == target {
                arr.remove(at: i)
                isIn = true
                break
            }
        } // 다 돌았는데도 없으면
        if !isIn { target += 1 }
        
    }
    
    // print(arr)
    return arr.map{ String($0) }.joined(separator: "")
}

// 틀린 이유: 
// 테스트 3
// 입력값 〉	"4177252841", 4
// 기댓값 〉	"775841"
// 실행 결과 〉	실행한 결괏값 "477584"이 기댓값 "775841"과 다릅니다.