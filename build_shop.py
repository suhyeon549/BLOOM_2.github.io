import re

with open(r'C:\Users\yeons\.gemini\antigravity\brain\a0de5db8-fcea-4037-b511-d410ef8bf03d\.system_generated\steps\415\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'return \((.*?)\);', text, re.DOTALL)
if match:
    jsx = match.group(1)
else:
    print('Failed to find return block')
    exit()

img_defs = {}
for line in text.split('\n'):
    if line.startswith('const img'):
        var_name = line.split(' ')[1]
        url = line.split('"')[1]
        filename = url.split('/')[-1]
        img_defs[var_name] = f'assets/{filename}'

html = jsx

for var_name, path in img_defs.items():
    html = html.replace('{' + var_name + '}', f'"{path}"')

html = html.replace('className=', 'class=')

def replace_tailwind(m):
    classes_str = m.group(1)
    classes = classes_str.split()
    styles = []
    new_classes = []
    
    for c in classes:
        if c.startswith('w-['):
            val = c[3:-1]
            if val.endswith('px'): styles.append(f'width: {float(val[:-2])/12.8}vw;')
            else: styles.append(f'width: {val};')
        elif c.startswith('h-['):
            val = c[3:-1]
            if val.endswith('px'): styles.append(f'height: {float(val[:-2])/12.8}vw;')
            else: styles.append(f'height: {val};')
        elif c.startswith('top-['):
            val = c[5:-1]
            if val.endswith('px'): styles.append(f'top: {float(val[:-2])/12.8}vw;')
            else: styles.append(f'top: {val};')
        elif c.startswith('left-['):
            val = c[6:-1]
            if val.endswith('px'): styles.append(f'left: {float(val[:-2])/12.8}vw;')
            elif val.startswith('calc('):
                inner = val[5:-1]
                parts = re.split(r'([+-])', inner)
                calc_expr = ''
                for p in parts:
                    if p in ['+', '-']: calc_expr += f' {p} '
                    elif p.endswith('px'): calc_expr += f'{float(p[:-2])/12.8}vw'
                    else: calc_expr += p
                styles.append(f'left: calc({calc_expr});')
            else: styles.append(f'left: {val};')
        elif c.startswith('text-['):
            val = c[6:-1]
            if val.endswith('px'): styles.append(f'font-size: {float(val[:-2])/12.8}vw;')
            else: styles.append(f'font-size: {val};')
        elif c.startswith('leading-['):
            val = c[9:-1]
            if val.endswith('px'): styles.append(f'line-height: {float(val[:-2])/12.8}vw;')
            else: styles.append(f'line-height: {val};')
        elif c.startswith('tracking-['):
            val = c[10:-1]
            if val.endswith('px'): styles.append(f'letter-spacing: {float(val[:-2])/12.8}vw;')
            else: styles.append(f'letter-spacing: {val};')
        elif c.startswith('text-#'): styles.append(f'color: {c[5:]};')
        elif c.startswith('bg-#'): styles.append(f'background-color: {c[3:]};')
        elif c.startswith('rounded-['):
            val = c[9:-1]
            if val.endswith('px'): styles.append(f'border-radius: {float(val[:-2])/12.8}vw;')
            else: styles.append(f'border-radius: {val};')
        elif c.startswith('gap-['):
            val = c[5:-1]
            if val.endswith('px'): styles.append(f'gap: {float(val[:-2])/12.8}vw;')
            else: styles.append(f'gap: {val};')
        elif c.startswith('px-['):
            val = c[4:-1]
            if val.endswith('px'): styles.append(f'padding-left: {float(val[:-2])/12.8}vw; padding-right: {float(val[:-2])/12.8}vw;')
        elif c.startswith('py-['):
            val = c[4:-1]
            if val.endswith('px'): styles.append(f'padding-top: {float(val[:-2])/12.8}vw; padding-bottom: {float(val[:-2])/12.8}vw;')
        elif c.startswith('pb-['):
            val = c[4:-1]
            if val.endswith('px'): styles.append(f'padding-bottom: {float(val[:-2])/12.8}vw;')
        elif c.startswith('pt-['):
            val = c[4:-1]
            if val.endswith('px'): styles.append(f'padding-top: {float(val[:-2])/12.8}vw;')
        elif c.startswith('ml-['):
            val = c[4:-1]
            if val.endswith('px'): styles.append(f'margin-left: {float(val[:-2])/12.8}vw;')
        elif c.startswith('mt-['):
            val = c[4:-1]
            if val.endswith('px'): styles.append(f'margin-top: {float(val[:-2])/12.8}vw;')
        elif c.startswith('shadow-['):
            val = c[8:-1]
            val = re.sub(r'(-?\d+(?:\.\d+)?)px', lambda x: f'{float(x.group(1))/12.8}vw', val)
            styles.append(f'box-shadow: {val.replace("_", " ")};')
        elif c.startswith('border-['):
            val = c[8:-1]
            styles.append(f'border-color: {val};')
        elif c.startswith('font-['):
            val = c[6:-1].split(',')[0].replace(':', ' ').replace('_', ' ')
            if 'Montserrat' in val: styles.append("font-family: 'Montserrat', sans-serif;")
            elif 'Pretendard' in val: styles.append("font-family: 'Pretendard', sans-serif;")
            elif 'Be Vietnam Pro' in val: styles.append("font-family: 'Be Vietnam Pro', sans-serif;")
            elif 'Playfair' in val: styles.append("font-family: 'Playfair Display', serif;")
            elif 'Helvetica' in val: styles.append("font-family: 'Helvetica Neue', sans-serif;")
        elif c == 'absolute': styles.append('position: absolute;')
        elif c == 'relative': styles.append('position: relative;')
        elif c == 'flex': styles.append('display: flex;')
        elif c == 'flex-col': styles.append('flex-direction: column;')
        elif c == 'items-center': styles.append('align-items: center;')
        elif c == 'justify-center': styles.append('justify-content: center;')
        elif c == 'justify-between': styles.append('justify-content: space-between;')
        elif c == 'justify-end': styles.append('justify-content: flex-end;')
        elif c == 'text-center': styles.append('text-align: center;')
        elif c == 'uppercase': styles.append('text-transform: uppercase;')
        elif c == 'italic': styles.append('font-style: italic;')
        elif c == 'font-semibold': styles.append('font-weight: 600;')
        elif c == 'font-medium': styles.append('font-weight: 500;')
        elif c == 'font-normal': styles.append('font-weight: 400;')
        elif c == 'whitespace-nowrap': styles.append('white-space: nowrap;')
        elif c == 'whitespace-pre-wrap': styles.append('white-space: pre-wrap;')
        elif c == 'object-cover': styles.append('object-fit: cover;')
        elif c == 'object-bottom': styles.append('object-position: bottom;')
        elif c == 'size-full': styles.append('width: 100%; height: 100%;')
        elif c == 'h-full': styles.append('height: 100%;')
        elif c == 'w-full': styles.append('width: 100%;')
        elif c == 'shrink-0': styles.append('flex-shrink: 0;')
        elif c == 'max-w-none': styles.append('max-width: none;')
        elif c == 'pointer-events-none': styles.append('pointer-events: none;')
        elif c == 'inset-0': styles.append('top: 0; right: 0; bottom: 0; left: 0;')
        elif c == 'opacity-80': styles.append('opacity: 0.8;')
        elif c == 'opacity-75': styles.append('opacity: 0.75;')
        elif c == 'opacity-50': styles.append('opacity: 0.5;')
        elif c == 'opacity-30': styles.append('opacity: 0.3;')
        elif c == 'text-white': styles.append('color: white;')
        elif c == 'text-black': styles.append('color: black;')
        elif c == 'bg-white': styles.append('background-color: white;')
        elif c == 'overflow-hidden': styles.append('overflow: hidden;')
        elif c == '-translate-x-1/2': styles.append('transform: translateX(-50%);')
        elif c == '-translate-y-1/2': styles.append('transform: translateY(-50%);')
        elif c == 'rotate-90': styles.append('transform: rotate(90deg);')
        elif c == 'border': styles.append('border-width: 1px;')
        elif c == 'border-solid': styles.append('border-style: solid;')
        elif c == 'border-t': styles.append('border-top-width: 1px;')
        elif c == 'border-b': styles.append('border-bottom-width: 1px;')
        elif c == 'mb-0': styles.append('margin-bottom: 0;')
        elif c.startswith('size-['):
            val = c[6:-1]
            if val.endswith('px'): styles.append(f'width: {float(val[:-2])/12.8}vw; height: {float(val[:-2])/12.8}vw;')
        elif c.startswith('inset-['):
            val = c[7:-1]
            val = re.sub(r'(-?\d+(?:\.\d+)?)px', lambda x: f'{float(x.group(1))/12.8}vw', val).replace('_', ' ')
            styles.append(f'inset: {val};')
        elif c.startswith('mask-size-['):
            val = c[11:-1].replace('px', '').split('_')
            styles.append(f'mask-size: {float(val[0])/12.8}vw {float(val[1])/12.8}vw; -webkit-mask-size: {float(val[0])/12.8}vw {float(val[1])/12.8}vw;')
        elif c.startswith('mask-position-['):
            val = c[15:-1].replace('px', '').split('_')
            styles.append(f'mask-position: {float(val[0])/12.8}vw {float(val[1])/12.8}vw; -webkit-mask-position: {float(val[0])/12.8}vw {float(val[1])/12.8}vw;')
        elif c == 'mask-no-repeat':
            styles.append('mask-repeat: no-repeat; -webkit-mask-repeat: no-repeat;')
        else:
            new_classes.append(c)
            
    style_str = ' '.join(styles)
    if style_str:
        return f'class="{" ".join(new_classes)}" style="{style_str}"'
    else:
        return f'class="{" ".join(new_classes)}"'

html = re.sub(r'class="([^"]+)"', replace_tailwind, html)

def replace_jsx_style(m):
    inner = m.group(1)
    inner = inner.replace('backgroundImage:', 'background-image:')
    inner = inner.replace('maskImage:', 'mask-image:').replace('-webkit-mask-image:', '')
    inner = inner.replace("`url('${imgImage723}')`", "url('assets/cd0adb4bf34be3ffcd34c8547eac5956c8e9d763.svg')")
    inner = inner.replace("`url('${imgRectangle40}')`", "url('assets/a32079bb82bd37fd61052d6f6eb6b609f8d8c3cf.svg')")

    return f'style="{inner}"'

html = re.sub(r'style=\{\{\s*(.*?)\s*\}\}', replace_jsx_style, html)

def merge_styles(m):
    tag = m.group(0)
    styles = re.findall(r'style="([^"]+)"', tag)
    if len(styles) > 1:
        merged = ' '.join(styles)
        tag = re.sub(r' style="[^"]+"', '', tag)
        tag = tag.replace('>', f' style="{merged}">', 1)
    return tag

html = re.sub(r'<[^>]+>', merge_styles, html)

html = re.sub(r'<img(.*?)\s*/>', r'<img\1>', html)
html = re.sub(r'<div(.*?)\s*/>', r'<div\1></div>', html)
html = re.sub(r'<p(.*?)\s*/>', r'<p\1></p>', html)

final_html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BLOOM | SHOP</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600&family=Montserrat:ital,wght@0,400;0,500;0,600;1,400&family=Playfair+Display:ital@1&family=Helvetica+Neue:wght@500&display=swap" rel="stylesheet">
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
  <link rel="stylesheet" href="style.css">
  <style>
    body {{ margin: 0; padding: 0; background-color: #e5e5e5; display: flex; justify-content: center; font-family: 'Pretendard', sans-serif; color: #2b201f; }}
    .figma-container {{ width: 100vw; height: 5651px; overflow: hidden; position: relative; background: #f8f4e7; }}
  </style>
</head>
<body>
  {html}
<script>
const texts = document.querySelectorAll('p');
texts.forEach(p => {{
  if(p.textContent.trim() === 'ABOUT') {{
    p.outerHTML = '<a href="index.html#everyday" style="' + p.getAttribute('style') + '; text-decoration: none; cursor: pointer; color: inherit;">ABOUT</a>';
  }}
  if(p.textContent.trim() === 'TEAM') {{
    p.outerHTML = '<a href="team.html" style="' + p.getAttribute('style') + '; text-decoration: none; cursor: pointer; color: inherit;">TEAM</a>';
  }}
  if(p.textContent.trim() === 'SHOP') {{
    p.style.cursor = 'pointer';
    p.style.fontWeight = '500';
  }}
}});
const divs = document.querySelectorAll('div');
divs.forEach(div => {{
  if(div.textContent.trim() === 'OOB\\nL\\nM') {{
    div.style.cursor = 'pointer';
    div.onclick = () => window.location.href = 'index.html';
  }}
}});
</script>
</body>
</html>
'''

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print('Generated shop.html')
