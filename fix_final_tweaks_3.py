import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

def remove_from_left_top(m):
    s = m.group(0)
    for ac in ["reveal", "reveal-up", "reveal-scale", "active", "delay-100", "delay-200", "delay-300", "delay-400", "delay-500", "delay-600", "delay-800"]:
        s = re.sub(rf'\b{ac}\b', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# 1. Remove animation from left-0 top-0 
html = re.sub(r'<div[^>]*class="[^"]*\bleft-0\b[^"]*\btop-0\b[^"]*"[^>]*>', remove_from_left_top, html)
html = re.sub(r'<div[^>]*class="[^"]*\btop-0\b[^"]*\bleft-0\b[^"]*"[^>]*>', remove_from_left_top, html)

def repl_class_delay(m, new_delay):
    cls_str = m.group(1)
    for ac in ["delay-100", "delay-200", "delay-300", "delay-400", "delay-500", "delay-600", "delay-800"]:
        cls_str = re.sub(rf'\b{ac}\b', '', cls_str)
    cls_str = re.sub(r'\s+', ' ', cls_str).strip()
    if new_delay:
        return f'class="{cls_str} {new_delay}"{m.group(2)}'
    return f'class="{cls_str}"{m.group(2)}'

# 2. Card timings: 100, 200, 300 to overlap perfectly and be very snappy.
card1_nodes = ['125:638', '125:640', '125:641', '125:642', '125:643', '125:644', '125:645', '125:646', '125:647']
for n in card1_nodes:
    html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{n}")', lambda m: repl_class_delay(m, 'delay-100'), html)

card2_nodes = ['125:648', '125:650', '125:651', '125:652', '125:653', '125:654', '125:655', '125:656', '125:657', '125:649']
for n in card2_nodes:
    html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{n}")', lambda m: repl_class_delay(m, 'delay-200'), html)

card3_nodes = ['125:658', '125:660', '125:661', '125:662', '125:663', '125:664', '125:665', '125:666', '125:667', '125:659']
for n in card3_nodes:
    html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{n}")', lambda m: repl_class_delay(m, 'delay-300'), html)

# 3. KEY FEATURES -> Made for Every Mood
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="134:235")', lambda m: repl_class_delay(m, ''), html) # KEY FEATURES
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="134:246")', lambda m: repl_class_delay(m, 'delay-300'), html) # Made for Every Mood

# 4. Text grids first, then Image grids
def ensure_reveal(m, extra):
    cls_str = m.group(1)
    if 'reveal' not in cls_str:
        cls_str += ' reveal'
    # strip existing reveal-up/scale to reset
    for ac in ["reveal-up", "reveal-scale", "delay-100", "delay-200", "delay-300", "delay-400", "delay-500", "delay-600", "delay-800"]:
        cls_str = re.sub(rf'\b{ac}\b', '', cls_str)
    cls_str = re.sub(r'\s+', ' ', cls_str).strip()
    return f'class="{cls_str} {extra}"{m.group(2)}'

text_grids = ['134:336', '134:337', '134:338']
for n in text_grids:
    if f'data-node-id="{n}"' in html and not re.search(rf'class="[^"]*"[^>]*data-node-id="{n}"', html):
        html = re.sub(rf'(data-node-id="{n}")', r'class="reveal reveal-scale" \1', html)
    else:
        html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{n}")', lambda m: ensure_reveal(m, 'reveal-scale'), html)

img_grids = ['134:340', '134:335', '134:341', '134:334']
for n in img_grids:
    if f'data-node-id="{n}"' in html and not re.search(rf'class="[^"]*"[^>]*data-node-id="{n}"', html):
        html = re.sub(rf'(data-node-id="{n}")', r'class="reveal reveal-scale delay-400" \1', html)
    else:
        html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{n}")', lambda m: ensure_reveal(m, 'reveal-scale delay-400'), html)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Adjusted successfully.")
