import plotly.express as px

# Plotly Express将渐变存储在模块colors 中。这些渐变是在列表
# px.colors.named_colorscales() 中定义的。下面的输出列出了可供你使用
# 的所有渐变：
for key in px.colors.named_colorscales():
    print(key)
