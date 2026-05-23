import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    "color: #FFFFFF; margin: 0; line-height: 1.6; letter-spacing: -0.078125vw; max-width: 45vw;",
    "color: #FFFFFF; margin: 0 auto; line-height: 1.6; letter-spacing: -0.078125vw; max-width: 45vw;"
)

html = html.replace(
    'style="z-index: 10; width: 100%; text-align: center; gap: 1.5vw; left: 50%; top: 50%;"',
    'style="z-index: 10; width: 100%; text-align: center; gap: 1.5vw; left: 50%; top: 50%; align-items: center;"'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
