
暴力做法是枚举所有排列，对每个排列做相应计算，时间复杂度通常是 $O(n!)$.

状压 DP 时间复杂度通常是 $O(n \cdot 2^n)$.

一般定义 $dfs(s)$ 表示「可选」/「已选」元素集合为 $s$ 时，和题目有关的最优值.

## Problems

**基础**

- [力扣 526. 优美的排列](https://leetcode.cn/problems/beautiful-arrangement/)
- [力扣 3376. 破解锁的最少时间 I](https://leetcode.cn/problems/minimum-time-to-break-locks-i/) 
- [力扣 1879. 两个数组最小的异或值之和](https://leetcode.cn/problems/minimum-xor-sum-of-two-arrays/) 