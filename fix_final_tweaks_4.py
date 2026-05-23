import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix duplicate class attributes created by accident
while re.search(r'(<[^>]*)class="([^"]*)"([^>]*)class="([^"]*)"', html):
    html = re.sub(r'(<[^>]*)class="([^"]*)"([^>]*)class="([^"]*)"', r'\1class="\2 \4"\3', html)

def repl_class(m, new_cls):
    cls_str = m.group(1)
    for ac in ["reveal", "reveal-up", "reveal-scale", "reveal-slow-zoom", "delay-100", "delay-200", "delay-300", "delay-400", "delay-500", "delay-600", "delay-800", "hover-lift", "hover-scale", "img-zoom-wrap"]:
        cls_str = re.sub(rf'\b{ac}\b', '', cls_str)
    cls_str = re.sub(r'\s+', ' ', cls_str).strip()
    if new_cls:
        return f'class="{cls_str} {new_cls}"{m.group(2)}'
    else:
        if cls_str:
            return f'class="{cls_str}"{m.group(2)}'
        else:
            return f'{m.group(2)}'

def ensure_class(node_id, cls):
    global html
    if f'data-node-id="{node_id}"' in html and not re.search(rf'class="[^"]*"[^>]*data-node-id="{node_id}"', html):
        html = re.sub(rf'(data-node-id="{node_id}")', rf'class="{cls}" \1', html)
    else:
        html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{node_id}")', lambda m: repl_class(m, cls), html)

for n in ['134:336', '134:337', '134:338']:
    html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{n}")', lambda m: repl_class(m, ''), html)

for n in ['134:342', '134:343', '134:344', '134:345']:
    ensure_class(n, 'reveal reveal-up delay-100')

for n in ['134:346', '134:347', '134:348', '134:349']:
    ensure_class(n, 'reveal reveal-up delay-200')

for n in ['134:334', '134:335', '134:340', '134:341']:
    ensure_class(n, 'reveal reveal-scale delay-400')

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated grid animation sequence successfully.")
