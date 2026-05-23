import re

with open(r'C:\Users\yeons\.gemini\antigravity\brain\a0de5db8-fcea-4037-b511-d410ef8bf03d\.system_generated\steps\1202\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract Frame 5 from the new output
match = re.search(r'(<div className="relative size-full" data-node-id="125:673".*?)(\n    </div>\n  \);\n})', text, re.DOTALL)
if not match:
    print("Could not find Frame 5 in output.txt")
    exit(1)

new_frame5 = match.group(1) + "\n    </div>"
# Fix the top-level class to match the old Frame 5 wrapper (absolute, top, left, width, height)
# In shop.html, the old wrapper was: <div class="left-0" style="position: absolute; height: 63.515625vw; overflow: clip; top: 185.15625vw; width: 100.0vw;" data-node-id="125:673" data-name="5">
new_frame5 = new_frame5.replace('<div className="relative size-full" data-node-id="125:673" data-name="5">', 
    '<div className="absolute h-[813px] left-0 overflow-clip top-[2370px] w-[1280px]" data-node-id="125:673" data-name="5">')

# Extract img defs
img_defs = {}
for line in text.split('\n'):
    if line.startswith('const img') and '=' in line:
        var_name = line.split(' ')[1]
        url = line.split('"')[1]
        filename = url.split('/')[-1]
        img_defs[var_name] = f"assets/{filename}"

def replace_tailwind(m):
    classes = m.group(1).split(' ')
    styles = []
    new_classes = []
    for c in classes:
        if c.startswith('text-[#'): styles.append(f"color: {c[6:13]};")
        elif c.startswith('text-['): styles.append(f"font-size: {float(c[6:-3])/12.8}vw;")
        elif c.startswith('leading-['):
            val = c[9:-1]
            if val.endswith('px'): styles.append(f"line-height: {float(val[:-2])/12.8}vw;")
            else: styles.append(f"line-height: {val};")
        elif c.startswith('tracking-['):
            val = c[10:-1]
            if val.endswith('px'): styles.append(f"letter-spacing: {float(val[:-2])/12.8}vw;")
            elif val.endswith('em'): styles.append(f"letter-spacing: {val};")
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
            val = c[6:-1]
            if val.startswith('calc'):
                val = val.replace('calc(', '').replace(')', '')
                parts = val.split('-') if '-' in val[1:] else val.split('+')
                op = '-' if '-' in val[1:] else '+'
                if len(parts) == 2:
                    p1 = parts[0].strip()
                    p2 = parts[1].strip()
                    if p1 == '50%': p1 = '50vw'
                    p2 = f"{float(p2[:-2])/12.8}vw"
                    styles.append(f"left: calc({p1} {op} {p2});")
            else:
                styles.append(f"left: {float(val[:-2])/12.8}vw;")
        elif c.startswith('rounded-['): styles.append(f"border-radius: {float(c[9:-3])/12.8}vw;")
        elif c.startswith('font-['):
            val = c[6:-1]
            if 'Montserrat' in val: styles.append("font-family: 'Montserrat', sans-serif;")
            elif 'Pretendard' in val: styles.append("font-family: 'Pretendard', sans-serif;")
            elif 'Helvetica' in val: styles.append("font-family: 'Helvetica Neue', sans-serif;")
        elif c == 'absolute': styles.append('position: absolute;')
        elif c == 'relative': styles.append('position: relative;')
        elif c == 'flex': styles.append('display: flex;')
        elif c == 'flex-col': styles.append('flex-direction: column;')
        elif c == 'items-center': styles.append('align-items: center;')
        elif c == 'justify-center': styles.append('justify-content: center;')
        elif c == 'uppercase': styles.append('text-transform: uppercase;')
        elif c == 'font-medium': styles.append('font-weight: 500;')
        elif c == 'font-normal': styles.append('font-weight: 400;')
        elif c == 'whitespace-nowrap': styles.append('white-space: nowrap;')
        elif c == 'object-cover': styles.append('object-fit: cover;')
        elif c == 'size-full': styles.append('width: 100%; height: 100%;')
        elif c == 'w-full': styles.append('width: 100%;')
        elif c == 'max-w-none': styles.append('max-width: none;')
        elif c == 'pointer-events-none': styles.append('pointer-events: none;')
        elif c == 'inset-0': styles.append('top: 0; right: 0; bottom: 0; left: 0;')
        elif c == 'text-black': styles.append('color: black;')
        elif c == 'bg-white': styles.append('background-color: white;')
        elif c == 'overflow-hidden': styles.append('overflow: hidden;')
        elif c == 'overflow-clip': styles.append('overflow: clip;')
        elif c == '-translate-x-1/2': styles.append('transform: translateX(-50%);')
        elif c == '-translate-y-1/2': styles.append('transform: translateY(-50%);')
        elif c == 'rotate-90': styles.append('transform: rotate(90deg);')
        elif c == 'border-solid': styles.append('border-style: solid;')
        elif c == 'border-b': styles.append('border-bottom-width: 1px;')
        elif c == 'border-t': styles.append('border-top-width: 1px;')
        elif c == 'border-l': styles.append('border-left-width: 1px;')
        elif c == 'border-r': styles.append('border-right-width: 1px;')
        elif c == 'border-black': styles.append('border-color: black;')
        elif c == 'border-white': styles.append('border-color: white;')
        elif c.startswith('size-['):
            val = c[6:-1]
            if val.endswith('px'): styles.append(f'width: {float(val[:-2])/12.8}vw; height: {float(val[:-2])/12.8}vw;')
        elif c.startswith('inset-['):
            val = c[7:-1]
            val = re.sub(r'(-?\d+(?:\.\d+)?)px', lambda x: f'{float(x.group(1))/12.8}vw', val).replace('_', ' ')
            styles.append(f'inset: {val};')
        else:
            new_classes.append(c)
            
    style_str = ' '.join(styles)
    if style_str:
        return f'class="{" ".join(new_classes)}" style="{style_str}"'
    else:
        return f'class="{" ".join(new_classes)}"'

new_frame5 = re.sub(r'className="([^"]+)"', replace_tailwind, new_frame5)

for var_name, path in img_defs.items():
    new_frame5 = new_frame5.replace(f'src={{{var_name}}}', f'src="{path}"')

def merge_styles(m):
    tag = m.group(0)
    styles = re.findall(r'style="([^"]+)"', tag)
    if len(styles) > 1:
        merged = ' '.join(styles)
        tag = re.sub(r' style="[^"]+"', '', tag)
        tag = tag.replace('>', f' style="{merged}">', 1)
    return tag

new_frame5 = re.sub(r'<[^>]+>', merge_styles, new_frame5)
new_frame5 = re.sub(r'<img(.*?)\s*/>', r'<img\1>', new_frame5)
new_frame5 = re.sub(r'<img([^>]*?style=")', r'<img\1object-fit: cover; ', new_frame5)
new_frame5 = re.sub(r'<div(.*?)\s*/>', r'<div\1></div>', new_frame5)
new_frame5 = re.sub(r'<p(.*?)\s*/>', r'<p\1></p>', new_frame5)

with open('shop.html', 'r', encoding='utf-8') as f:
    shop_html = f.read()

# Replace the old frame 5 with the new one
old_frame5_match = re.search(r'<div[^>]*?data-node-id="134:235"[^>]*?>.*?data-node-id="125:676"', shop_html, re.DOTALL)
if old_frame5_match:
    old_text = old_frame5_match.group(0)
    # We matched up to data-node-id="125:676", which is the start of Frame 6. We should replace up to the div closure before Frame 6.
    old_text = re.sub(r'\s*<div class="" style="position: absolute; height: 121.015625vw; left: 0.15625vw; overflow: clip; top: 248.75vw; width: 99.84375vw;" data-node-id="125:676".*$', '', old_text, flags=re.DOTALL)
    
    shop_html = shop_html.replace(old_text, new_frame5)
    with open('shop.html', 'w', encoding='utf-8') as f:
        f.write(shop_html)
    print("Successfully replaced Frame 5")
else:
    print("Could not find old Frame 5 in shop.html")
