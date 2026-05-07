
$n$ 个物品对应 $n$ 个位置.

暴力做法是枚举所有排列，对每个排列做相应计算，时间复杂度通常是 $O(n!)$.

状压 DP 时间复杂度通常是 $O(n \cdot 2^n)$.

一般定义 $dfs(s)$ 表示「可选」/「已选」元素集合为 $s$ 时，和题目有关的最优值.

状压的规模一般在 $n \leq 20$.

## Problems

**相邻无关**

- [力扣 526. 优美的排列](https://leetcode.cn/problems/beautiful-arrangement/)
- [力扣 3376. 破解锁的最少时间 I](https://leetcode.cn/problems/minimum-time-to-break-locks-i/) 
- [力扣 1879. 两个数组最小的异或值之和](https://leetcode.cn/problems/minimum-xor-sum-of-two-arrays/) 

**相邻相关 / 旅行商问题(TSP)**

增加一维 $pre$ 来消除后效性.

- [力扣 2741. 特别的排列](https://leetcode.cn/problems/special-permutations/) 
- [力扣 996. 平方数组的数目](https://leetcode.cn/problems/number-of-squareful-arrays/) 排列去重
- [力扣 1681. 最小不兼容性](https://leetcode.cn/problems/minimum-incompatibility/) 子集型 DP，可以转换为排列型 代码细节很多

- [力扣 943. 最短超级串](https://leetcode.cn/problems/find-the-shortest-superstring/) TSP 在搜索转移过程中留下路标 代码量大