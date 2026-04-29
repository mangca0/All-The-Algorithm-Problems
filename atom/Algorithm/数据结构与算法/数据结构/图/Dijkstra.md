是一种求解**非负权图**上单源最短路径的算法。既适用于无向图也适用于有向图，无向图可视为双向边。

最短路不仅限于**路径边权和**的**最小值**，也可以是**路径点权最大值**、**路径边权最大值**的**最小值**。

## 灵魂的统一
最短路和 DP 都是贝尔曼方程（最优子结构）在不同图拓扑结构下的具象表现。

从本质上说，**DP 问题是一类特殊的图论问题。**

DP 问题虽然都属于图论范畴，但对于不是拓扑图的图论问题，我们无法使用 DP 求解。

更严谨和准确的说法应该是：
1. **动态规划（狭义）** = DAG 上的最短/最长路径求解。
2. **最短路算法** = 为了解决图论中**出现环（后效性）**时，普通 DP 无法推导拓扑序的问题，而衍生出来的**特殊状态方程求解器**（Dijkstra 用贪心定序，Bellman-Ford 用迭代收敛）。

**最短路就是在有环图上做 DP，而 DP 就是在 DAG（有向无环图）上求最短路。**


Dijkstra 算法的底层逻辑是**贪心 + BFS**

## 算法过程
将顶点分成两个集合：已确定最短路长度的点集（记为 $S$ 集合）的和未确定最短路长度的点集（记为 $T$ 集合）。一开始所有的点都属于 $T$ 集合。

初始化 $dis(st)=0$，其他点的 $dis$ 均为 $+\infty$。$st$ 代表原点，$dis$ 为原点到某点的最短距离。
然后重复这些操作：
1. 从 $T$ 集合中，选取一个最短路长度最小的结点，移到 $S$ 集合中。
2. 用那些刚刚被加入 $S$ 集合的结点的所有出边更新 $dis$（执行松弛操作）。

直到 $T$ 集合为空，算法结束。

## 实现
Dijkstra 并不是一下子求出源点到目标点的最短路径，而是一步步求出它们之间顶点的最短路径，过程中都是基于已求出的最短路径的基础上，求得更远点的最短路径。

Dijkstra 有适用于**稠密图**的朴素写法 $O(n^2)$；也有适用于**稀疏图**的堆优化版本 $O(m\log m)$。其中 $n$ 为图中顶点数，$m$ 为图中边数。

### 朴素实现
朴素的实现方法为每次 2 操作执行完毕后，直接在 $T$ 集合中**暴力**寻找最短路长度最小的结点。2 操作总时间复杂度为 $O(m)$，1 操作总时间复杂度为 $O(n^2)$，全过程的时间复杂为 $O(n^2)$。
```cpp
struct edge {
	int v, w;
};

vector<edge> e[N]; // 邻接表
int dis[MAXN], vis[N];

void dijkstra(int n, int s)
{
	// 初始化
	memset(dis, 0x3f, (n + 1) * sizeof(int));
	dis[s] = 0;
	
	for (int i = 1; i <= n; i++)
	{
		int u = 0, mi = 0x3f3f3f3f;
	    for (int j = 1; j <= n; j++)
		    if (!vis[j] && dis[j] < mi) u = j, mi = dis[j];
	    vis[u] = true;
	    for (auto edge : e[u])
	    {
		    int v = edge.v, w = edge.w;
			if (dis[v] > dis[u] + w) dis[v] = dis[u] + w;
	    }
	}
}
```

