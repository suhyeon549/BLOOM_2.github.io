import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'(\.everyday-title \{[^}]*?)font-size:\s*4\.6875vw;', r'\1font-size: 3.125vw;', css)
css = re.sub(r'(\.everyday-title p \{[^}]*?)line-height:\s*4\.9219vw;', r'\1line-height: 1.1;', css)

css = re.sub(r'(\.everyday-text-2 \{[^}]*?)font-size:\s*2\.5vw;', r'\1font-size: 1.5625vw;', css)
css = re.sub(r'(\.everyday-text-2 p \{[^}]*?)line-height:\s*3\.2812vw;', r'\1line-height: 3.28125vw;', css)

css = re.sub(r'(\.everyday-text-1 \{[^}]*?)font-size:\s*1\.4062vw;', r'\1font-size: 0.9375vw;', css)
css = re.sub(r'(\.everyday-text-1 p \{[^}]*?)line-height:\s*2\.1875vw;', r'\1line-height: 1.4;', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Font sizes updated.")
