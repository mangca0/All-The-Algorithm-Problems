对于一些二维 DP（例如背包、最长公共子序列），如果把 DP 矩阵画出来，其实状态转移可以视作**在网格图上的移动**。在学习相对更抽象的二维 DP 之前，做一些形象的网格图 DP 会让后续的学习更轻松。

记忆化搜索在网格图上更得天独厚。

## 带路径的递归
带路径的递归不适合改 DP。
[力扣 79. 单词搜索](https://leetcode.cn/problems/word-search/) 路径依赖「已访问格集合」导致状态爆炸。
能改成动态规划的递归，**决定返回值的可变参数往往都比较简单**，而这题中搜索路径也是可变参数之一。

[力扣 3393. 统计异或值为给定值的路径数目](https://leetcode.cn/problems/count-paths-with-the-given-xor-value/) 这题同样是带路径的递归，但数据范围小，可以把路径状态压缩到三维 DP。

体会这两题。

## 习题
[力扣 63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/) 有障碍的二维爬楼梯
[力扣 120. 三角形最小路径和](https://leetcode.cn/problems/triangle/) 计算杨辉三角
[力扣 2304. 网格中的最小路径代价](https://leetcode.cn/problems/minimum-path-cost-in-a-grid/)做到 $O(mn^2)$

[力扣 3418. 机器人可以获得的最大金币数](https://leetcode.cn/problems/maximum-amount-of-money-robot-can-earn/) 选与不选
[力扣 3742. 网格中得分最大的路径](https://leetcode.cn/problems/maximum-path-score-in-a-grid/) 要同时注意 $k$ 的边界判断，**如果递推边界写不好，推荐写记忆化搜索**

[力扣 1824. 最少侧跳次数](https://leetcode.cn/problems/minimum-sideway-jumps/) 很有意思的题，要注意状态更新的顺序

#atom