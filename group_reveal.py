import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<div class=" reveal reveal-up"  style="word-break: break-word; display: contents; line-height: 0;" data-node-id="134:273">',
    '<div class=" reveal reveal-up" data-reveal-group="rainy" style="word-break: break-word; display: contents; line-height: 0;" data-node-id="134:273">'
)
html = html.replace(
    '<div class=" reveal reveal-scale hover-scale hover-lift"  style="position: absolute; height: 24.921875vw; left: 50.625vw; border-radius: 1.875vw; top: 21.796875vw; width: 39.765625vw;"  data-node-id="134:302" data-name="image 714">',
    '<div class=" reveal reveal-scale hover-scale hover-lift" data-reveal-group="rainy" style="position: absolute; height: 24.921875vw; left: 50.625vw; border-radius: 1.875vw; top: 21.796875vw; width: 39.765625vw;"  data-node-id="134:302" data-name="image 714">'
)

html = html.replace(
    '<div class=" reveal reveal-up delay-100 reveal reveal-up"  style="display: contents;"  data-node-id="134:280">',
    '<div class=" reveal reveal-up delay-100 reveal reveal-up" data-reveal-group="cloudy" style="display: contents;"  data-node-id="134:280">'
)
html = html.replace(
    '<div class=" reveal reveal-scale hover-scale delay-100 hover-lift"  style="position: absolute; height: 25.15625vw; left: 50.625vw; border-radius: 1.875vw; top: 84.0625vw; width: 39.84375vw;"  data-node-id="134:300" data-name="Cloudy Rest Soap Experience">',
    '<div class=" reveal reveal-scale hover-scale delay-100 hover-lift" data-reveal-group="cloudy" style="position: absolute; height: 25.15625vw; left: 50.625vw; border-radius: 1.875vw; top: 84.0625vw; width: 39.84375vw;"  data-node-id="134:300" data-name="Cloudy Rest Soap Experience">'
)

html = html.replace(
    '<div class=" reveal reveal-up delay-200 reveal reveal-up"  style="word-break: break-word; display: contents; line-height: 0;"  data-node-id="134:291">',
    '<div class=" reveal reveal-up delay-200 reveal reveal-up" data-reveal-group="autumn" style="word-break: break-word; display: contents; line-height: 0;"  data-node-id="134:291">'
)
html = html.replace(
    '<div class=" reveal reveal-scale hover-scale delay-200 hover-lift"  style="position: absolute; height: 25.15625vw; left: 9.296875vw; border-radius: 1.875vw; top: 54.21875vw; width: 39.765625vw;"  data-node-id="134:301" data-name="Autumn Harvest Soap Experience">',
    '<div class=" reveal reveal-scale hover-scale delay-200 hover-lift" data-reveal-group="autumn" style="position: absolute; height: 25.15625vw; left: 9.296875vw; border-radius: 1.875vw; top: 54.21875vw; width: 39.765625vw;"  data-node-id="134:301" data-name="Autumn Harvest Soap Experience">'
)

old_script = """    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);"""

new_script = """    const observer = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          
          const group = entry.target.getAttribute('data-reveal-group');
          if (group) {
            document.querySelectorAll(`[data-reveal-group="${group}"]`).forEach(el => {
              el.classList.add('active');
              observer.unobserve(el);
            });
          }
          
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);"""

if old_script in html:
    html = html.replace(old_script, new_script)
else:
    print("Script not found for replacement.")

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Grouping applied.")
