```
import pandas as pd  
import numpy as np  
  
# 1. 读取数据  
df = pd.read_excel("data.xlsx", sheet_name="Sheet2", header=None)  
  
# 2. 去掉第一行（标题行）  
df = df.iloc[1:]  # 从第二行开始  
  
# 3. 将第三列（索引为2）的数据转换为数值类型  
avg = df[2].astype(float).values.reshape(10, 4)  
  
# 4. 打印结果  
print("矩阵形状:", avg.shape)  
print("\n矩阵内容:")  
print(avg)  
  
# 5. 如果需要，可以设置打印精度  
np.set_printoptions(precision=6, suppress=True)  
print("\n设置精度后的矩阵内容:")  
print(avg)
```

![[Pasted image 20241216163709.png]]