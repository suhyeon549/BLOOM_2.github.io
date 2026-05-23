import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

def exact_class(node_id, cls):
    global html
    if f'data-node-id="{node_id}"' in html and not re.search(rf'class="[^"]*"[^>]*data-node-id="{node_id}"', html):
        html = re.sub(rf'(data-node-id="{node_id}")', rf'class="{cls}" \1', html)
    else:
        html = re.sub(rf'class="[^"]*"([^>]*?data-node-id="{node_id}")', rf'class="{cls}"\1', html)

exact_class('134:289', 'reveal reveal-scale delay-100')
exact_class('134:283', 'reveal reveal-scale delay-100')

exact_class('134:287', 'reveal reveal-scale delay-200')
exact_class('134:284', 'reveal reveal-scale delay-200')

exact_class('134:288', 'reveal reveal-scale delay-300')
exact_class('134:285', 'reveal reveal-scale delay-300')

exact_class('134:290', 'reveal reveal-scale delay-400')
exact_class('134:286', 'reveal reveal-scale delay-400')

html = html.replace('class="-scale ', 'class="')

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Cloudy Rest fixed.")
