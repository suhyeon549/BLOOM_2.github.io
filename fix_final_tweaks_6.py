import re

with open('team.html', 'r', encoding='utf-8') as f:
    team_html = f.read()

team_html = re.sub(r'(class="abs team-hero-logo[^"]*) delay-200', r'\1', team_html)
team_html = re.sub(r'(class="abs team-hero-title reveal reveal-up)"', r'\1 delay-200"', team_html)

with open('team.html', 'w', encoding='utf-8') as f:
    f.write(team_html)

with open('shop.html', 'r', encoding='utf-8') as f:
    shop_html = f.read()

shop_html = re.sub(r'(style="[^"]*)(" data-node-id="126:696")', r'\1; z-index: 10;\2', shop_html)
shop_html = re.sub(r'(style="[^"]*)(" data-node-id="124:488")', r'\1; cursor: pointer;\2', shop_html)
shop_html = re.sub(r'(style="[^"]*)(" data-node-id="124:491")', r'\1; cursor: pointer;\2', shop_html)

shop_html = shop_html.replace(' -up reveal hover-lift reveal-up hover-lift delay-200', ' reveal reveal-up hover-lift delay-200')
shop_html = shop_html.replace(' -up ', ' ')
shop_html = shop_html.replace('"-up ', '"')

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(shop_html)

print("Fixed team.html and shop.html buttons")
