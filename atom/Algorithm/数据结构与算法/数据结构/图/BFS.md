单源、多源
01bfs
bfs+优先队列
bfs+dfs，建图+生成路径

特点是**逐层扩散**，扩散了几层，最短路就是多少
队列，单点弹出或整层弹出
需要标记状态，防止同一节点重复进出队列

可以用的特征 任意两个结点之间的相互距离相同（无向图）

开始时，可以是单源或多源

可能有剪枝策略

bfs时理解难度很低的算法，难点在于 节点如何找到路、路的展开和剪枝设计

[力扣 1162. 地图分析](https://leetcode.cn/problems/as-far-from-land-as-possible/) 多源最短路

01bfs[1824. 最少侧跳次数](https://leetcode.cn/problems/minimum-sideway-jumps/)

#atom  