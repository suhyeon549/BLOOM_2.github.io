import os

# 1. Update font size in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    'font-size: 1.40625vw; color: #000000; margin: 0 auto; line-height: 1.6; letter-spacing: -0.078125vw; max-width: 45vw;">BLOOM은 단순한 세정 제품이 아닌',
    'font-size: 1.1vw; color: #000000; margin: 0 auto; line-height: 1.6; letter-spacing: -0.078125vw; max-width: 45vw;">BLOOM은 단순한 세정 제품이 아닌'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Add wrapper in shop.html
with open('shop.html', 'r', encoding='utf-8') as f:
    shop_html = f.read()

target_text = """        <div class="[word-break:break-word] contents" style="display: contents; line-height: 0;" data-node-id="124:522">
          <div class="reveal reveal-up delay-200 reveal reveal-up" style="transform: translateY(-50%); position: absolute; display: flex; flex-direction: column; font-family: 'Montserrat', sans-serif; font-weight: 500; justify-content: center; left: calc(50% - 40.78125vw); font-size: 1.5625vw; color: black; top: 26.328125vw; letter-spacing: -0.15625vw; white-space: nowrap;"  data-node-id="124:523">
            <p class="" style="line-height: 3.28125vw;">향과 기능만으로 비누를 고르기 어렵지 않으셨나요?</p>
          </div>
          <div class="not-italic reveal reveal-up delay-400 reveal reveal-up delay-100" style="transform: translateY(-50%); position: absolute; display: flex; flex-direction: column; font-family: 'Pretendard', sans-serif; justify-content: center; left: calc(50% - 40.78125vw); color: #2b201f; font-size: 0.9375vw; top: 31.0546875vw; letter-spacing: -0.078125vw; width: 41.640625vw; white-space: pre-wrap;"  data-node-id="124:524">
            <p class="" style="line-height: 1.4; margin-bottom: 0;">기존 비누들은 단순히 세정력이나 향기만을 강조합니다. 하지만 우리의 일상은 매일 다른 감정과 날씨, 계절의</p>
            <p class="" style="line-height: 1.4; margin-bottom: 0;">흐름 속에 있습니다. 가치 소비와 개인화된 경험을 중시하는 MZ 세대를 위해, 기존의 단순한 향, 기능 중심 나열에서 벗어나</p>
            <p class="" style="line-height: 1.4;">자신의 감정과 분위기에 맞는 제품을 찾기 어려운 문제점을 해결하고, 당신의 오늘에 가장 잘 어울리는 감각적인 비누를 제안합니다.</p>
          </div>
          <div class="reveal reveal-up reveal reveal-up" style="transform: translateY(-50%); position: absolute; display: flex; flex-direction: column; font-family: 'Montserrat', sans-serif; font-weight: 500; justify-content: center; left: 9.140625vw; color: #2b201f; font-size: 3.125vw; top: 20.078125vw; letter-spacing: -0.078125vw; white-space: nowrap;"  data-node-id="124:525">
            <p class="" style="line-height: 1.1; margin-bottom: 0;">Soap</p>
            <p class="" style="line-height: 1.1;">for Your Mood</p>
          </div>
        </div>"""

replacement_text = """        <div class="[word-break:break-word] contents" style="display: contents; line-height: 0;" data-node-id="124:522">
          <div class="problem-content-wrapper" style="position: relative; z-index: 10; display: block;">
          <div class="reveal reveal-up delay-200 reveal reveal-up" style="transform: translateY(-50%); position: absolute; display: flex; flex-direction: column; font-family: 'Montserrat', sans-serif; font-weight: 500; justify-content: center; left: calc(50% - 40.78125vw); font-size: 1.5625vw; color: black; top: 26.328125vw; letter-spacing: -0.15625vw; white-space: nowrap;"  data-node-id="124:523">
            <p class="" style="line-height: 3.28125vw;">향과 기능만으로 비누를 고르기 어렵지 않으셨나요?</p>
          </div>
          <div class="not-italic reveal reveal-up delay-400 reveal reveal-up delay-100" style="transform: translateY(-50%); position: absolute; display: flex; flex-direction: column; font-family: 'Pretendard', sans-serif; justify-content: center; left: calc(50% - 40.78125vw); color: #2b201f; font-size: 0.9375vw; top: 31.0546875vw; letter-spacing: -0.078125vw; width: 41.640625vw; white-space: pre-wrap;"  data-node-id="124:524">
            <p class="" style="line-height: 1.4; margin-bottom: 0;">기존 비누들은 단순히 세정력이나 향기만을 강조합니다. 하지만 우리의 일상은 매일 다른 감정과 날씨, 계절의</p>
            <p class="" style="line-height: 1.4; margin-bottom: 0;">흐름 속에 있습니다. 가치 소비와 개인화된 경험을 중시하는 MZ 세대를 위해, 기존의 단순한 향, 기능 중심 나열에서 벗어나</p>
            <p class="" style="line-height: 1.4;">자신의 감정과 분위기에 맞는 제품을 찾기 어려운 문제점을 해결하고, 당신의 오늘에 가장 잘 어울리는 감각적인 비누를 제안합니다.</p>
          </div>
          <div class="reveal reveal-up reveal reveal-up" style="transform: translateY(-50%); position: absolute; display: flex; flex-direction: column; font-family: 'Montserrat', sans-serif; font-weight: 500; justify-content: center; left: 9.140625vw; color: #2b201f; font-size: 3.125vw; top: 20.078125vw; letter-spacing: -0.078125vw; white-space: nowrap;"  data-node-id="124:525">
            <p class="" style="line-height: 1.1; margin-bottom: 0;">Soap</p>
            <p class="" style="line-height: 1.1;">for Your Mood</p>
          </div>
          </div>
        </div>"""

if target_text in shop_html:
    shop_html = shop_html.replace(target_text, replacement_text)
    with open('shop.html', 'w', encoding='utf-8') as f:
        f.write(shop_html)
    print("Wrapper added.")
else:
    print("Target text not found.")
