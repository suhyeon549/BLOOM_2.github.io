import re
import os
import urllib.request

with open(r'C:\Users\yeons\.gemini\antigravity\brain\a0de5db8-fcea-4037-b511-d410ef8bf03d\.system_generated\steps\1499\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'(<div className="relative size-full".*?)(\n    </div>\n  \);\n})', text, re.DOTALL)
if not match:
    print("Could not find Frame 6 in 1499 output.txt")
    exit(1)

new_frame6 = match.group(1) + "\n    </div>"
# Add the top-level container positioning: right below Frame 5
# Frame 5 is height 63.515625vw (813px), top 185.15625vw (2370px).
# So Frame 6 should be at top 185.15625 + 63.515625 = 248.671875vw (3183px).
# Let's check Frame 6 height from the first child: 
# Wait, the first child is <div className="absolute ... h-[166px] left-0 top-0 w-[1280px]" ...> but there are elements at top-[923px] and h-[35px]. So height is 958px (74.84375vw).
new_frame6 = new_frame6.replace('<div className="relative size-full" data-node-id="134:263" data-name="6">', 
    '<div class="" style="position: absolute; height: 74.84375vw; left: 0; overflow: clip; top: 248.671875vw; width: 100.0vw;" data-node-id="134:263" data-name="6">')

img_defs = {}
for m in re.finditer(r'const (img[a-zA-Z0-9_]+) = "http://localhost:3845/(assets/[^"]+)";', text):
    img_defs[m.group(1)] = m.group(2)

# Download images if they don't exist
os.makedirs('assets', exist_ok=True)
for var_name, path in img_defs.items():
    local_path = path
    if not os.path.exists(local_path):
        print(f"Downloading {local_path}...")
        try:
            urllib.request.urlretrieve(f"http://localhost:3845/{path}", local_path)
        except Exception as e:
            print(f"Error downloading {path}: {e}")
    new_frame6 = new_frame6.replace(f'src={{{var_name}}}', f'src="{path}"')

