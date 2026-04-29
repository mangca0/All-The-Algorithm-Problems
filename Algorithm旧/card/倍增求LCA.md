**利用LCA可求树上路径权值和**
关联：[[区间DP]]、[[倍增]]
最近公共祖先
fa\[x]\[i]意味着从x向上走2^i步
2^20～1e6
# 确定深度关系，预处理fa
```cpp
inline void dfs(int x, int p)
{
	dep[x] = dep[p] + 1; //更新dep
	fa[x][0] = p; //初始化fa
	for(int i = 1; i <= 20; i ++) //更新fa
		fa[x][i] = fa[fa[x][i - 1]][i - 1]; //找爷爷->找爸爸的爸爸
	for(auto &y : g[x])
	{
		if(y == p)continue;
		dfs(y, x);
	}
}
```

# 统一深度，倍增求LCA
**LCA部分的枚举均从大到小，贪心的跳**
```cpp
inline int lca(int a, int b)
{
	//统一深度
	if(dep[a] < dep[b])swap(a, b); //确保a深
	for(int i = 20; i >= 0; i --)
		if(dep[fa[a][i]] >= dep[b])
			a = fa[a][i];

	//特判
	if(a == b)return a;
	
	//求LCA
	for(int i = 20; i >= 0; i --)
		if(fa[a][i] != fa[b][i]) //不相等就更新，确保求的是最近祖先
			a = fa[a][i], b = fa[b][i];

	//LCA为a的父亲
	return fa[a][0];
}
```

# 暴力 朴素
统一深度，一起上移，直到相等