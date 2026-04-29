c不能将数组赋值给数组
strcpy是字符数组的特例
memcpy、memmove可处理任何类型的数组，**因为他们不知道也不关心数据的类型，仅仅是把字节从一个地方移到另一个地方。**
void * memcpy(void * **restrict** s1, const void * **restrict** s2, size_t n)
void * memmove(void * s1, const void * s2, size_t n)
n为字节数
**memcpy和strcpy处理重叠区域时未定义， 请用memmove**
memmove利用了缓冲区，擅长处理重叠区域