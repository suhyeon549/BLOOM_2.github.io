with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.rfind('data-name="Footer"')
start = html.rfind('<div', 0, idx)
print("Start idx:", start)

count = 0
i = start
footer_end = -1
while i < len(html):
    if html.startswith('<div', i):
        count += 1
        i += 4
    elif html.startswith('</div', i):
        count -= 1
        if count == 0:
            footer_end = html.find('>', i) + 1
            break
        i += 5
    else:
        i += 1

print("End idx:", footer_end)
print("Content snippet:", html[start:start+100])
