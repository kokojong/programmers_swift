import Foundation

func solution(_ s:String) -> Int{
    var answer: Int

    var arr = Array(s)
    
    var stack: [Character] = []
    
    for i in 0..<arr.count {
        if stack.isEmpty { 
            stack.append(arr[i]) 
        } else {
          if stack.last! == arr[i] {
              stack.removeLast()
          } else {
              stack.append(arr[i])
          }
        }
    }
    
    answer = stack.isEmpty ? 1 : 0

    return answer
}
