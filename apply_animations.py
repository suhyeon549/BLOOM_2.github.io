import re

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

# index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements_index = [
    (r'class="([^"]*?brand-statement[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?everyday-text-1[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?everyday-text-2[^"]*?)"', r'class="\1 reveal reveal-up delay-200"'),
    (r'class="([^"]*?everyday-title[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?everyday-img-moon[^"]*?)"', r'class="\1 reveal reveal-scale"'),
    (r'class="([^"]*?everyday-img-snip-1[^"]*?)"', r'class="\1 reveal reveal-scale delay-100"'),
    (r'class="([^"]*?everyday-img-snip-2[^"]*?)"', r'class="\1 reveal reveal-scale delay-200"'),
    (r'class="([^"]*?mood-text-1[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?mood-text-2[^"]*?)"', r'class="\1 reveal reveal-up delay-200"'),
    (r'class="([^"]*?mood-title[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?rooted-title[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?feature-box-1[^"]*?)"', r'class="\1 reveal reveal-scale hover-lift"'),
    (r'class="([^"]*?feature-box-2[^"]*?)"', r'class="\1 reveal reveal-scale hover-lift delay-100"'),
    (r'class="([^"]*?feature-box-3[^"]*?)"', r'class="\1 reveal reveal-scale hover-lift delay-200"'),
    (r'class="([^"]*?feature-text-1-desc[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?feature-text-2-desc[^"]*?)"', r'class="\1 reveal reveal-up delay-200"'),
    (r'class="([^"]*?feature-text-3-desc[^"]*?)"', r'class="\1 reveal reveal-up delay-300"'),
]

for pat, repl in replacements_index:
    html = re.sub(pat, repl, html)

if '<script>' not in html:
    html = html.replace('</body>', script_code)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# shop.html
with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements_shop = [
    (r'class="([^"]*?shop-hero-title[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?shop-hero-desc[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?shop-hero-desc2[^"]*?)"', r'class="\1 reveal reveal-up delay-200"'),
    (r'class="([^"]*?shop-hero-img[^"]*?)"', r'class="\1 reveal reveal-scale img-zoom-wrap hover-scale"'),
    (r'class="([^"]*?shop-section-title[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?shop-section-subtitle[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?shop-problem-main[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?shop-problem-sub1[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?shop-how-title[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?shop-how-subtitle[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?shop-how-card[^"]*?)"', r'class="\1 reveal reveal-scale hover-lift"'),
    (r'class="([^"]*?shop-case-title[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?shop-case-desc[^"]*?)"', r'class="\1 reveal reveal-up delay-100"'),
    (r'class="([^"]*?shop-ready-title[^"]*?)"', r'class="\1 reveal reveal-up"'),
    (r'class="([^"]*?shop-bg-img1[^"]*?)"', r'class="\1 reveal reveal-scale img-zoom-wrap"'),
    (r'class="([^"]*?shop-bg-img2[^"]*?)"', r'class="\1 reveal reveal-scale img-zoom-wrap delay-100"'),
]

for pat, repl in replacements_shop:
    html = re.sub(pat, repl, html)

# For shop.html Frame 6 elements
# Note: they might already have a class="" attribute
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="134:273")', r'class="\1 reveal reveal-up" \2', html)
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="134:302")', r'class="\1 reveal reveal-scale hover-scale" \2', html)
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="134:280")', r'class="\1 reveal reveal-up delay-100" \2', html)
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="134:300")', r'class="\1 reveal reveal-scale hover-scale delay-100" \2', html)
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="134:291")', r'class="\1 reveal reveal-up delay-200" \2', html)
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="134:301")', r'class="\1 reveal reveal-scale hover-scale delay-200" \2', html)

# Frame 5 features
html = re.sub(r'class="([^"]*?)"([^>]*?data-name="Problem Area")', r'class="\1 hover-lift" \2', html)
html = re.sub(r'class="([^"]*?)"([^>]*?data-name="How-to Step")', r'class="\1 hover-lift" \2', html)


if '<script>' not in html:
    html = html.replace('</body>', script_code)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied animations")
