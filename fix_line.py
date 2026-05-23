with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('line-"', 'line-height: 0;"')
html = html.replace('line- ', 'line-height: 0; ')

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
