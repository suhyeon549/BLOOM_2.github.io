import re

# 1. Read index.html and extract footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

footer_match = re.search(r'<!-- Footer -->(.*?)</div>\s*</div>', index_html, re.DOTALL)
if footer_match:
    index_footer = '<!-- Footer -->' + footer_match.group(1) + '</div>\n    </div>'
else:
    print("Could not find Footer in index.html")
    exit(1)

# Add top property to override index.html's CSS
index_footer = index_footer.replace('class="abs footer-wrap"', 'class="abs footer-wrap" style="top: 426.015625vw;"')

# 2. Read shop.html and replace its footer
with open('shop.html', 'r', encoding='utf-8') as f:
    shop_html = f.read()

# Replace shop.html's footer. It starts with data-name="Footer"
start_idx = shop_html.find('data-name="Footer"')
if start_idx != -1:
    footer_start = shop_html.rfind('<div', 0, start_idx)
    count = 0
    i = footer_start
    footer_end = -1
    while i < len(shop_html):
        if shop_html.startswith('<div', i):
            count += 1
            i += 4
        elif shop_html.startswith('</div', i):
            count -= 1
            if count == 0:
                footer_end = shop_html.find('>', i) + 1
                break
            i += 5
        else:
            i += 1
            
    shop_html = shop_html[:footer_start] + index_footer + shop_html[footer_end:]
    print("Replaced footer in shop.html")
else:
    print("Could not find Footer in shop.html")

# 3. Fix the image in class="left-0 top-0" (Frame 7 wrapper)
old_str = 'left: 0.234375vw; overflow: clip; top: 369.84375vw; width: 99.765625vw;'
new_str = 'left: 0; overflow: clip; top: 369.84375vw; width: 100vw;'
if old_str in shop_html:
    shop_html = shop_html.replace(old_str, new_str)
    print("Fixed Frame 7 left and width")

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(shop_html)
print("Saved shop.html")
