import Foundation

func solution(_ number:String, _ k:Int) -> String {
    var arr = number.map { Int(String($0))! }
    var stack: [Int] = []
    var delete = 0
    var i = 0 // arr의 인덱스를 집는것
    
    while i < arr.count, delete < k {
        let a = arr[i] // 들어올만한 숫자
        
        if stack.isEmpty { 
            stack.append(a)
            i += 1
            continue
        }
        
        if stack.last! < a {
            stack.removeLast()
            delete += 1
            continue // 스텍의 마지막거를 계속 비교해서 a보다 안작을때까지 지움
        }
        
        stack.append(a) // 이제 다 지워진거면 a를 추가하고 i를 옮김
        i += 1
    }
    
    // print(stack, i, delete)
    
    if delete == k { // k개만큼 삭제 완료
        stack.append(contentsOf: arr[i...])
    } else { // delete개만큼 지우지 못한 경우 - stack이 너무 큼
        for _ in 0..<(k-delete) { // 못지운 갯수만큼 뒤에서 제거해줌
            stack.removeLast()    
        }
    }
    
    return stack.map{ String($0) }.joined(separator: "")
}

// https://tngusmiso.tistory.com/52 참고함