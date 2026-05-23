import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

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

# 1. Autumn Harvest sequence
ensure_class('134:296', 'reveal reveal-scale delay-100')
ensure_class('134:332', 'reveal reveal-scale delay-100')
ensure_class('134:294', 'reveal reveal-scale delay-200')
ensure_class('134:330', 'reveal reveal-scale delay-200')
ensure_class('134:295', 'reveal reveal-scale delay-300')
ensure_class('134:331', 'reveal reveal-scale delay-300')
ensure_class('134:297', 'reveal reveal-scale delay-400')
ensure_class('134:333', 'reveal reveal-scale delay-400')

# 2. Cloudy Rest sequence
ensure_class('134:289', 'reveal reveal-scale delay-100')
ensure_class('134:271', 'reveal reveal-scale delay-100')
ensure_class('134:283', 'reveal reveal-scale delay-200')
ensure_class('134:269', 'reveal reveal-scale delay-200')
ensure_class('134:288', 'reveal reveal-scale delay-300')
ensure_class('134:270', 'reveal reveal-scale delay-300')
ensure_class('134:290', 'reveal reveal-scale delay-400')
ensure_class('134:272', 'reveal reveal-scale delay-400')

# 3. bottom image zoom
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="125:680")', lambda m: repl_class(m, 'reveal reveal-slow-zoom delay-0'), html)

# 4. left-0 class="block" (124:575)
ensure_class('124:575', 'reveal reveal-scale delay-0')

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated tags and bottom sections successfully.")
