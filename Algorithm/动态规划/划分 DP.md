
## **判定能否划分**

一般定义 f\[i] 表示长为 i 的前缀 a\[:i] 能否划分。

枚举最后一个子数组的左端点 L，从 f\[L] 转移到 f\[i]（过去更新现在），并考虑 a\[L:i] 是否满足要求。

### 习题
- [力扣 2369. 检查数组是否存在有效划分](https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/) 
- [力扣 139. 单词拆分](https://leetcode.cn/problems/word-break/)


## **最优划分**

计算最少（最多）可以划分出多少段、最优划分得分等。

一般定义 f[i] 表示长为 i 的前缀 a[:i] 在题目约束下，分割出的最少（最多）子数组个数（或者定义成分割方案数）。

枚举最后一个子数组的左端点 L，从 f[L] 转移到 f[i]，并考虑 a[L:i] 对最优解的影响。

## 习题
- [力扣 132. 分割回文串 II](https://leetcode.cn/problems/palindrome-partitioning-ii/) 模板
- [力扣 2707. 字符串中的额外字符](https://leetcode.cn/problems/extra-characters-in-a-string/) 
- [力扣 3196. 最大化子数组的总成本](https://leetcode.cn/problems/maximize-total-cost-of-alternating-subarrays/) 更小的划分
- [力扣 2767. 将字符串分割为最少的美丽子字符串](https://leetcode.cn/problems/partition-string-into-minimum-beautiful-substrings/) 不用预处理 5 的幂做法
- [力扣 91. 解码方法](https://leetcode.cn/problems/decode-ways/) 前导零 等价于 10<=s[i-1:i+1]
- [力扣 639. 解码方法 II](https://leetcode.cn/problems/decode-ways-ii/) 分支
- [力扣 LCR 165. 解密数字](https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/) 同 91
- [力扣 1043. 分隔数组以得到最大和](https://leetcode.cn/problems/partition-array-for-maximum-sum/)
- [力扣 3144. 分割字符频率相等的最少子字符串](https://leetcode.cn/problems/minimum-substring-partition-of-equal-character-frequency/) 快速判断平衡字符串（每个字母出现的次数相同的字符串）
- [力扣 1416. 恢复数组](https://leetcode.cn/problems/restore-the-array/) 91 变形


## **约束划分个数**

将数组分成（恰好/至多）k 个连续子数组，计算与这些子数组有关的最优值。
一般定义 f\[i]\[j] 表示将长为 j 的前缀 a\[:j] 分成 i 个连续子数组所得到的最优解。
枚举最后一个子数组的左端点 L，从 f\[i−1]\[L] 转移到 f\[i]\[j]，并考虑 a\[L:j] 对最优解的影响。

约束划分个数时，在恰好划分成 $i$ 份时，前缀长度 $r$ 的一般合法区间为 $[i, n-(k-i)]$，最后一个划分的左端点 $l$ 的一般合法区间为 $[i, r]$。

注：对于恰好型划分 DP，可以通过控制内层循环的上下界，把时间复杂度从 O(nk) 优化至 O((n−k)k)。例如 3473 题。

## 习题
- [力扣 813. 最大平均值和的分组](https://leetcode.cn/problems/largest-sum-of-averages/) 注意初始化 想象格子转移
- [力扣 3599. 划分数组得到最小 XOR](https://leetcode.cn/problems/partition-array-to-minimize-xor/) 循环范围优化
- [力扣 410. 分割数组的最大值](https://leetcode.cn/problems/split-array-largest-sum/)
- [力扣 1278. 分割回文串 III](https://leetcode.cn/problems/palindrome-partitioning-iii/) 递归+记忆化 求 回文串价值
- [力扣 1745. 分割回文串 IV](https://leetcode.cn/problems/palindrome-partitioning-iv/) 递归+记忆化