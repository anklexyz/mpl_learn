import matplotlib.pyplot as plt

# 临时修改配置让matplotlib支持中文字体
plt.rcParams["font.sans-serif"]=["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"]=False  # 该语句解决图像中的“-”负号的乱码问题

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

# subplots() 既创建了一个包含子图区域的画布，又创建了一个 figure 图形对象
fig, ax = plt.subplots()

ax.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Reds, s=10)

# 设置图表标题并给坐标轴指定标签
ax.set_title("立方", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的立方", fontsize=14)

plt.show()