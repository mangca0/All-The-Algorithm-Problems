## 买卖股票
状态设计：$dfs(i, j, k)$，前 $i$ 天，状态为 $j,(j=1表示持有状态，j=0表示非持有状态)$，已经交易了 $k$ 次的最大利润。
初始化：$dfs(0,0,k)=0$，前 $0$ 天未持有的最大利润为 $0$；$dfs(0,1,k)=-inf$，前 $0$ 天持有的最大利润为 $-\infty$（不存在这种可能）。

### 习题
- [力扣 122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/) 状态机 DP 模板
- [力扣 188. 买卖股票的最佳时机 IV](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/) 交易 $k$ 次模板
- [力扣 121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) 交易 1 次
- [力扣 123. 买卖股票的最佳时机 III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/) 交易 2 次
- [力扣 3573. 买卖股票的最佳时机 V](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-v/) 状态机 DP 设计
- [力扣 309. 买卖股票的最佳时机含冷冻期](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/) 状态机 DP 设计
- [力扣 714. 买卖股票的最佳时机含手续费](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) 模板

## 其他
### 习题
- **基础**
	- [力扣 3259. 超级饮料的最大强化能量](https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/) 模板
	- [力扣 2222. 选择建筑的方案数](https://leetcode.cn/problems/number-of-ways-to-select-buildings/) 恰好 $k$ 次模板/简单做法
	- [力扣 2708. 一个小组的最大实力值](https://leetcode.cn/problems/maximum-strength-of-a-group/) 选或不选分支，非空子序列
	- [力扣 1567. 乘积为正数的最长子数组长度](https://leetcode.cn/problems/maximum-length-of-subarray-with-positive-product/) 子数组
	- [力扣 2786. 访问数组中的位置使分数最大](https://leetcode.cn/problems/visit-array-positions-to-maximize-score/) 注意初始状态，严格状态定义
	- [力扣 1911. 最大交替子序列和](https://leetcode.cn/problems/maximum-alternating-subsequence-sum/) 模板，选或不选
- **进阶**
	- [力扣 376. 摆动序列](https://leetcode.cn/problems/wiggle-subsequence/) **枚举选哪个**。可以做到 $O(n)$
	- [力扣 3628. 插入一个字母的最大子序列数](https://leetcode.cn/problems/maximum-number-of-subsequences-after-one-inserting/) 难以理解



#atom 