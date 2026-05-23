import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'(\.everyday-text-1 \{[^}]*?)top:\s*91\.3281vw;',
    r'\1top: 86.8359vw;',
    css
)

css = re.sub(
    r'(\.everyday-text-2 \{[^}]*?)left:\s*calc\([^)]+\);',
    r'\1left: 50%; text-align: center;',
    css
)
css = re.sub(
    r'(\.everyday-text-2 \{[^}]*?)top:\s*84\.8438vw;',
    r'\1top: 82.1094vw;',
    css
)

css = re.sub(
    r'(\.everyday-title \{[^}]*?)left:\s*calc\([^)]+\);',
    r'\1left: 50%;',
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)


with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<div class="abs flex-col center-y everyday-text-2 reveal reveal-up delay-200">',
    '<div class="abs flex-col center-xy everyday-text-2 reveal reveal-up delay-200">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Spacing and centering fixed.")
