import Foundation

func solution(_ dirs:String) -> Int {
    
    var positionX = 0, positionY = 0
    
    var passed: [[Int]] = []
    
    func checkRoot(_ x1: Int, _ y1: Int, _ x2: Int, _ y2: Int) -> [Int] {
        if x2 <= 5 && x2 >= -5 && y2 <= 5 && y2 >= -5 { // -5 ~ 5 사이 일때만
            if !passed.contains([x1,y1,x2,y2]) && !passed.contains([x2,y2,x1,y1]) {
                passed.append([x1,y1,x2,y2])
                // print(passed)
            }
             return [x2, y2]
        }
        return [x1,y1]
        
    }
    
    for dir in dirs {
        var result: [Int] = [0,0]
        if dir == "U" {
            result = checkRoot(positionX,positionY,positionX,positionY+1)
        } else if dir == "D"{
            result = checkRoot(positionX,positionY,positionX,positionY-1)
        } else if dir == "L" {
          result = checkRoot(positionX,positionY,positionX-1,positionY)
        } else if dir == "R" {
            result = checkRoot(positionX,positionY,positionX+1,positionY)
        }
        positionX = result[0]
        positionY = result[1]
        
    }
    return passed.count
    
    
}