这里有一个比较完整的，适用于 PTA 读写，C 语言的版本，这题中遵循 “D 因素优先、P 因素次之”，采用「邻接矩阵」+「朴素 Dijkstra」。
这题是：PTA 7-1 旅游规划，***可以折磨一下自己（***。
```c
#include "stdio.h"
#include "stdlib.h"
#define INFINITY 65535

int main(void)
{   
    int n, m, s, t;
    scanf("%d %d %d %d", &n, &m, &s, &t);
    int g[n + 10][n + 10][2];
    for(int i = 0; i < n; i ++)
    {
        for(int j = 0; j < n; j ++)
        {
            if(i == j)g[i][j][0] = g[i][j][1] =0;
            else g[i][j][0] = g[i][j][1] = INFINITY;
        }
    }
    for(int k = 0; k < m; k ++)
    {
        int u, v, i, j;
        scanf("%d %d %d %d", &u, &v, &i, &j);
        g[u][v][0] = g[v][u][0] = i;
        g[u][v][1] = g[v][u][1] = j;
    }

    int D[n + 10], P[n + 10];
    
    int v,w,k,min;
    int vis[n + 10];
    for(int i = 0; i < n; i ++)
    {        
        vis[i] = 0;
        D[i] = P[i] = INFINITY;
    }
    D[s] = P[s] = 0;
    vis[s] = 1;
    for(int i = 0; i < n; i ++)
    {
        int u = s, minD = INFINITY, minP = INFINITY;
        for(int j = 0; j < n; j ++)
            if(!vis[j] && (D[j] < minD || D[j] == min && P[j] < minP))
                u = j, minD = D[j], minP = P[j];
        vis[u] = 1;
        for(int v = 0; v < n; v ++)
        {
            if(g[u][v][0] == INFINITY)continue;
            int d = g[u][v][0], p = g[u][v][1];
            if(D[u] + d < D[v] || D[u] + d == D[v] && P[u] + p < P[v])
                D[v] = D[u] + d, P[v] = P[u] + p;
        }
    }
    
    printf("%d %d\n", D[t], P[t]); 
    return 0;
}
```

### 优先队列实现
时间复杂度：$O(m\log m)$，优点是实现较简单。

使用优先队列维护时，每个节点最多只出队更新周围一次。即可以通过每次松弛时重新插入该结点，且弹出时检查该结点是否已被松弛过（或直接判断是否有 $du > dis[u]$，则不需要 $vis$ 数组），若是则跳过。

```java
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
ArrayList<int[]>[] g = new ArrayList[N];
boolean[] vis = new boolean[N];
int[] dis = new int[N];

// 假设源点为 st
// 初始化
pq.offer(new int[]{st, 0});
Arrays.fill(dis, Integer.MAX_VALUE);
dis[st] = 0;
for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();

// Dijkstra
while(!pq.isEmpty()) {
	int u = pq.poll()[0];
	if(vis[u]) continue;
	// if(du > dis[u]) continue; 这条判断与 vis 同作用
	vis[u] = true;

	for (int[] edge : g[u]) {
		int v = edge[0], w = edge[1];
		if (dis[u] + w < dis[v]) { // 没作为过松弛源点，且此路径够优秀
			dis[v] = dis[u] + w;
			pq.offer(new int[]{v, dis[v]});
		}
	}
}
```

为什么代码要判断 `if(vis[u])`/ `if(du > dis[u])` ？
- 对于同一个 x，例如先入堆一个比较大的 $dis[x]=10$，后面又把 $dis[x]$ 更新成 $5$，之后这个 $5$ 会先出堆，然后再把 10 出堆。10 出堆时候是没有必要去更新周围邻居的最短路的，因为 5 出堆之后，就已经把邻居的最短路更新过了，用 10 是无法把邻居的最短路变得更短的，所以直接 continue。

```cpp
#define inf 2e18;  
struct node  
{  
    int x, w;  
    bool operator <(const node u) const  
    {  
        if (w == u.w)return x < u.x; // 无所谓  
        return w > u.w; // 默认是大根堆，需要升序排列  
    }  
};  

vector<node> g[N]; // 邻接表  
priority_queue<node> pq; // 堆优化  
bool vis[N]; // 是否作为过松弛源点  
int dis[N];  

inline void dijkstra(int st) // st为单源点  
{  
    for (int i = 1; i <= n; i++)dis[i] = inf;  
    pq.push({st, dis[st] = 0});  
    while (pq.size())  
    {  
        int u = pq.top().x;  
        pq.pop();  
        if (vis[u]) continue;  
        vis[u] = 1;  
        // 上两行等价于：if (du > dis[u]) continue;

        // x可以作为松弛出发点  
        for (const auto& edge : g[u])  
        {  
            int v = edge.x, w = edge.w;  
            if (dis[u] + w < dis[v])  
            {  
                dis[v] = dis[u] + w;  
                pq.push({v, dis[v]}); // 贪心：y可作为下个拓展出发点  
            }  
        }  
    }  
}
```

