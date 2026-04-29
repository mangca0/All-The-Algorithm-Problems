离线查询区间最值，本质是[[区间DP]]. [[倍增]]思想
预处理O(nlogn)，查询O(1)
# 可解决
==ST 表是用于解决 **可重复贡献问题** 的数据结构==
即满足 x opt x = x
**区间max, min, |, &, gcd**

# 构建
st\[i]\[j]表示从i开始，长度为2^j的区间最值，即\[i, i+2^j-1]
```
//初始化
for(int i = 1; i <= n; i ++)st[i][0] = 1;

//枚举j且必须顺序，枚举范围取决于题目数据
for(int j = 1; j <= 20; j ++)
	//i无所谓
	for(int i = 1; i <= n; i ++)
		//合法性判断
		if(i + (1 << j) - 1 <= n)
			//状态转移，从j-1到j
			st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
```

# 查询
2^k + 2^k > r - l + 1
```
inline int getMax(int l, int r)
{
	int k = log(r - l + 1) / log(2);
	return max(st[l][k], st[r - (1 << k) + 1][r])
}
```

# 可更新ST表

[[洛谷 P1198 [JSOI2008] 最大数]]

若在ST表末端插入元素，则不会改变原有ST表，只需要**更新所有==以插入点为右端点==的ST数组**
即有$i+2^j-1=n$
```
inline void ins(int num)
{
	st[++ n][0] = num;
	for(int j = 1; j <= 20; j ++)
	{
		int i = n - (1 << j) + 1;
		//确定右端点，倒推左端点，确保左端点合法
		if(i >= 0)
			st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
	}
}
```
