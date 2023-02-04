import json

filename='eq_data_1_day_m1.json'
with open(filename) as f:
    # 原来格式人类看不懂，但可以用
    # .load格式化加载到python中
    all_eq_data=json.load(f)

# readable_file='readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)
#     # 这个文件的开头是一个键为"metadata" 的片段，指出了这个数据文件是
#     # 什么时候生成的，以及能够在网上的什么地方找到。它还包含适合人类阅读的标题
#     # 以及文件中记录了多少次地震：在过去的24小时内，发生了158次地震。

# all_eq_data这个字典中键'features'的对应的值是 列表
all_eq_dicts=all_eq_data['features']
# print(len(all_eq_dicts))

mags,titles,lons,lats=[],[],[],[]
for eq_dict in all_eq_dicts:
    # 可以理解为二维数组，properties那行下的mag那列
    # eq_dict字典中键为properties的值是一个嵌套字典，嵌套字典中键为map的值value赋给mag变量
    mag=eq_dict['properties']['mag']
    mags.append(mag)  # 追加到mags列表中

    title=eq_dict['properties']['title']
    titles.append(title)

    lon=eq_dict['geometry']['coordinates'][0]
    lons.append(lon)

    lat = eq_dict['geometry']['coordinates'][1]
    lats.append(lat)

# print(mags[:10])  # 遍历前0-9个数据，一共10个数据
# print(titles[:2])
# print(lons[:5])
# print(lats[:5])

# 首先，导入plotly.express ，用别名px 表示。Plotly Express是Plotly的高级
# 接口，简单易用，语法与Matplotlib类似。
import plotly.express as px
# 调用px.scatter 函数，配置参数创建一个fig 实例
fig =px.scatter(
    x=lons,
    y=lats,
    labels={"x":"经度","y":"维度"},
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title="全球地震散点图"
)# 分别设置 轴为经度［范围是[-200, 200] （扩大
# 空间，以便完整显示东西经180°附近的地震散点）］、 轴为纬度［范围是[-90,
# 90] ］，设置散点图显示的宽度和高度均为800像素，并设置标题为“全球地震散点
# 图”

# scatter返回了一个fig 对象
# fig.write_html 方法可以将可视化图保存为html文件。
fig.write_html("global_earthquakes.html")
fig.show()


