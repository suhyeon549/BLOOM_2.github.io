import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'(\.team-hero-title \{[^}]*?)font-size:\s*2\.8125vw;',
    r'\1font-size: 2.4vw;',
    css
)
css = re.sub(
    r'(\.team-hero-title \{[^}]*?)font-weight:\s*600;',
    r'\1font-weight: 400;',
    css
)

css = re.sub(
    r'(\.team-hero-desc \{[^}]*?)font-size:\s*1\.4062vw;',
    r'\1font-size: 1.1vw;',
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Team hero fonts adjusted.")
