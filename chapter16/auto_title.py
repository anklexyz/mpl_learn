# 自动生成标题 　本节定义my_layout 时以手工方式指定标题，这
# 意味着每次变更源文件时，都需要修改标题。你可以不这样做，而是使用JSON
# 文件中元数据（metadata）部分的数据集标题。为此，可提取这个值，将其赋
# 给一个变量，并在定义my_layout 时使用这个变量来指定散点图的标题。

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

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title=all_eq_data['metadata']['title'],
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
)
fig.write_html('global_earthquakes.html')
fig.show()


if __name__ == '__main__':
    print(mags[:5])
    print(titles[:5])
    print(lons[:5])
    print(lats[:5])