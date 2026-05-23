import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'(\.everyday-title \{[^}]*?)font-size:\s*4\.2vw;',
    r'\1font-size: 3.8vw;',
    css
)
css = re.sub(
    r'(\.mood-title \{[^}]*?)font-size:\s*4\.2vw;',
    r'\1font-size: 3.8vw;',
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Font size set to 3.8vw")
