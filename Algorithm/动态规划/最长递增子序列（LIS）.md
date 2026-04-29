## 模板
核心思想：**枚举选哪个**。
递推：
```python
def lengthOfLIS(self, nums: List[int]) -> int:
	n = len(nums)
	f = [0] * n # 末尾元素为 nums[i] 的 LIS 长度
	for i in range(n):
		res = 0
		for j in range(i):
			if nums[j] < nums[i
				res = max(res, f[j])
		f[i] = res + 1
	return max(f[c] for c in range(n))
```
时间复杂度：$O(n^2)$。
空间复杂度：$O(n)$。

交换状态与状态值 + 二分优化：
```python
def lengthOfLIS(self, nums: List[int]) -> int:
	n = len(nums)
	f = [] # 长度为 i+1 的 LIS 的末尾元素的最小值
	for x in nums:
		i = self.lowerBound(f, x)
		if i == len(f):
			f.append(x)
		else:
			f[i] = x
	return len(f)

def lowerBound(self, nums: List[int], x: int) -> int:
	l, r = 0, len(nums)
	while l < r:
		mid = (l + r) // 2
		if nums[mid] >= x:
			r = mid
		else:
			l = mid + 1
	return r
```
时间复杂度：$O(n\log n)$。
空间复杂度：$O(n)$。

这题是：[力扣 300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)。

## 习题
- 模板：
	- [力扣 300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/) 模板
	- [力扣 334. 递增的三元子序列](https://leetcode.cn/problems/increasing-triplet-subsequence/) 模板
	- [力扣 2826. 将三个组排序](https://leetcode.cn/problems/sorting-three-groups/) 模板
	- [力扣 2111. 使数组 K 递增的最少操作次数](https://leetcode.cn/problems/minimum-operations-to-make-the-array-k-increasing/) 模板 正难则反
		- 进阶问题：[如果本题改成严格递增要怎么做？](https://leetcode.cn/discuss/post/3169302/guan-yu-zhe-zhou-zhou-sai-di-si-ti-kdi-z-zjc6/comments/2727336/)
- [力扣 1964. 找出到每个位置为止最长的有效障碍赛跑路线](https://leetcode.cn/problems/find-the-longest-valid-obstacle-course-at-each-position/) 用二分法得到朴素法生成的数组
- [力扣 354. 俄罗斯套娃信封问题](https://leetcode.cn/problems/russian-doll-envelopes/) 
- [力扣 3825. 按位与结果非零的最长上升子序列](https://leetcode.cn/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/) 枚举比特位
- [力扣 1671. 得到山形数组的最少删除次数](https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/) 前后缀分解
- [力扣 646. 最长数对链](https://leetcode.cn/problems/maximum-length-of-pair-chain/) 元素是范围的 LIS \贪心
- [洛谷 P8776 蓝桥杯 2022 省 A 最长不下降子序列](https://www.luogu.com.cn/problem/P8776) 最长不上升 
#atom 