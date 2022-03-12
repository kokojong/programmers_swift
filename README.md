# 프로그래머스 문제 스위프트로 풀기

### 2022.03.12(sat) 오픈채팅방
[오픈채팅방](https://programmers.co.kr/learn/courses/30/lessons/42888?language=swift)

[풀이](https://github.com/kokojong/programmers_swift/blob/main/%EC%98%A4%ED%94%88%EC%B1%84%ED%8C%85%EB%B0%A9.swift)

***

알게 된 것
- `String.components(separatedBy: String)` 로 문자열 자르기(기준이 되는 것은 사라짐)
  - components 는 반환형이 [String]
  - 비슷한 `String.split(seperator: Charcter)` 는 반환형이 [Substring]
- Dictionary의 사용
  - 딕셔너리 생성
  ```swift
  var dict: [String: Int] = [:]
  ```
  - 딕셔너리 값 추가, 수정
  ```swift
  let aa = dict["a", default: 1]  
  ```
  
  
