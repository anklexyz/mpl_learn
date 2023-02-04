import matplotlib.pyplot as plt
#
# # 像scatter方法传递两个分别包含x值和y值的列表
# # (1,1) (2,4) (3,9) (4,16) (5,25)
# x_values=[1,2,3,4,5]
# y_values=[1,4,9,16,25]
#
# plt.style.use('seaborn')
# fig, ax=plt.subplots()
# # s就是圆点的尺寸
# ax.scatter(x_values,y_values,s=200)
#
# # 设置图表标题并给坐标轴指定标签
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记的大小
# ax.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()

# # 手工计算列表效率低下，需要绘制的点很多是更是如此。
# # 可以使用循环来完成
# x_values = range(1, 1001) # 返回一个列表
# y_values = [x**2 for x in x_values] # x的平方，每轮循环
#
# plt.style.use('seaborn')
# fig, ax=plt.subplots()
# ax.scatter(x_values,y_values,s=10) # 这个数据集很大，因此将点尺寸s=10设置的比较小
#
# # 设置图表标题并给坐标轴指定标签
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # 设置每个坐标轴的取值范围
# ax.axis([0,1100,0,1100000])
#
# plt.show()

# x_values = range(1, 1001) # 返回一个列表
# y_values = [x**2 for x in x_values] # x的平方，每轮循环
#
# plt.style.use('seaborn')
# fig, ax=plt.subplots()
# # ax.scatter(x_values,y_values,c='red',s=10) # 这个数据集很大，因此将点尺寸s=10设置的比较小
# # c=参数是手动RGB控制color的，值越接近0颜色越深，越接近1则相反
# ax.scatter(x_values,y_values,c=(0,0.8,0),s=10) # 这个数据集很大，因此将点尺寸s=10设置的比较小
#
# # 设置图表标题并给坐标轴指定标签
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # 设置每个坐标轴的取值范围
# ax.axis([0,1100,0,1100000])
#
# plt.show()

x_values = range(1, 1001) # 返回一个列表
y_values = [x**2 for x in x_values] # x的平方，每轮循环

plt.style.use('seaborn')
fig, ax=plt.subplots()

# 将参数c设置成一个y值列表，并使用参数camp告诉pyplot使用哪个颜色映射
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)

# 设置图表标题并给坐标轴指定标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0,1100,0,1100000])

# plt.show()

# 要让程序自动将图表保存到文件中，可将调用plt.show()替换为调用plt.savefig()
# 第一个实参指定要以什么文件名保存图表，这个文件将存储到scatter_squares.py所在的目录。
# 第二个实参指定将图表多余的空白区域裁剪掉。（如果要保留，省略这个实参即可）
plt.savefig('squares_plot.png', bbox_inches='tight')