
推荐使用 **刷表法**.

## Template


>网格被划分成 $M$ 行 $N$ 列 $(1 \le M \le 12, 1 \le  N \le 12)$。
>在牧场上种草，草地只能种在特定位置，并且不能上下左右相邻。
>求一共有多少种种植方案。
>
>输入：
>一个 $N$ 行 $M$ 列的矩阵，$1$ 表示该地可以种草，$0$ 表示该地不可以种草。
>
>输出：
>一个整数，即牧场分配总方案数除以 $10^8$ 的余数。

无空间压缩：
```java
public static void solve() {  
	int[][][] f = new int[n][m][1 << m];  
	for (int i = 0; i < n; i++) {  
		for (int j = 0; j < m; j++) {  
			if (i == 0 && j == 0) {  
				f[i][j][0] = 1;  
				if (a[0][0] == 1) {  
					f[i][j][1] = 1;  
				}  
				continue;  
			}  
			int pi = i, pj = j - 1;  
			if (pj < 0) {  
				pi = i - 1;  
				pj = m - 1;  
			}
			// 刷表 枚举上一个格子的所有状态
			for (int s = 0; s < (1 << m); s++) {  
				int ways = f[pi][pj][s];  
				// 剪枝
				if (ways == 0) {  
					continue;  
				}  
				// 不种
				f[i][j][set(s, j, 0)] += ways;  
				// 种
				if (a[i][j] == 1 && (j == 0 || get(s, j - 1) == 0) && get(s, j) == 0) {  
					f[i][j][set(s, j, 1)] += ways;  
				}  
			}  
		}  
	}  
	long ans = 0;  
	for (int i = 0; i < (1 << m); i++) {  
		ans = (ans + f[n - 1][m - 1][i]) % p;  
	}  
	out.println(ans);
}  

public static int set(int s, int i, int j) {  
	if (j == 1) {  
		s |= (1 << i);  
	} else {  
		s &= ~(1 << i);  
	}  
	return s;  
}  

public static int get(int s, int i) {  
	return s >> i & 1;  
}  
```
时间复杂度：$O(nm 2^m)$. 由于存在大量不合法的状态，复杂度不会跑满.
空间复杂度：$O(nm2^m)$.

利用滚动数组 空间压缩：
```java
public static void solve() {  
	// 只依赖上一个格子的所有状态  
	// O(nm) -> O(2)
	int[][] f = new int[2][1 << m];  
	int cur = 0;  
	for (int i = 0; i < n; i++) {  
	    for (int j = 0; j < m; j++) {  
	        int pre = cur;  
	        cur ^= 1;  
	        Arrays.fill(f[cur], 0);  
	  
	        if (i == 0 && j == 0) {  
	            f[cur][0] = 1;  
	            if (a[0][0] == 1) {  
	                f[cur][1] = 1;  
	            }  
	            continue;  
	        }  
	        for (int s = 0; s < (1 << m); s++) {  
	            int ways = f[pre][s];  
	            if (ways == 0) {  
	                continue;  
	            }  
	            f[cur][set(s, j, 0)] += ways;  
	            if (a[i][j] == 1 && (j == 0 || get(s, j - 1) == 0) && get(s, j) == 0) {  
	                f[cur][set(s, j, 1)] += ways;  
	            }  
	        }  
	    }  
	}  
	long ans = 0;  
	for (int i = 0; i < (1 << m); i++) {  
	    ans = (ans + f[cur][i]) % p;  
	}
		out.println(ans);
}  
```
时间复杂度：$O(nm 2^m)$. 由于存在大量不合法的状态，复杂度不会跑满.
空间复杂度：$O(2^m)$.

## Problems

[洛谷 P1879 [USACO06NOV] Corn Fields G](https://www.luogu.com.cn/record/277067061) 