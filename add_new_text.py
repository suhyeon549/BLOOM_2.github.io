import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_block = """
    <!-- Requested Text Block -->
    <div class="abs flex-col center-y reveal reveal-up" style="top: 210vw; width: 100vw; text-align: center; gap: 2vw; z-index: 10;">
      <p style="font-family: 'Montserrat', sans-serif; font-size: 3.125vw; font-weight: 500; color: #2b201f; margin: 0; letter-spacing: -0.078125vw;">Soap — <br>for your daily moods.</p>
      <p style="font-family: 'Pretendard', sans-serif; font-size: 1.40625vw; color: black; margin: 0; letter-spacing: -0.078125vw; line-height: 1.625; max-width: 50vw; margin-left: auto; margin-right: auto; word-break: break-word;">BLOOM은 단순한 세정 제품이 아닌, 하루의 분위기와 감각을 선택하는 작은 라이프스타일 오브제로서의 비누를 제안합니다.</p>
    </div>
"""

# Insert before <!-- Footer -->
html = html.replace('    <!-- Footer -->', new_block + '\n    <!-- Footer -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added new block successfully.")
