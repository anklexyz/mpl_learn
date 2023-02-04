import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename='death_valley_2018_simple.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    # # 在循环中，对列表调用了enumerate()来获取每个元素的 索引index 及 其值column_header 。
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        # 你使用的很多数据集都可能缺失数据、格式不正确或数据本身不正确。对于这样的
        # 情形，可使用本书前半部分介绍的工具来处理。在这里，使用了一个try-except-else 代码块来处理数据缺失的问题。在有些情况下，需要使用continue 来跳过
        # 一些数据，或者使用remove() 或del 将已提取的数据删除。只要能进行精确而有
        # 意义的可视化，采用任何管用的方法都是可以的
        try:
            high=int(row[4])
            low=int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
