//
//  main.swift
//  Algo_swift
//
//  Created by 전판근 on 2021/06/13.
//

// 백준 2042 구간 합 구하기

import Foundation

struct Fenwick {
    var list = [0]
    
    init(_ n: Int) {
        list = Array(repeating: 0, count: n+1)
    }
    
    func sum(_ idx: Int) -> Int {
        var ret = 0
        var pos = idx
        while pos > 0 {
            ret += list[pos]
            pos &= (pos-1)
        }
        
        return ret
    }
    
    mutating func add(_ idx: Int, _ val: Int) {
        var pos = idx
        
        while pos < list.count {
            list[pos] += val
            pos += (pos & -pos)
        }
    }
}

var input = readLine()!.split(separator: " ").map { Int(String($0))! }
let N = input[0], M = input[1], K = input[2]

var fenwick = Fenwick(N)

var list = [0]
for i in 0..<N {
    let num = Int(readLine()!)!
    list.append(num)
    fenwick.add(i+1, num)
}

for _ in 0..<M+K {
    let input2 = readLine()!.split(separator: " ").map { Int(String($0))! }
    
    if input2[0] == 1 {
        fenwick.add(input2[1], -list[input2[1]] + input2[2])
        list[input2[1]] = input2[2]
    } else {
        print(fenwick.sum(input2[2]) - fenwick.sum(input2[1]-1))
    }
}
