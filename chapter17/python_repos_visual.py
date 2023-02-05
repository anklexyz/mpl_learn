# import requests
# from plotly.graph_objs import Bar
# from plotly import offline
#
# url = 'https://api.github.com/search/repositories?' \
#       'q=language:python&sort=stars'
# headers = {'Accept': 'application/vnd.github.com.v3+json'}
# r = requests.get(url, headers=headers)
# # print(f"Status code:{r.status_code}")
#
# response_dict = r.json()
# repo_dicts = response_dict['items']
# repo_names, stars = [], []
# for repo_dict in repo_dicts:
#     repo_names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# # 数据填充
# data = [{
#     'type': 'bar',
#     'x': repo_names,
#     'y': stars,
#     'marker': {
#         'color': 'rgb(60,100,150)',
#         'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
#     },
#     'opacity': 0.6,
# }]
# # 定义列表data （见❹）。它像第16章的列表data 一样包含一个字典，指定
# # 了图表的类型，并提供了 值和 值： 值为项目名称， 值为项目获得了多少个
# # 星。
#
# # 布局（标题，x轴名称，y轴名称）
# my_layout = {
#     'title': 'GitHub上最受欢迎的Python项目',
#     'titlefont': {'size': 28},
#     'xaxis': {
#         'title': '仓库Repository',
#         'titlefont': {'size': 24},
#         'tickfont': {'size': 14},
#     },
#     'yaxis': {
#         'title': '星数Stars',
#         'titlefont': {'size': 24},
#         'tickfont': {'size': 14},
#     },
# }
# # 使用字典定义图表的布局。这里没有创建Layout 实例，而是创建了一个
# # 包含布局规范的字典，并在其中指定了图表的名称以及每个坐标轴的标签。
#
# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='python_repos.html')

import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)


# Make visualization.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