## 反向索引堆优化
时间复杂度：$O(m\log n)$，比优先队列实现更优秀。



## 正确性证明

下面用数学归纳法证明，在 **所有边权值非负** 的前提下，$Dijkstra$ 算法的正确性。

记 $D(u)$ 为源点 $st$ 到 $u$ 的实际最短路。

简单来说，我们要证明的，就是在执行 $1$ 操作时，取出的结点 $u$ 最短路均已经被确定，即满足 $D(u)=dis(u)$。

初始时 $S=\varnothing$，假设成立。

接下来用反证法。

设 $u$ 点为算法中第一个在加入 $S$ 集合时不满足 $D(u)=dis(u)$ 的点。因为 $st$ 点一定满足 $D(st)=dis(st)=0$，且它一定是第一个加入 $S$ 集合的点，因此将 $u$ 加入 $S$ 集合前，$S\neq\varnothing$，如果不存在 $st$ 到 $u$ 的路径，则 $D(u)=dis(u)=+\infty$，与假设矛盾。

于是一定存在路径 𝑠 →𝑥 →𝑦 →𝑢，其中 𝑦 为 𝑠 →𝑢 路径上第一个属于 𝑇 集合的点，而 𝑥 为 𝑦 的前驱结点（显然 𝑥 ∈𝑆）。需要注意的是，可能存在 𝑠 =𝑥 或 𝑦 =𝑢 的情况，即 𝑠 →𝑥 或 𝑦 →𝑢 可能是空路径。

因为在 𝑢 结点之前加入的结点都满足 𝐷(𝑢) =𝑑𝑖𝑠(𝑢)，所以在 𝑥 点加入到 𝑆 集合时，有 𝐷(𝑥) =𝑑𝑖𝑠(𝑥)，此时边 (𝑥,𝑦) 会被松弛，从而可以证明，将 𝑢 加入到 𝑆 时，一定有 𝐷(𝑦) =𝑑𝑖𝑠(𝑦)。

下面证明 𝐷(𝑢) =𝑑𝑖𝑠(𝑢) 成立。在路径 𝑠 →𝑥 →𝑦 →𝑢 中，因为图上所有边边权非负，因此 𝐷(𝑦) ≤𝐷(𝑢)。从而 𝑑𝑖𝑠(𝑦) =𝐷(𝑦) ≤𝐷(𝑢) ≤𝑑𝑖𝑠(𝑢)。但是因为 𝑢 结点在 1 过程中被取出 𝑇 集合时，𝑦 结点还没有被取出 𝑇 集合，因此此时有 𝑑𝑖𝑠(𝑢) ≤𝑑𝑖𝑠(𝑦)，从而得到 𝑑𝑖𝑠(𝑦) =𝐷(𝑦) =𝐷(𝑢) =𝑑𝑖𝑠(𝑢)，这与 𝐷(𝑢) ≠𝑑𝑖𝑠(𝑢) 的假设矛盾，故假设不成立。

因此我们证明了，1 操作每次取出的点，其最短路均已经被确定。命题得证。

注意到证明过程中的关键不等式 𝐷(𝑦) ≤𝐷(𝑢) 是在图上所有边边权非负的情况下得出的。当图上存在负权边时，这一不等式不再成立，Dijkstra 算法的正确性将无法得到保证，算法可能会给出错误的结果。

[正确性证明](https://oi-wiki.org/graph/shortest-path/#%E6%AD%A3%E7%A1%AE%E6%80%A7%E8%AF%81%E6%98%8E)

## 习题
- 基础
	- [力扣 743. 网络延迟时间](https://leetcode.cn/problems/network-delay-time/) 模板题
- 进阶
	- 传统 Dijkstra 计算的是**路径边权和**的**最小值**，也可以求**路径点权最大值**、**路径边权最大值**的**最小值**。
	- [力扣 1631. 最小体力消耗路径](https://leetcode.cn/problems/path-with-minimum-effort/) 路径上的最大边作为长度
	- [力扣 778. 水位上升的泳池中游泳](https://leetcode.cn/problems/swim-in-rising-water/) 同 1631

#atom