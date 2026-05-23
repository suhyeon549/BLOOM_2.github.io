import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

def repl_class(m, new_cls):
    cls_str = m.group(1)
    for ac in ["delay-100", "delay-200", "delay-300", "delay-400", "delay-500", "delay-600", "delay-800"]:
        cls_str = re.sub(rf'\b{ac}\b', '', cls_str)
    cls_str = re.sub(r'\s+', ' ', cls_str).strip()
    return f'class="{cls_str} {new_cls}"{m.group(2)}'

html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="124:488")', lambda m: repl_class(m, 'delay-200'), html)
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="124:491")', lambda m: repl_class(m, 'delay-200'), html)

card1_nodes = ['125:638', '125:640', '125:641', '125:642', '125:643', '125:644', '125:645', '125:646', '125:647']
for n in card1_nodes:
    html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{n}")', lambda m: repl_class(m, 'delay-400'), html)

card2_nodes = ['125:648', '125:650', '125:651', '125:652', '125:653', '125:654', '125:655', '125:656', '125:657', '125:649']
for n in card2_nodes:
    html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{n}")', lambda m: repl_class(m, 'delay-500'), html)

card3_nodes = ['125:658', '125:660', '125:661', '125:662', '125:663', '125:664', '125:665', '125:666', '125:667', '125:659']
for n in card3_nodes:
    html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{n}")', lambda m: repl_class(m, 'delay-600'), html)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Adjusted timings successfully.")
