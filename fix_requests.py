import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_tag = '<div class="abs flex-col center-xy everyday-text-1'
end_tag = '<!-- Moon/Star Soap Image -->'

start_idx = html.find(start_tag)
end_idx = html.find(end_tag)

if start_idx != -1 and end_idx != -1 and "everyday-content-wrapper" not in html[start_idx:end_idx]:
    content = html[start_idx:end_idx]
    wrapped = f'<div class="everyday-content-wrapper" style="position: relative; z-index: 10;">\n    {content}    </div>\n    '
    html = html[:start_idx] + wrapped + html[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# .mood-title
css = re.sub(r'(\.mood-title \{[^}]*?)font-size:\s*4\.6875vw;', r'\1font-size: 3.125vw;', css)
css = re.sub(r'(\.mood-title p \{[^}]*?)line-height:\s*4\.9219vw;', r'\1line-height: 1.1;', css)

# .mood-text-2
css = re.sub(r'(\.mood-text-2 \{[^}]*?)font-size:\s*2\.5vw;', r'\1font-size: 1.5625vw;', css)
css = re.sub(r'(\.mood-text-2 p \{[^}]*?)line-height:\s*3\.2812vw;', r'\1line-height: 3.28125vw;', css)
css = re.sub(r'(\.mood-text-2 \{[^}]*?)top:\s*140\.7031vw;', r'\1top: 137.1875vw;', css)

# .mood-text-1
css = re.sub(r'(\.mood-text-1 \{[^}]*?)font-size:\s*1\.4062vw;', r'\1font-size: 0.9375vw;', css)
css = re.sub(r'(\.mood-text-1 p \{[^}]*?)line-height:\s*2\.1875vw;', r'\1line-height: 1.4;', css)
css = re.sub(r'(\.mood-text-1 \{[^}]*?)top:\s*148\.8281vw;', r'\1top: 141.9140vw;', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixes applied.")
