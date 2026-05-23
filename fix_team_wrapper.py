import re

with open('team.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'\s*<div class="team-hero-rect"></div>', '', html)

start_idx = html.find('<div class="abs team-hero-logo')
end_idx = html.find('</div>', html.find('<div class="abs flex-col team-hero-desc')) + 6

hero_text_content = html[start_idx:end_idx]

# Remove existing delays and set new ones
hero_text_content = re.sub(r'class="([^"]*?team-hero-logo[^"]*)"', lambda m: f'class="{re.sub(r" delay-\d+", "", m.group(1)).strip()}"', hero_text_content)
hero_text_content = re.sub(r'class="([^"]*?team-hero-title[^"]*)"', lambda m: f'class="{re.sub(r" delay-\d+", "", m.group(1)).strip()} delay-100"', hero_text_content)
hero_text_content = re.sub(r'class="([^"]*?team-hero-desc[^"]*)"', lambda m: f'class="{re.sub(r" delay-\d+", "", m.group(1)).strip()} delay-200"', hero_text_content)

wrapped = f"""    <!-- Hero Content Wrapper -->
    <div class="team-hero-content-wrapper" style="position: relative; z-index: 10; display: block;">
      <div class="team-hero-rect"></div>
{hero_text_content}
    </div>"""

html = html[:start_idx] + wrapped + html[end_idx:]

with open('team.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Team HTML fixed.")
