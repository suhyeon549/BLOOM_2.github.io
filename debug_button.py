with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()
idx = html.find('data-node-id="124:488"')
print(html[max(0, idx-500):min(len(html), idx+1000)])
