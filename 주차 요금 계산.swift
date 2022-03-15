import Foundation

func calculateTime(_ inTime: String, _ outTime: String) -> Int {
    let inComponents = inTime.components(separatedBy: ":")
    let inHour = Int(inComponents[0])!
    let inMin = Int(inComponents[1])!
    
    let outComponents = outTime.components(separatedBy: ":")
    let outHour = Int(outComponents[0])!
    let outMin = Int(outComponents[1])!
    
    let result = (60*outHour + outMin) - (60*inHour + inMin)
    return result
}

func calculateFee(_ useTime: Int, _ baseTime: Int, _ baseFee: Int, _ extraTime: Int, _ extraFee: Int) -> Int {
    
    if useTime <= baseTime {
        return baseFee
    } else {
        // extraTime -1 을 더해줌으로써 올림처리
        var result = (useTime - baseTime + extraTime - 1)/extraTime * extraFee + baseFee
        return result   
    }
}

func solution(_ fees:[Int], _ records:[String]) -> [Int] {
    
    // 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return
    // 아직 출차하지 않은 차량은 23:59분에 출차한 것으로 간주
    
    // 차량 번호 : 들어온 시간
    var inDict: [String: String] = [:]
    // 차랑번호 : 총 이용시간
    var timeDict: [String:Int] = [:]
    
    for rec in records {
        let components = rec.components(separatedBy: " ")
        let time = components[0]
        let car = components[1]
        // let action = components[2]
        // 이렇게 하면 action에 대한 처리를 안해줘도 될 듯
        
        // 아직 안들어왔거나 나갔거나
        if inDict[car] == nil {
            inDict[car] = time
            if timeDict[car] == nil { // 미이용
                timeDict[car] = 0
            } else { // 재출입
                timeDict[car]! += 0
            }
        } else {
            timeDict[car]! += calculateTime(inDict[car]!, time)
            inDict[car] = nil
        }
    }
    
    // 아직 나가지 않은 차량 계산
    inDict.forEach {
        timeDict[$0.key]! += calculateTime($0.value, "23:59")
        // print("미출차",timeDict)
    }
    
    // 차량번호 오름차순 정렬
    let sortedTimeDict = timeDict.sorted(by: < )
    // print(sortedTimeDict)
    
    var result: [Int] = []
    sortedTimeDict.forEach {
        result.append(calculateFee($0.value, fees[0], fees[1], fees[2], fees[3]))
    }
    
    return result
}
