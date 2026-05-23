import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.delay-500' not in css:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write("\n.delay-500 { transition-delay: 500ms; }\n.delay-600 { transition-delay: 600ms; }\n")

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

def set_class(node_id, new_cls):
    global html
    def repl(m):
        cls_str = m.group(1)
        for ac in ["reveal", "reveal-up", "reveal-scale", "delay-100", "delay-200", "delay-300", "delay-400", "delay-500", "delay-600", "hover-lift", "hover-scale", "img-zoom-wrap"]:
            cls_str = re.sub(rf'\b{ac}\b', '', cls_str)
        cls_str = re.sub(r'\s+', ' ', cls_str).strip()
        final_cls = f"{cls_str} {new_cls}".strip()
        return f'class="{final_cls}"{m.group(2)}'
    
    html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{node_id}")', repl, html)

# 1. Top Hero Section
set_class('124:494', 'reveal reveal-up')
set_class('125:629', 'reveal reveal-scale img-zoom-wrap')
set_class('124:495', 'reveal reveal-up delay-200')
set_class('124:496', 'reveal reveal-up delay-200')
set_class('124:488', 'reveal reveal-up hover-lift delay-400')
set_class('124:491', 'reveal reveal-up hover-lift delay-600')

# 2. Problem Header
set_class('124:563', 'reveal reveal-up')
set_class('124:567', 'reveal reveal-up delay-200')

# 3. Problem Section Content
set_class('124:525', 'reveal reveal-up')
set_class('125:624', 'reveal reveal-scale img-zoom-wrap')
set_class('124:523', 'reveal reveal-up delay-200')
set_class('124:524', 'reveal reveal-up delay-400')

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated sequences successfully.")
