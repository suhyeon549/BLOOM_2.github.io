import re
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Original regex from fix_shop.py:
regex = r'<!-- Top horizontal line -->.*?<!-- Small Logo / Title -->\s*<div class="abs logo-small-wrapper" onclick="window\.location\.href=\'index\.html\'" style="cursor: pointer;">\s*<div class="logo-small-text">OOB</div>\s*<div class="logo-small-text">L</div>\s*<div class="logo-small-text">M</div>\s*</div>'

header_match = re.search(regex, index_html, re.DOTALL)
print('Header match:', bool(header_match))

if not header_match:
    print("Let's look for Top horizontal line")
    idx = index_html.find('<!-- Top horizontal line -->')
    print("Index of top horizontal line:", idx)
    if idx != -1:
        print(index_html[idx:idx+500])
