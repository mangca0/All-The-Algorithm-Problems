# 两种维护方法
### dfn + siz
```
int id = 0;

void dfs(int x, int fa)
{
	siz[x] = 1;
	dfn[x] = ++ id;
	idx[dfn[x]] = x;
	for(auto &y : g[x])
	{
		if(y == fa)continue;
		dfs(y, x);
		siz[x] += siz[y];
	}
}
```
子树区间为\[dfn\[x], dfn\[x] + siz\[x] - 1]

### in + out
```
int id = 0;

void dfs(int x, int fa)
{
	in[x] = ++ id;
	idx[dfn[x]] = x;
	for(auto &y : g[x])
	{
		if(y == fa)continue;
		dfs(y, x);
	}
	out[x] = id; //回溯不消耗时间
}
```
子树区间为\[in\[x], out\[x]]

# idx
dfn、in用于真实编号找序
idx用于序找真实编号

# 性质
子树区间：若真实编号v存在于u的子树中，有in\[u] <= in\[v] <= out\[u]
拓扑性质：若in\[u] < in\[v] && out\[v] < out\[u]，有u时v的祖先