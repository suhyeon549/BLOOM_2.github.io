import re
with open('shop.html', 'r', encoding='utf-8') as f:
    text = f.read()
print(re.findall(r'data-node-id="([^"]+)"', text[-10000:]))
