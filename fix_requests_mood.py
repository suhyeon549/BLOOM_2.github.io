import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'(\.everyday-title \{[^}]*?)font-size:\s*3\.125vw;',
    r'\1font-size: 3.5vw;',
    css
)
css = re.sub(
    r'(\.mood-title \{[^}]*?)font-size:\s*3\.125vw;',
    r'\1font-size: 3.5vw;',
    css
)

css = re.sub(
    r'(\.mood-text-2 \{[^}]*?)top:\s*138\.6875vw;',
    r'\1top: 137.9375vw;',
    css
)
css = re.sub(
    r'(\.mood-text-1 \{[^}]*?)top:\s*144\.9375vw;',
    r'\1top: 143.4375vw;',
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_tag = '<div class="abs flex-col center-y mood-text-1'
end_tag = '<!-- Rooted Section'

start_idx = html.find(start_tag)
end_idx = html.find(end_tag)

if start_idx != -1 and end_idx != -1 and "mood-content-wrapper" not in html[start_idx:end_idx]:
    content = html[start_idx:end_idx]
    wrapped = f'<div class="mood-content-wrapper" style="position: relative; z-index: 10;">\n    {content}    </div>\n    '
    html = html[:start_idx] + wrapped + html[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

print("Updates applied.")
