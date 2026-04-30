## 算法思路
用 **选或不选** 的思想。

考虑最后一对字母 $s[i]$ 和 $s[j]$，有这几种情况： $\begin{cases} 不选s[i]，不选t[j] \\ 不选s[i]，选t[j] \\选s[i]，不选t[j] \\ 选s[i]，选t[j] \end{cases}$。

此时 **都选** 和 **都不选** 的子问题是一样的，但 **都选** 明显要比 **都不选** 优秀，于是就有转移方程：
$$dfs(i, j) = \begin{cases}
max(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1) + 1) & s[i] = t[j]\\
max(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) & s[i] \neq t[j]
\end{cases}$$

当 $s[i]=t[j]$ 时，$dfs(i - 1, j)、dfs(i, j - 1)$ 是可以被省略的，因为 $dfs(i - 1, j)/dfs(i, j - 1)$ 不会比 $dfs(i - 1, j - 1) + 1$ 更优。
当 $s[i] \ne t[j]$ 时，$dfs(i - 1, j - 1)$ 是可以被省略的，因为 $dfs(i - 1, j - 1)$ 已经被包括在 $dfs(i - 1, j)/dfs(i, j - 1)$ 里了。

于是就有转移方程：
$$dfs(i, j) = \begin{cases}
dfs(i - 1, j - 1) + 1 & s[i]=t[j] \\
max(dfs(i - 1, j), dfs(i, j - 1)) & s[i] \neq t[j]
\end{cases}$$

推荐参考 [SourceForge 的 LCS 交互网页](http://lcs-demo.sourceforge.net/) 来更好地理解 LCS 的实现过程。

## 模板
以下时间复杂度均为 $O(mn)$。

记忆化搜索：
```python
m, n = len(text1), len(text2)
@cache
def dfs(i: int, j: int) -> int:
	if i < 0 or j < 0:
		return 0
	if text1[i] == text2[j]:
		return dfs(i - 1, j - 1) + 1
	return max(dfs(i - 1, j), dfs(i, j - 1))
return dfs(m - 1, n - 1)
```

递推（无空间优化）：
```python
m, n = len(text1), len(text2)
f = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
	for j in range(1, n + 1):
		if text1[i - 1] == text2[j - 1]:
			f[i][j] = f[i - 1][j - 1] + 1
		else:
			f[i][j] = max(f[i - 1][j], f[i][j - 1])
return f[m][n]
```

LCS 也可以像背包那样，把空间优化成一个数组。

在实现空间优化时，如果单纯从左往右，或从右往左更新一维数组，都不能满足 依赖**左、上、左上**三个位置。

我们可以用一个临时变量 $pre$ 来存储 **左上** 的信息，并从左往右遍历。

一维数组优化：
```python
# 用较小的长度 作为dp数组的长度
m, n = len(text1), len(text2)
if n > m:
	tmp = text1
	text1 = text2
	text2 = tmp
	tmp = m
	m = n
	n = tmp

f = [0] * (n + 1)
for i in range(1, m + 1):
	pre = 0
	for j in range(1, n + 1):
		cur = f[j]
		if text1[i - 1] == text2[j - 1]:
			f[j] = pre + 1
		else:
			f[j] = max(f[j], f[j - 1])
		pre = cur
return f[n]
```

这题是 [力扣 1143. 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/)。

# 习题
核心思路：**选或不选**

- [力扣 1143. 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/) 模板
	- 字符串操作问题：
		- [力扣 583. 两个字符串的删除操作](https://leetcode.cn/problems/delete-operation-for-two-strings/) 删除操作
		- [力扣 712. 两个字符串的最小ASCII删除和](https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/) ASCII 码背景下的 LCS
		- 以上两题都可以通过 正难则反 + LCS，或直接 DP 解决
		- [力扣 72. 编辑距离](https://leetcode.cn/problems/edit-distance/) 
		- [力扣 115. 不同的子序列](https://leetcode.cn/problems/distinct-subsequences/) 只能对其中一个字符串进行删除操作
		- [力扣 3628. 插入一个字母的最大子序列数](https://leetcode.cn/problems/maximum-number-of-subsequences-after-one-inserting/) 115 题的变种，插入策略和前后缀分解
		- [力扣 97. 交错字符串](https://leetcode.cn/problems/interleaving-string/) 用两个样本固定第三个样本
	- [力扣 1035. 不相交的线](https://leetcode.cn/problems/uncrossed-lines/) LCS
	- 数列乘积问题：
		- [力扣 1458. 两个子序列的最大点积](https://leetcode.cn/problems/max-dot-product-of-two-subsequences/) 初始化和表达序列非空
		- [力扣 3290. 最高乘法得分](https://leetcode.cn/problems/maximum-multiplication-score/) 初始化和表达选择数列的所有
	- [力扣 718. 最长重复子数组](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/) 子数组默认连续




#atom 