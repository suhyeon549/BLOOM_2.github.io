import re

with open('shop.html', 'r', encoding='utf-8') as f:
    shop_html = f.read()

shop_html = shop_html.replace(
    'flex-direction: column; gap: 2.578125vw; align-items: center;',
    'flex-direction: column; gap: 1.5vw; align-items: center;'
)

shop_html = shop_html.replace(
    "font-family: 'Pretendard', sans-serif; justify-content: center; margin-top: 3.4375vw; position: relative;",
    "font-family: 'Pretendard', sans-serif; justify-content: center; margin-top: 2.0vw; position: relative;"
)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(shop_html)

print("Gaps reduced.")
