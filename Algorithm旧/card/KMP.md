# kmp
**构建next数组 & 字符串匹配**核心都是kmp算法

下标均从1开始
j为已匹配长度 & 判断位置的前一位

### 构建next数组
```
next[0] = next[1] = 0;
for(int i = 2, j = 0; i <= s2.length(); i ++)
{
	//kmp模板
	while(j && s2[i] != s2[j + 1])
		j = next[j];
	if(s2[i] == s2[j + 1])
		j ++;

	//构建next数组
	next[i] = j;
}
```

### 字符串匹配
```
for(int i = 1, j = 0; i <= s1.length(); i ++)
{
	//kmp模板
	while(j && s2[i] != s2[j + 1])
		j = next[j];
	if(s2[i] == s2[j + 1])
		j ++;

	//字符串匹配
	if(j == s2.length())
	{
		cout << i - j + 1 << endl; //匹配位置
		return;
	}
}
```

