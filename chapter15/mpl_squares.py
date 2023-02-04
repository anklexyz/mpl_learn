import matplotlib.pyplot as plt

# 临时修改配置让matplotlib支持中文字体
plt.rcParams["font.sans-serif"]=["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"]=False  # 该语句解决图像中的“-”负号的乱码问题

# 创建一个名为squares的列表。在其中存储用来制作图表的数据。
input_values=[1,2,3,4,5]
squares = [1,4,9,16,25]

# # seaborn背景色
# plt.style.use('seaborn')

# 调用subplots--这个函数可在一张图片中绘制一个或多个图表
# fig表示整张图片，ax表示图片中的各个图表
fig,ax=plt.subplots() # 使用元组返回的多个值

# 调用plot方法，根据给定的数据以”有意义“的方式绘制图表
# linewidth决定了绘制线条的粗细
ax.plot(input_values,squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小。
# 影响x和y轴的刻度，并将刻度标记的字号设置为14
ax.tick_params(axis='both', labelsize=14)

# show方法打开matplotlib查看器并显示绘制的图表
plt.show()