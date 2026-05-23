import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Everyday sequence
html = html.replace(
    '<div class="abs flex-col center-xy everyday-text-1 reveal reveal-up delay-100">',
    '<div class="abs flex-col center-xy everyday-text-1 reveal reveal-up delay-200">'
)
html = html.replace(
    '<div class="abs flex-col center-xy everyday-text-2 reveal reveal-up delay-200">',
    '<div class="abs flex-col center-xy everyday-text-2 reveal reveal-up delay-100">'
)

# 2. Mood sequence
html = html.replace(
    '<div class="abs flex-col center-y mood-text-1 reveal reveal-up delay-100">',
    '<div class="abs flex-col center-y mood-text-1 reveal reveal-up delay-200">'
)
html = html.replace(
    '<div class="abs flex-col center-y mood-text-2 reveal reveal-up delay-200">',
    '<div class="abs flex-col center-y mood-text-2 reveal reveal-up delay-100">'
)

# 3. minimal_lifestyle.png animation
html = html.replace(
    '<div class="abs center-x mood-img-wrap">',
    '<div class="abs center-x mood-img-wrap reveal reveal-scale">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 4 & 5. style.css updates
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# .rooted-title font-size
css = re.sub(
    r'(\.rooted-title \{[^}]*?)font-size:\s*4\.6875vw;',
    r'\1font-size: 3.8vw;',
    css
)

# .feature-text-*-desc font-size
css = re.sub(
    r'(\.feature-text-1-desc \{[^}]*?)font-size:\s*1\.4062vw;',
    r'\1font-size: 1.1vw;',
    css
)
css = re.sub(
    r'(\.feature-text-2-desc \{[^}]*?)font-size:\s*1\.4062vw;',
    r'\1font-size: 1.1vw;',
    css
)
css = re.sub(
    r'(\.feature-text-3-desc \{[^}]*?)font-size:\s*1\.4062vw;',
    r'\1font-size: 1.1vw;',
    css
)

# .feature-desc-p line-height
css = re.sub(
    r'(\.feature-desc-p \{[^}]*?)line-height:\s*2\.1875vw;',
    r'\1line-height: 1.6;',
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("All 5 fixes applied.")
