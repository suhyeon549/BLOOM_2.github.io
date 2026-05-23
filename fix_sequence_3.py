import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.delay-800' not in css:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write("\n.delay-800 { transition-delay: 800ms; }\n")

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

def set_class(node_id, new_cls):
    global html
    def repl(m):
        cls_str = m.group(1)
        for ac in ["reveal", "reveal-up", "reveal-scale", "delay-100", "delay-200", "delay-300", "delay-400", "delay-500", "delay-600", "delay-800", "hover-lift", "hover-scale", "img-zoom-wrap"]:
            cls_str = re.sub(rf'\b{ac}\b', '', cls_str)
        cls_str = re.sub(r'\s+', ' ', cls_str).strip()
        final_cls = f"{cls_str} {new_cls}".strip()
        return f'class="{final_cls}"{m.group(2)}'
    
    html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{node_id}")', repl, html)

set_class('124:491', 'reveal reveal-up hover-lift delay-400')
set_class('124:488', 'reveal reveal-up hover-lift delay-400')

# HOW IT WORKS
set_class('125:669', 'reveal reveal-up')
set_class('125:671', 'reveal reveal-up delay-200')

# From mood to soap ...
set_class('125:668', 'reveal reveal-up')
set_class('125:637', 'reveal reveal-up delay-200')

card1_nodes = ['125:638', '125:640', '125:641', '125:642', '125:643', '125:644', '125:645', '125:646', '125:647']
for n in card1_nodes:
    if n == '125:638':
        set_class(n, 'reveal reveal-scale hover-lift delay-400')
    else:
        set_class(n, 'reveal reveal-scale delay-400')

card2_nodes = ['125:648', '125:650', '125:651', '125:652', '125:653', '125:654', '125:655', '125:656', '125:657', '125:649']
for n in card2_nodes:
    if n == '125:648':
        set_class(n, 'reveal reveal-scale hover-lift delay-600')
    else:
        set_class(n, 'reveal reveal-scale delay-600')

card3_nodes = ['125:658', '125:660', '125:661', '125:662', '125:663', '125:664', '125:665', '125:666', '125:667', '125:659']
for n in card3_nodes:
    if n == '125:658':
        set_class(n, 'reveal reveal-scale hover-lift delay-800')
    else:
        set_class(n, 'reveal reveal-scale delay-800')

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Card sequence updated successfully.")
