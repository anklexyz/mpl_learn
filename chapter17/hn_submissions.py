from operator import itemgetter

import requests
# 下面的URL返回一个列表，其中包含Hacker News上当前排名靠前的文章的ID：
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # 对于每篇文章，都执行一个API调用。
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    # 对于每篇文章，都创建一个字典。
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

# 我们要根据评论数对字典列表
# submission_dicts 进行排序，为此使用了模块operator 中的函数
# itemgetter() （见❼）。我们向这个函数传递了键'comments' ，因此它从该
# 列表的每个字典中提取与键'comments' 关联的值。这样，函数sorted() 将根据
# 这个值对列表进行排序。我们将列表按降序排列，即评论最多的文章位于最前面。
# 第二个参数是提取列表中所有键key的值，根据这个排序
# submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
#                           reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

