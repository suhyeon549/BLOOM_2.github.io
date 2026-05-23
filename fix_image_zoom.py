import re

with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* Specific slow zoom for appearance */
.reveal-slow-zoom {
  overflow: hidden;
}
.reveal-slow-zoom img {
  scale: 1;
  transform-origin: center;
  transition: scale 2s cubic-bezier(0.25, 1, 0.5, 1) 0.8s;
}
.reveal-slow-zoom.active img {
  scale: 1.05;
}
""")

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(class=".*?)\bdelay-600\b(.*?"[^>]*?data-node-id="124:491")', r'\1delay-500\2', html)

def repl(m):
    cls_str = m.group(1)
    for ac in ["reveal-scale", "img-zoom-wrap", "delay-100", "delay-200", "delay-300", "delay-400"]:
        cls_str = re.sub(rf'\b{ac}\b', '', cls_str)
    cls_str = re.sub(r'\s+', ' ', cls_str).strip()
    if 'reveal' not in cls_str:
        cls_str += ' reveal'
    final_cls = f"{cls_str} reveal-slow-zoom".strip()
    return f'class="{final_cls}"{m.group(2)}'

html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="125:624")', repl, html)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed successfully.")
