with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

if '""' in html:
    print('Bug found!')
    idx = html.find('""')
    print(html[max(0, idx-50):min(len(html), idx+50)])
else:
    print('No double quotes bug found.')
