用于求解全源最短路（任意两点之间的最短距离）。
适用于任何图，但不能有负环（保证最短路存在）。

本质是三维 DP。
对于路径 $i、j$，枚举中转点 $k$，有 $dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])$。

时间复杂度 $O(n^3)$，空间复杂度 $O(n^2)$。
适用于 $n≤500$，适用于邻接矩阵。

## 模板
```java
for (int k = 1; k <= n; k++) {  
    for (int i = 1; i <= n; i++) {  
        for (int j = 1; j <= n; j++) {  
            if (a[i][k] != Integer.MAX_VALUE && a[k][j] != Integer.MAX_VALUE) {  
                a[i][j] = Math.min(a[i][j], a[i][k] + a[k][j]);  
            }  
        }  
    }  
}
```

## 习题
- 基础
	- [洛谷 # P2910 [USACO08OPEN] Clear And Present Danger S](https://www.luogu.com.cn/problem/P2910) 模板
	- [力扣 1334. 阈值距离内邻居最少的城市](https://leetcode.cn/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) 模板

#atom 
