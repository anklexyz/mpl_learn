import json
import plotly.express as px
import pandas as pd


filename = 'eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

# eq_explore_data的做法是在Plotly Express中给图表定义数据的最简单方式之一，但在数据处理中并不
# 是最佳的。下面是另一种给图表定义数据的等效方式，需要使用pandas数据分析工
# 具。首先创建一个DataFrame ，将需要的数据封装起来：
data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)

# fig =px.scatter(
#     x=lons,
#     y=lats,
#     labels={"x":"经度","y":"维度"},
#     range_x=[-200,200],
#     range_y=[-90,90],
#     width=800,
#     height=800,
#     title="全球地震散点图"
# )

# 然后，参数配置方式可以变更为：
fig = px.scatter(
    data,  # 打包的对象
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
)
# 在这种方式中，所有有关数据的信息都以键值对的形式放在一个字典中。如果在
# eq_plot.py中使用这些代码，生成的图表是一样的。相比于前一种格式，这种格式
# 让我们能够无缝衔接数据分析，并且更轻松地进行定制。

# 上面配置时使用了
# size 参数来指定散点图中每个标记的尺寸，我们只需要将前面data 中的"震级"
# 字段提供给size 参数即可

# 为了让标记的震级按照不同的颜色
# 显示，只需要配置color="震级" 即可。默认的视觉映射图例渐变色范围是从蓝到
# 红再到黄，数值越小则标记越蓝，而数值越大则标记越黄

# 为完成这幅散点图的绘制，我们将添加一些说明性文本，在你将鼠标指向表示地震
# 的标记时显示出来。除了默认显示的经度和纬度外，还将显示震级以及地震的大致
# 位置
# Plotly Express的操作非常简单，只需要将hover_name 参数配置为data 的"位
# 置" 字段即可。

# 将图形写入HTML文件表示
# Write a figure to an HTML file representation
fig.write_html('global_earthquakes.html')
# 使用默认渲染器或renderer参数指定的渲染器显示图形
fig.show()


if __name__ == '__main__':
    print(mags[:5])
    print(titles[:5])
    print(lons[:5])
    print(lats[:5])