import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_rainy = """      <div class=" reveal reveal-up" data-reveal-group="rainy" style="word-break: break-word; display: contents; line-height: 0;" data-node-id="134:273">
        <div class="" style="transform: translateY(-50%); position: absolute; display: flex; flex-direction: column; font-family: 'Montserrat', sans-serif; font-weight: 500; justify-content: center; left: 9.0625vw; font-size: 2.5vw; color: black; top: 29.921875vw; letter-spacing: -0.15625vw; white-space: nowrap;" data-node-id="134:274">"""

new_rainy = """      <div class="" style="word-break: break-word; display: contents; line-height: 0;" data-node-id="134:273">
        <div class="reveal reveal-up" data-reveal-group="rainy" style="transform: translateY(-50%); position: absolute; display: flex; flex-direction: column; font-family: 'Montserrat', sans-serif; font-weight: 500; justify-content: center; left: 9.0625vw; font-size: 2.5vw; color: black; top: 29.921875vw; letter-spacing: -0.15625vw; white-space: nowrap;" data-node-id="134:274">"""

if old_rainy in html:
    html = html.replace(old_rainy, new_rainy)
else:
    print("Rainy Blue not found")

old_cloudy = """      <div class=" reveal reveal-up delay-100 reveal reveal-up" data-reveal-group="cloudy" style="display: contents;"  data-node-id="134:280">
        <div class="" style="transform: translateY(-50%); word-break: break-word; position: absolute; display: flex; flex-direction: column; font-family: 'Montserrat', sans-serif; font-weight: 500; justify-content: center; line-height: 0; left: 9.296875vw; font-size: 2.5vw; color: black; top: 92.265625vw; letter-spacing: -0.15625vw; white-space: nowrap;" data-node-id="134:281">"""

new_cloudy = """      <div class="" style="display: contents;"  data-node-id="134:280">
        <div class="reveal reveal-up" data-reveal-group="cloudy" style="transform: translateY(-50%); word-break: break-word; position: absolute; display: flex; flex-direction: column; font-family: 'Montserrat', sans-serif; font-weight: 500; justify-content: center; line-height: 0; left: 9.296875vw; font-size: 2.5vw; color: black; top: 92.265625vw; letter-spacing: -0.15625vw; white-space: nowrap;" data-node-id="134:281">"""

if old_cloudy in html:
    html = html.replace(old_cloudy, new_cloudy)
else:
    print("Cloudy Rest not found")

old_autumn = """      <div class=" reveal reveal-up delay-200 reveal reveal-up" data-reveal-group="autumn" style="word-break: break-word; display: contents; line-height: 0;"  data-node-id="134:291">
        <div class="" style="transform: translateY(-50%); position: absolute; display: flex; flex-direction: column; font-family: 'Montserrat', sans-serif; font-weight: 500; justify-content: center; left: 52.578125vw; font-size: 2.5vw; color: black; top: 60.703125vw; letter-spacing: -0.15625vw; white-space: nowrap;" data-node-id="134:292">"""

new_autumn = """      <div class="" style="word-break: break-word; display: contents; line-height: 0;"  data-node-id="134:291">
        <div class="reveal reveal-up" data-reveal-group="autumn" style="transform: translateY(-50%); position: absolute; display: flex; flex-direction: column; font-family: 'Montserrat', sans-serif; font-weight: 500; justify-content: center; left: 52.578125vw; font-size: 2.5vw; color: black; top: 60.703125vw; letter-spacing: -0.15625vw; white-space: nowrap;" data-node-id="134:292">"""

if old_autumn in html:
    html = html.replace(old_autumn, new_autumn)
else:
    print("Autumn Harvest not found")

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Text wrappers fixed.")
