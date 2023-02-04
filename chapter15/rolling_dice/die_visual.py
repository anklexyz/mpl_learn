"""
本节将使用Python包Plotly来生成交互式图表。需要创建在浏览器中显示的图表
时，Plotly很有用，因为它生成的图表将自动缩放以适合观看者的屏幕。Plotly生
成的图表还是交互式的：用户将鼠标指向特定元素时，将突出显示有关该元素的信
息。
"""

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# Visualize the results.
# Plotly不能直接接受函数range()的结果，
# 因此需要使用函数list() 将其转换为列表。
x_values = list(range(1, die.num_sides + 1)) # x轴的数值
# Plotly类
# Bar() 表示用于绘制条形图的数据集，需要一个存储值的列表和一个存
# 储值的列表。这个类必须放在方括号内，因为数据集可能包含多个元素。
data = [Bar(x=x_values, y=frequencies)]
# 每个坐标轴都能以不同的方式进行配置，而每个配置选项都是一个字典元素。这里
# 只设置了坐标轴标签。
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
# 类Layout() 返回一个指定图表布局和配置的对象。
# 这里设置了图表名称，并传入了 x轴和 y轴的配置字典。
my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
# 为生成图表，我们调用了函数offline.plot()。这个函数需要一个包含
# 数据和布局对象的字典，还接受一个文件名，指定要将图表保存到哪里。这里将输
# 出存储到文件d6.html。
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
