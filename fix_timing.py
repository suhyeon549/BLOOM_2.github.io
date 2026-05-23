with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace("transition: scale 2s cubic-bezier(0.25, 1, 0.5, 1) 0.8s;", "transition: scale 2s cubic-bezier(0.25, 1, 0.5, 1) 0.2s;")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

import re
with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(class=".*?)\bdelay-500\b(.*?"[^>]*?data-node-id="124:491")', r'\1delay-400\2', html)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Timing fixed successfully.")
