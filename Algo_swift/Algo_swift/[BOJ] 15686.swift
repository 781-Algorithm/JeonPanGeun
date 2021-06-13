//
//  main.swift
//  Algo_swift
//
//  Created by 전판근 on 2021/06/13.
//

// 백준 15686 치킨 배달

import Foundation

let input = readLine()!.split(separator : " " ).map{ Int(String($0))! }
let N = input[0], M = input[1]

var chickens = [Int]()
var houses = [Int]()
var answer = Int.max


// 입력을 받아서, 치킨집,집의 위치를 정수로 append한다.
for i in 0..<N {
    let input2 = readLine()!.split(separator : " " ).map{Int(String($0))!}
    
    for j in 0..<N {
        if input2[j] == 2 {
            chickens.append(i*N + (j))
        } else if input2[j] == 1 {
            houses.append(i*N + (j))
        }
    }
}

print(houses)
print(chickens)

// 치킨집들중에서 M개의 조합을 선택한다.
func select(_ selected : [Int], _ idx : Int ) {
    if selected.count  == M {
        answer = min(answer, mutate(selected))
    }else {
        for i in idx..<chickens.count {
            select(selected + [chickens[i]], i+1)
        }
    }
}

// 선택된 치킨집들로 각 집마다의 최소가 되는 거리를 구한다.
func mutate(_ selectChickens : [Int]) -> Int {
    var dists = 0
    for house in houses {
        let houseCor = transCorr(house)
        var minDist = Int.max
        
        for chicken in selectChickens {
            let dist = getDist(transCorr(chicken), houseCor )
            minDist = min(dist,minDist)
        }
        dists += minDist
    }

    return dists
}

// 정수인 값을 (r,c) 좌표로 변환한다.
func transCorr(_ val : Int ) -> (Int,Int) {
    return (val/N, val%N)
}

// (r,c)좌표로 두 좌표의 거리를 계산한다.
func getDist(_ cor1 : (Int,Int), _ cor2 : (Int,Int)) -> Int {
    return abs(cor1.0 - cor2.0) + abs(cor1.1 - cor2.1)
}


select([], 0)

print(answer)






