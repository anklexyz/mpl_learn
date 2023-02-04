import csv

filename='sitka_weather_2018_simple.csv'
with open(filename) as f:
    # reader返回一个迭代（每次一行）的文件对象
    reader=csv.reader(f)
    # next()每次返回迭代器的下一项
    header_row=next(reader)
    # print(header_row)

# # 在循环中，对列表调用了enumerate()来获取每个元素的 索引index 及 其值column_header 。
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# 从中可知，日期和最高温度分别存储在第三列和第六列。为研究这些数据，我们将
# 处理sitka_weather_07-2018_simple.csv中的每行数据，并提取其中索引为2和5的
# 值。

    # 从文件中获取每天的最高温度。
    highs = []
    for row in reader: # reader返回一行，以列表形式储存在row中
        # 第6列赋值给high，将high追加到highs这个[]列表
        high=int(row[5])
        highs.append(high)

print(highs)
