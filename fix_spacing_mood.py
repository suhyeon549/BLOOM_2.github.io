import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. line-height for .mood-text-2
css = re.sub(
    r'(\.mood-text-2 p \{[^}]*?)line-height:\s*3\.28125vw;',
    r'\1line-height: 1.4;',
    css
)

# 2. Block spacing gaps
# .mood-text-2 top: 137.1875vw -> 138.6875vw
css = re.sub(
    r'(\.mood-text-2 \{[^}]*?)top:\s*137\.1875vw;',
    r'\1top: 138.6875vw;',
    css
)

# .mood-text-1 top: 141.9140vw -> 144.9375vw
css = re.sub(
    r'(\.mood-text-1 \{[^}]*?)top:\s*141\.9140vw;',
    r'\1top: 144.9375vw;',
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Mood spacing updated.")