def translate_classes(m):
    tag = m.group(0)
    classes = re.search(r'className="([^"]+)"', tag)
    if not classes: return tag
    classes = classes.group(1).split()
    styles = []
    for c in classes:
        if c == 'absolute': styles.append('position: absolute;')
        elif c == 'relative': styles.append('position: relative;')
        elif c == 'bg-white': styles.append('background-color: white;')
        elif c.startswith('bg-[#'): styles.append(f"background-color: {c[4:11]};")
        elif c.startswith('border-[#'): styles.append(f"border-color: {c[8:15]};")
        elif c.startswith('w-['):
            val = c[3:-1]
            if val.endswith('%'): styles.append(f"width: {val};")
            else: styles.append(f"width: {float(val[:-2])/12.8}vw;")
        elif c.startswith('h-['):
            val = c[3:-1]
            if val.endswith('%'): styles.append(f"height: {val};")
            else: styles.append(f"height: {float(val[:-2])/12.8}vw;")
        elif c.startswith('top-['):
            val = c[5:-1]
            if val.endswith('%'): styles.append(f"top: {val};")
            else: styles.append(f"top: {float(val[:-2])/12.8}vw;")
        elif c == 'top-0': styles.append("top: 0;")
        elif c == 'left-0': styles.append("left: 0;")
        elif c.startswith('left-['):
            inner = c[6:-1]
            if inner.startswith('calc(50%-'): styles.append(f"left: {(640 - float(inner[9:-3]))/12.8}vw;")
            elif inner.startswith('calc(50%+'): styles.append(f"left: {(640 + float(inner[9:-3]))/12.8}vw;")
            else: styles.append(f"left: {float(inner[:-2])/12.8}vw;")
        elif c.startswith('size-['):
            val = c[6:-1]
            if val.endswith('px'): styles.append(f'width: {float(val[:-2])/12.8}vw; height: {float(val[:-2])/12.8}vw;')
        elif c == 'size-full': styles.append('width: 100%; height: 100%;')
        elif c == 'w-full': styles.append('width: 100%;')
        elif c == '-translate-x-1/2': styles.append('transform: translateX(-50%);')
        elif c == '-translate-y-1/2': styles.append('transform: translateY(-50%);')
        elif c == 'border-solid': styles.append('border-style: solid;')
        elif c == 'border-b': styles.append('border-bottom-width: 1px;')
        elif c == 'border-t': styles.append('border-top-width: 1px;')
        elif c == 'border-l': styles.append('border-left-width: 1px;')
        elif c == 'border-r': styles.append('border-right-width: 1px;')
        elif c == 'border-black': styles.append('border-color: black;')
        elif c == 'border-white': styles.append('border-color: white;')
        elif c == 'object-cover': styles.append('object-fit: cover;')
        elif c == 'max-w-none': styles.append('max-width: none;')
        elif c == 'pointer-events-none': styles.append('pointer-events: none;')
        elif c == 'inset-0': styles.append('top: 0; right: 0; bottom: 0; left: 0;')
        elif c == 'flex': styles.append('display: flex;')
        elif c == 'flex-col': styles.append('flex-direction: column;')
        elif c == 'justify-center': styles.append('justify-content: center;')
        elif c.startswith('text-[#'): styles.append(f"color: {c[6:13]};")
        elif c.startswith('text-['): styles.append(f"font-size: {float(c[6:-3])/12.8}vw;")
        elif c == 'text-black': styles.append('color: black;')
        elif c == 'whitespace-nowrap': styles.append('white-space: nowrap;')
        elif c == 'font-medium': styles.append('font-weight: 500;')
        elif c == 'font-normal': styles.append('font-weight: 400;')
        elif c == 'font-bold': styles.append('font-weight: 700;')
        elif c.startswith('rounded-['): styles.append(f"border-radius: {float(c[9:-3])/12.8}vw;")
        elif c.startswith('tracking-['): styles.append(f"letter-spacing: {float(c[10:-3])/12.8}vw;")
        elif c.startswith('leading-['):
            val = c[9:-1]
            if val.endswith('px'): styles.append(f"line-height: {float(val[:-2])/12.8}vw;")
            else: styles.append(f"line-height: {val};")
        elif c == 'mb-0': styles.append("margin-bottom: 0;")
        elif c == 'contents': styles.append("display: contents;")
        elif c == '[word-break:break-word]': styles.append("word-break: break-word;")
        elif c == 'not-italic': styles.append("font-style: normal;")
    
    style_str = ' '.join(styles)
    tag = re.sub(r'className="[^"]+"', f'class="" style="{style_str}"', tag)
    return tag

new_frame6 = re.sub(r'<div[^>]*>', translate_classes, new_frame6)
new_frame6 = re.sub(r'<p[^>]*>', translate_classes, new_frame6)
new_frame6 = re.sub(r'<img[^>]*>', translate_classes, new_frame6)

new_frame6 = re.sub(r'<img([^>]*?style=")', r'<img\1object-fit: cover; ', new_frame6)
new_frame6 = re.sub(r'<div(.*?)\s*/>', r'<div\1></div>', new_frame6)
new_frame6 = re.sub(r'<p(.*?)\s*/>', r'<p\1></p>', new_frame6)

with open('shop.html', 'r', encoding='utf-8') as f:
    shop_html = f.read()

# Find the end of Frame 5 (data-node-id="125:673")
# First, let's find data-node-id="125:673" and then count divs to find its end.
start_idx = shop_html.find('data-node-id="125:673"')
if start_idx == -1:
    print("Could not find Frame 5")
    exit(1)

start_div_idx = shop_html.rfind('<div', 0, start_idx)
div_count = 0
end_idx = start_div_idx
while end_idx < len(shop_html):
    tag_start = shop_html.find('<', end_idx)
    if tag_start == -1: break
    if shop_html[tag_start:tag_start+4] == '<div':
        div_count += 1
        end_idx = tag_start + 4
    elif shop_html[tag_start:tag_start+5] == '</div':
        div_count -= 1
        end_idx = tag_start + 5
        if div_count == 0:
            end_idx = shop_html.find('>', end_idx) + 1
            break
    else:
        end_idx = tag_start + 1

# Insert new_frame6 right after Frame 5
shop_html = shop_html[:end_idx] + '\n' + new_frame6 + shop_html[end_idx:]

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(shop_html)

print("Successfully inserted Frame 6")
