//
//  main.swift
//  Algo_swift
//
//  Created by 전판근 on 2021/06/04.
//

// 백준 14500번 테트리미노


import Foundation

let list = readLine()!.components(separatedBy: " ").map { Int(String($0))! }
let n = list[0]
let m = list[1]
var board = [[Int]]()

for _ in 0..<n {
    board.append(readLine()!.components(separatedBy: " ").map { Int(String($0))! } )
}

let figures = [
    // ⚡️ 모양
    [[1, 0], [1, 1], [0, 1]],
    
    // ㄴ 모양
    [[1, 0], [1, 0], [1, 1]],
    
    // ㅗ 모양
    [[0, 1, 0], [1, 1, 1]],
    
    // ㅡ 모양
    [[1, 1, 1, 1]],
    
    // ㅁ 모양
    [[1, 1], [1, 1]]
]


