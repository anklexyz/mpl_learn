# 模块json 提供了各种探索和处理JSON数据的工具，其中一些有助于重新设置这个
# 文件的格式，让我们能够更清楚地查看原始数据，继而决定如何以编程的方式来处
# 理。
import json

filename = 'data/eq_data_30_day_m1.json'
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


if __name__ == '__main__':
    print(mags[:5])
    print(titles[:5])
    print(lons[:5])
    print(lats[:5])
