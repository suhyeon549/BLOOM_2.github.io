import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    'class="[word-break:break-word] reveal reveal-up reveal reveal-up"',
    'class="[word-break:break-word] reveal reveal-up"'
)

html = html.replace(
    'class="reveal reveal-up delay-200 reveal reveal-up delay-100"',
    'class="reveal reveal-up delay-100"'
)

html = html.replace(
    'class="reveal reveal-up delay-200 reveal reveal-up delay-200"',
    'class="reveal reveal-up delay-100"'
)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Animations sequenced.")
