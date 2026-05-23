import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the block I added at the bottom
block_start = html.find('    <!-- Requested Text Block -->')
if block_start != -1:
    block_end = html.find('    <!-- Footer -->', block_start)
    if block_end != -1:
        html = html[:block_start] + html[block_end:]

# Create the text block to be placed inside hero-bg-wrapper
new_hero_text = """
      <div class="abs flex-col center-xy reveal reveal-up delay-100" style="z-index: 10; width: 100%; text-align: center; gap: 1.5vw;">
        <p style="font-family: 'Montserrat', sans-serif; font-size: 4.6875vw; color: #FFFFFF; font-weight: 500; margin: 0; line-height: 1.2; letter-spacing: -0.1vw;">Soap — <br>for your daily moods.</p>
        <p style="font-family: 'Pretendard', sans-serif; font-size: 1.40625vw; color: #FFFFFF; margin: 0; line-height: 1.6; letter-spacing: -0.078125vw; max-width: 45vw;">BLOOM은 단순한 세정 제품이 아닌, 하루의 분위기와 감각을 선택하는 작은 라이프스타일 오브제로서의 비누를 제안합니다.</p>
      </div>
"""

# Inject into hero-bg-wrapper
if "Soap — <br>for your daily moods." not in html:
    html = re.sub(
        r'(<div class="abs hero-bg-wrapper">\s*<img[^>]*>)\s*(</div>)',
        r'\1\n' + new_hero_text + r'\n\2',
        html,
        flags=re.DOTALL
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Moved to hero-bg-wrapper")
