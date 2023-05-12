import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    let size = brown + yellow
    
    var bb = brown/2 + 2 // brown = (가로 + 세로 - 2) * 2 - 테두리
    // 가로 + 세로
    
    var width = 0
    var height = 0 // 가로 >= 세로
    
    for w in 1..<bb { // 가로
        let h = bb - w // 세로
            
        if (w-2)*(h-2) == yellow {
            width = max(w, h)
            height = min(w, h)
        }
    }
    
    return [width, height]
}