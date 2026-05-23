import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

def fix_contents(m):
    style = m.group(1)
    # Remove positioning for elements with display: contents
    new_style = re.sub(r'position:\s*absolute;?', '', style)
    new_style = re.sub(r'left:\s*[^;]+;?', '', new_style)
    new_style = re.sub(r'top:\s*[^;]+;?', '', new_style)
    new_style = re.sub(r'right:\s*[^;]+;?', '', new_style)
    new_style = re.sub(r'bottom:\s*[^;]+;?', '', new_style)
    new_style = re.sub(r'width:\s*[^;]+;?', '', new_style)
    new_style = re.sub(r'height:\s*[^;]+;?', '', new_style)
    # clean up multiple spaces
    new_style = re.sub(r'\s+', ' ', new_style).strip()
    return m.group(0).replace(style, new_style)

new_html = re.sub(r'<div[^>]*?style="([^"]*?display:\s*contents[^"]*?)"', fix_contents, html)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Fixed display: contents issues.")
