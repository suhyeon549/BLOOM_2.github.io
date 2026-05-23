import re

with open('team.html', 'r', encoding='utf-8') as f:
    html = f.read()

script_code = """
<script>
  document.addEventListener("DOMContentLoaded", () => {
    const observerOptions = {
      root: null,
      rootMargin: "0px",
      threshold: 0.15
    };
    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
  });
</script>
</body>
"""

if '<script>' not in html:
    html = html.replace('</body>', script_code)

replacements = [
    (r'class="([^"]*?team-hero-title[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?team-hero-desc[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?team-hero-logo[^"]*?)"', r'class="\1 reveal reveal-up delay-200"'),
    (r'class="([^"]*?team-title-1[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?team-title-desc[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?team-person1-img[^"]*?)"', r'class="\1 reveal reveal-scale hover-scale"'),
    (r'class="([^"]*?team-person1-role[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?team-person1-name[^"]*?)"', r'class="\1 reveal reveal-up delay-200"'),
    (r'class="([^"]*?team-person1-desc[^"]*?)"', r'class="\1 reveal reveal-up delay-300"'),
    (r'class="([^"]*?team-person2-img[^"]*?)"', r'class="\1 reveal reveal-scale hover-scale"'),
    (r'class="([^"]*?team-person2-role[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?team-person2-name[^"]*?)"', r'class="\1 reveal reveal-up delay-200"'),
    (r'class="([^"]*?team-person2-desc[^"]*?)"', r'class="\1 reveal reveal-up delay-300"'),
    (r'class="([^"]*?team-title-2[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?team-promise-text[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?team-bottom-img[^"]*?)"', r'class="\1 reveal reveal-scale"'),
]

for pat, repl in replacements:
    html = re.sub(pat, repl, html)

with open('team.html', 'w', encoding='utf-8') as f:
    f.write(html)
