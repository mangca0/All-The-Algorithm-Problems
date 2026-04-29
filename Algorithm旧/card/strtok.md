char* strtok(char* str, const char* delim)
切割函数，**本质是在对应字符位置替换为'\0'**
连续切割：
```
gets(str);
int i = 1;
p[i] = strtok(str, " ");
while(p[i] != NULL)
{
    p[++ i] = strtok(NULL, " ");//用NULL，strtok()自动记录切割位置
}
```

