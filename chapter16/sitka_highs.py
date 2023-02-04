# import csv
# from datetime import datetime
#
# import matplotlib.pyplot as plt
#
# filename = 'sitka_weather_07-2018_simple.csv'
# with open(filename) as f:
#     reader=csv.reader(f)
#     header_row = next(reader)
#
#     # 从文件中获取每天的日期和最高温度。
#     dates, highs = [], []
#     for row in reader: # reader返回一行，以列表形式储存在row中
#         current_date = datetime.strptime(row[2], '%Y-%m-%d')
#         # 第6列赋值给high，将high追加到highs这个[]列表
#         high=int(row[5])
#         dates.append(current_date)
#         highs.append(high)
#
#     plt.style.use('seaborn')
#     # subplots获取一个画布
#     # fig代表整个图像，ax代表坐标轴和画的图
#     fig, ax = plt.subplots()
#     # 在ax上的子区域画图
#     ax.plot(dates, highs,c='red')
#
#     ax.set_title("Maximum daily temperatures for July 2018", fontsize=24)
#     ax.set_xlabel('',fontsize=16)
#     # 调用fig.autofmt_xdate() 来绘制倾斜的日期标签，
#     # 以免其彼此重叠。
#     fig.autofmt_xdate()
#     ax.set_ylabel("Temp(F)",fontsize=16)
#     ax.tick_params(axis='both',which='major',labelsize=16)
#
#     plt.show()
#     # 现在图表的x轴上有日期，含义更丰富


# 1、用subplots新建一块画板，fig,ax接收
# 2、用ax.plot(dates,highs,c='red',alpha=0.5)在画板上建画布
# 3、设置坐标名称等
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename='sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row = next(reader)

    dates,highs,lows=[],[],[]

    for row in reader:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        high=int(row[5])
        low=int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # plt.style.use('seaborn')
    fig,ax=plt.subplots()
    ax.plot(dates,highs,c='red',alpha=0.5)
    ax.plot(dates,lows,c='blue',alpha=0.5)
    # 添加两个数据系列后，就可以知道每天的温度范围了。下面来给这个图表做最后的
    # 修饰，通过着色来呈现每天的温度范围。为此，将使用方法fill_between() 。
    # 它接受一个 值系列和两个 值系列，并填充两个 值系列之间的空间：
    ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    ax.set_title("2018 daily temp",fontsize=24)
    ax.set_xlabel('',fontsize=16) # x轴名称
    fig.autofmt_xdate()
    ax.set_ylabel('Temp(F)',fontsize=16) # y轴名称
    ax.tick_params(axis='both',which='major',labelsize=16)

    plt.show()


