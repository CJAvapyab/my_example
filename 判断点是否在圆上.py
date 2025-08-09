x = float(input("输入x:"))  # 转换为float
y = float(input("输入y:"))  # 转换为float

distance_squared = (x-3)**2 + (y+2)**2  # 使用**表示平方
distance = distance_squared ** 0.5  # 计算实际距离（平方根）

if distance_squared == 16:
    print("在圆上")
elif distance_squared > 16:
    print(f"在圆外，距圆心为{distance}")  # 使用正确的变量名
else:
    print(f"在圆内，距圆心为{distance}")  # 使用正确的变量名
