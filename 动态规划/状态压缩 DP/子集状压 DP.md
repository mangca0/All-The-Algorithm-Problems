
把 $n$ 个元素扔进 $k$ 个集合里，注意集合无序.

打破线性思维，从单点转移到子集枚举，一次处理一个集合.

一般定义 $dfs(i, s)$ 表示前 $i$ 个桶，接受了 $s$ 集合的最优情况. 将桶作为线性参数，处理完第 $i$ 个，就永远不回头管他.

状压的规模一般在 $n \leq 15$.

子集枚举（$O(3^n)$）：直接枚举当前 $mask$ 的所有子集 $sub$，一次性剥离，复杂度可用二项式定理证明.
`for (int sub = mask; sub > 0; sub = (sub - 1) & mask)`

## Problems

- [力扣 2305. 公平分发饼干](https://leetcode.cn/problems/fair-distribution-of-cookies/) 把零食分给孩子

- [力扣 1655. 分配重复整数](https://leetcode.cn/problems/distribute-repeating-integers/) 把需求分给数字频次 注意桶可以不被使用

- [力扣 1986. 完成任务的最少工作时间段](https://leetcode.cn/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) 不需要桶维度

- [力扣 1681. 最小不兼容性](https://leetcode.cn/problems/minimum-incompatibility/) 有 排列型状压做法