import os
os.system("git restore shop.html")
os.system("python my_update_frame6.py")
os.system("python fix_contents.py")
os.system("python fix_line.py")

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
index_footer = "".join(lines[193:213])
index_footer = index_footer.replace('class="abs footer-wrap"', 'class="abs footer-wrap" style="top: 426.015625vw;"')

with open('shop.html', 'r', encoding='utf-8') as f:
    shop_html = f.read()

start_idx = shop_html.find('data-name="Footer"')
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

# Fix Frame 7 left
old_str = 'left: 0.234375vw; overflow: clip; top: 369.84375vw; width: 99.765625vw;'
new_str = 'left: 0; overflow: clip; top: 369.84375vw; width: 100vw;'
shop_html = shop_html.replace(old_str, new_str)

# Fix Frame 6 left
old_frame6_str = 'left: 0.15625vw; overflow: clip; top: 248.75vw; width: 99.84375vw;'
new_frame6_str = 'left: 0; overflow: clip; top: 248.75vw; width: 100vw;'
shop_html = shop_html.replace(old_frame6_str, new_frame6_str)

# Fix .figma-container height
shop_html = shop_html.replace('height: 5651px;', 'height: 441.484vw;')

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(shop_html)

final_html = open('shop.html', 'r', encoding='utf-8').read()
print("Divs:", final_html.count('<div'), final_html.count('</div'))
