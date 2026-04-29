适合于解决两个点之间的最短路径问题。因为是一步一步往外走，所以==**bfs本身自带最短路径的属性**==

```cpp
int dir[][] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
void bfs(int x, int y, int g[][], int vis[][])
{
	queue<pair<int, int>> q;
	q.push({x, y});
	vis[x][y] = 1;
	while(q.size())
	{
		auto cur = q.front();q.pop();
		for(int i = 0; i < 4; i ++)
		{
			int nx = cur.first + dir[i][0];
			int ny = cur.second + dir[i][1];
			if(1 <= nx && nx <= n && 1 <= ny && ny <= n)
				if(!vis[nx][ny])
				{
					q.push({nx, ny});
					vis[nx][ny] = 1;
				}
		}
	}
}
```