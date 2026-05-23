import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
.reveal-expand-x {
  transform: scaleX(0);
  transform-origin: center;
  transition: transform 1s cubic-bezier(0.25, 1, 0.5, 1);
}
.reveal.active.reveal-expand-x {
  transform: scaleX(1);
}
.delay-300 { transition-delay: 0.3s; }
.delay-400 { transition-delay: 0.4s; }
"""

if ".reveal-expand-x" not in css:
    css += new_css
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

with open('team.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<div class="team-hero-rect"></div>',
    '<div class="team-hero-rect reveal reveal-expand-x delay-0"></div>'
)

html = html.replace(
    '<div class="abs team-hero-logo reveal reveal-up">',
    '<div class="abs team-hero-logo reveal reveal-up delay-200">'
)

html = html.replace(
    '<div class="abs team-hero-title reveal reveal-up delay-100">',
    '<div class="abs team-hero-title reveal reveal-up delay-300">'
)

html = html.replace(
    '<div class="abs flex-col team-hero-desc reveal reveal-up delay-200">',
    '<div class="abs flex-col team-hero-desc reveal reveal-up delay-400">'
)

with open('team.html', 'w', encoding='utf-8') as f:
    f.write(html)
