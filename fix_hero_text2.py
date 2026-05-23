import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    'style="z-index: 10; width: 100%; text-align: center; gap: 1.5vw;"',
    'style="z-index: 10; width: 100%; text-align: center; gap: 1.5vw; left: 50%; top: 50%;"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
