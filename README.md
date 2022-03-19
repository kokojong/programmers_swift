# 프로그래머스 문제 스위프트로 풀기

### 2022.03.12(sat) 오픈채팅방
[문제](https://programmers.co.kr/learn/courses/30/lessons/42888?language=swift)
[풀이](https://github.com/kokojong/programmers_swift/blob/main/%EC%98%A4%ED%94%88%EC%B1%84%ED%8C%85%EB%B0%A9.swift)

알게 된 것
- `String.components(separatedBy: String)` 로 문자열 자르기(기준이 되는 것은 사라짐)
  - components 는 반환형이 [String]
  - 비슷한 `String.split(seperator: Charcter)` 는 반환형이 [Substring]이며 조금 더 빠르다고 한다.
- Dictionary의 사용
  - 딕셔너리 생성
  ```swift
  var dict: [String: Int] = [:]
  ```
  - 딕셔너리 값 추가, 수정
  ```swift
  let aa = dict["a", default: 1]  
  ```

***

### 2022.03.13(sun) 신고 결과 받기
[문제](https://programmers.co.kr/learn/courses/30/lessons/92334)
[풀이](https://github.com/kokojong/programmers_swift/blob/main/%EC%8B%A0%EA%B3%A0%20%EA%B2%B0%EA%B3%BC%20%EB%B0%9B%EA%B8%B0.swift)

알게 된 것
- `let setArray = Set(Array)`로 배열을 한번에 Set형태로 변환하기
- `Array(repeating: 0, count: id_list.count)`로 동일한 크기의 배열 초기화하기

***

### 2022.03.14(mon) 주차 요금 계산
[문제](https://programmers.co.kr/learn/courses/30/lessons/92341)
[풀이](https://github.com/kokojong/programmers_swift/blob/main/%EC%A3%BC%EC%B0%A8%20%EC%9A%94%EA%B8%88%20%EA%B3%84%EC%82%B0.swift)

알게 된 것
- m/n의 올림처리 -> (m + n - 1)/n
- Dictionary의 sort
  ```swift 
  let sortedTimeDict = timeDict.sorted(by: < ) 
  ```

***

### 2022.03.15(tue) k진수에서 소수의 갯수 구하기
[문제](https://programmers.co.kr/learn/courses/30/lessons/92335)
[풀이](https://github.com/kokojong/programmers_swift/blob/main/k%EC%A7%84%EC%88%98%EC%97%90%EC%84%9C%20%EC%86%8C%EC%88%98%20%EA%B0%9C%EC%88%98%20%EA%B5%AC%ED%95%98%EA%B8%B0.swift)

알게 된 것
- k진법으로 변환 -> String(n, radix: k)
- 추가적으로 filter를 통해서 ""에 대한 처리가 가능함(원래는 optional 처리로 했음)
- sqrt(Double(n))로 제곱근을 구할 수 있음
- 간만에 소수를 구하는 방법을 복습

***

### 2022.03.19(sat) 입국 심사
[문제](https://programmers.co.kr/learn/courses/30/lessons/43238?language=swift)
[풀이](https://github.com/kokojong/programmers_swift/blob/main/%EC%9E%85%EA%B5%AD%EC%8B%AC%EC%82%AC.swift)

알게 된 것
- 이진 탐색의 기본 원리(왜 1부터 무작정 체크하지 않고 중간을 찾아가야 하는지 - 너무 큰 수이기 때문에)
