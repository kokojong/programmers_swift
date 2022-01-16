import Foundation

func solution(_ n:Int) -> Int 
{   
    // var dp: [Int] = Array(repeating: 0, count: n+1)
    // print(dp)
    var now = n
    var count = 0
    
    // 이렇게 했더니 하나하나 해줘야해서 효율성 0점 받음ㅋㅋㅋ
//     for i in 1...n {
//         if i == 1 || i == 2 {
//             dp[i] = 1
//         } else {
//           if i%2 == 0 {
//               dp[i] = min(dp[i-1]+1, dp[i/2])
//           } else {
//               dp[i] = dp[i-1]+1
//           }
//         }
        
//     }
    
    while now != 0 {
        if now%2 == 0 {
            now = now/2
        } else {
            now -= 1
            count += 1
        }
        
    }
   
    
    return count
}
