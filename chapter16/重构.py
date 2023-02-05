import json

filename='eq_data_1_day_m1.json'
with open(filename) as f:
    # 原来格式人类看不懂，但可以用
    # .load格式化加载到python中
    all_eq_data=json.load(f)

all_eq_dicts=all_eq_data['features']

mags=[eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
titles=[eq_dict['properties']['title'] for eq_dict in all_eq_dicts]
lons=[eq_dict['geometry']['coordinates'] for eq_dict in all_eq_dicts][0]
lats=[eq_dict['geometry']['coordinates'] for eq_dict in all_eq_dicts][1]

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
)

fig.write_html("global_earthquakes.html")
fig.show()


