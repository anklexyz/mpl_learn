# import requests
#
# # 存储API调用的URL
# url = 'https://api.github.com/search/repositories?' \
#       'q=language:python&sort=stars'
# # 最新的GitHub API版本为第3版，因此通过
# # 指定headers“显式地”要求使用这个版本的API，再使
# # 用requests 调用API。
# headers = {'Accept': 'application/vnd.github.v3+json'}
# # 我们调用get()并将URL传递给它，再将 响应对象 赋给变量r 。
# r = requests.get(url, headers=headers)
# # 响应对象包含一个
# # 名为status_code的属性，指出了请求是否成功（状态码200表示请求成功）。
# print(f"Status code: {r.status_code}")
# # 这个API返回JSON格式的信息，因此使用方法json()
# # 将这些信息转换为一个Python字典
# response_dict = r.json()
# # 打印response_dict 中的键
# print(response_dict.keys())
# # 注意 　像这样简单的调用应该会返回完整的结果集，因此完全可以忽略
# # 与'incomplete_results' 关联的值。但在执行更复杂的API调用时，应检
# # 查这个值。

# import requests
#
# # 执行API调用并存储响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print("Status code:", r.status_code)
#
# # 将API响应存储在一个变量中
# response_dict = r.json()
# print("Total repositories:", response_dict['total_count'])
#
# # 探索有关仓库的信息
# repo_dicts = response_dict['items']  # 返回一个items的列表，与'items'相关联的值
# # 是一个列表，其中包含很多字典，而每个字典都包含有关一个Python仓库的信息。
# print("Repositories returned:", len(repo_dicts))
#
# # 研究第一个仓库
# repo_dict = repo_dicts[0]  # 每个元素是一个字典类型，里面包含每个仓库的信息
# # print("\nKeys:", len(repo_dict)) # 这个字典中Key的个数
# # for key in sorted(repo_dict.keys()):
# #     print(key)  # 排序后打印这些键
# print("\nSelected information about first repository:")
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
# print(f"Description: {repo_dict['description']}")


import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
rq_obj=requests.get(url)
print(f"Status code: {rq_obj.status_code}")
response_dict = rq_obj.json() # 响应对象用.json方法把json格式解析为列表返回

repo_dicts=response_dict['items']

print("Selected information about first repository:")

for repo in repo_dicts:
    print(f"\nName: {repo['name']}")
    print(f"Owner: {repo['owner']['login']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Repository: {repo['html_url']}")
    print(f"Description: {repo['description']}")

