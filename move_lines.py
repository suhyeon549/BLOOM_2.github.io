import re

with open('team.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'\s*<div class="team-hero-line-01">.*?</div>\s*<div class="team-hero-line-02">.*?</div>'
match = re.search(pattern, html, flags=re.DOTALL)

if match:
    lines_str = match.group(0)
    html = html.replace(lines_str, '')
    
    target = '<div class="team-hero-rect"></div>'
    html = html.replace(target, target + lines_str)
    print("Moved lines successfully.")
else:
    print("Could not find lines to move.")

with open('team.html', 'w', encoding='utf-8') as f:
    f.write(html)
