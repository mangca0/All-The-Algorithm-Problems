# Java IO - 字节输出流 FileOutputStream
作用：可以把程序的数据写到文件中，是字节流的基本流。

| **构造方法摘要**                                                                                                    |
| :------------------------------------------------------------------------------------------------------------ |
| `FileOutputStream(File file)`<br>          创建一个向指定 `File` 对象表示的文件中写入数据的文件输出流。                                 |
| `FileOutputStream(File file, boolean append)`  <br>          创建一个向指定 `File` 对象表示的文件中写入数据的文件输出流。               |
| `FileOutputStream(FileDescriptor fdObj)`  <br>          创建一个向指定文件描述符处写入数据的输出文件流，该文件描述符表示一个到文件系统中的某个实际文件的现有连接。 |
| `FileOutputStream(String name)`  <br>          创建一个向具有指定名称的文件中写入数据的输出文件流。                                     |
| `FileOutputStream(String name, boolean append)`  <br>          创建一个向具有指定 `name` 的文件中写入数据的输出文件流。               |

## 书写步骤、细节
1. 创建字节输出流对象。
	  - 参数可以是字符串或者是 File 对象。
	  - 如果指定路径下文件不存在，则会新建一个文件。但需要保证父级路径存在。
	  - 如果文件已经存在，则会清空文件。
2. 写数据。
	  - write 方法参数是整数，实际为 ASCII 码对应字符。
3. 释放资源。
	- 每次使用完流之后都要释放资源。

### 调用 write 方法的的三种方式
```java
void write(int b)
void write(byte[] b)
void write(byte[] b, int off, int len) // 将指定 byte 数组中从偏移量 off 开始的 len 个字节写入此文件输出流。
```

将 String 书写进文件：
```java
String str = "abc123";
byte[] bytes = str.getBytes();
```

### 换行和续写
不同系统中的换行符：
Windows：\r\n
Linux：\n
MacOS：\r
在 Java 中\r、\n会自动补齐。

需要续写就要**打开续写开关**，开关位于创建对象的第二个参数，默认false，传入true就不会清空，而是续写。

#atom 
