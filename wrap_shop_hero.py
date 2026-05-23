import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'(<div class="contents" style="display: contents;" data-node-id="124:487">)(.*?)(?=        </div>\n        <div class="top-0 w-0")'

def repl(m):
    return m.group(1) + '\n          <div class="hero-content-wrapper" style="position: relative; z-index: 10; display: block;">' + m.group(2) + '          </div>\n'

html_new = re.sub(pattern, repl, html, flags=re.DOTALL)

if html_new != html:
    with open('shop.html', 'w', encoding='utf-8') as f:
        f.write(html_new)
    print("Wrapper added successfully.")
else:
    print("Regex match failed.")
