# Java IO - 字节输入流 FileInputStream
可以把本地文件中的数据读取到程序中。

## 使用细节
1. 创建字节输入流对象。
	- 如果文件不存在，直接报错。 
2. 读取数据（read）。
	- 一次只读一个字节，返回为字符在 ASCII 码上对应的数字。
	- 读到文件末尾时返回-1。
3. 释放资源。

## 循环读取
```java
FileInputStream fis = new FileInputStream(); // 传入 File 对象或路径 String

int b;
while((b = fis.read()) != -1) {
	System.out.print((char) b);
}

fis.close();
```

## 方法详细信息
![[Pasted image 20251223180831.png]]
![[Pasted image 20251223180925.png]]

#atom 