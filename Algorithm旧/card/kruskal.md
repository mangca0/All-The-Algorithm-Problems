贪心地选最小n-1条边，如构成环则跳过
需要[[并查集]]维护集合

最小生成树性质：权值和最小
kruskal性质：最大边权最小
```cpp
// 存边
struct edge{
	int x, y, w;
	bool operator < (const edge &u)const{
		return w < u.w;
	}
}
vector<edge> es;
sort(es.begin(), es.end());

// 并查集
/*

*/

// 贪心
for(const auto &[x, y, w] : es)
{
	// 若xy已经在一个集合里，连接会成环
	if(find(x) == find(y))continue;

	// merge
	x = fing(x), y = find(y);
	fa[y] = x;

	// 按题目
	/*
	ans = max(ans, w);
	*/
}
```