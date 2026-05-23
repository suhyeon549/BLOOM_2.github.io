import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Top Hero
html = re.sub(r'(data-node-id="124:494")', r'class="reveal reveal-up" \1', html)
html = re.sub(r'(data-node-id="124:495")', r'class="reveal reveal-up delay-100" \1', html)
html = re.sub(r'(data-node-id="124:496")', r'class="reveal reveal-up delay-200" \1', html)
html = re.sub(r'(data-node-id="125:629")', r'class="reveal reveal-scale img-zoom-wrap" \1', html)
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="124:488")', r'class="\1 hover-lift" \2', html)
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="124:491")', r'class="\1 hover-lift" \2', html)

# Bottom Ready to Start
html = re.sub(r'(data-node-id="124:603")', r'class="reveal reveal-up" \1', html)
html = re.sub(r'(data-node-id="124:578")', r'class="reveal reveal-up delay-100" \1', html)
html = re.sub(r'(data-node-id="124:579")', r'class="reveal reveal-up delay-100" \1', html)
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="124:581")', r'class="\1 hover-lift" \2', html)
html = re.sub(r'class="([^"]*?)"([^>]*?data-node-id="124:584")', r'class="\1 hover-lift" \2', html)

# Problem & How-to
up_ids = [
    "124:523",
    "124:525",
    "124:567",
    "125:637",
]
for node_id in up_ids:
    html = re.sub(rf'(data-node-id="{node_id}")', r'class="reveal reveal-up" \1', html)

up_delay_ids = [
    "124:524",
    "124:563",
]
for node_id in up_delay_ids:
    html = re.sub(rf'(data-node-id="{node_id}")', r'class="reveal reveal-up delay-100" \1', html)

card_ids = [
    "125:638",
    "125:648",
    "125:658",
]
for node_id in card_ids:
    html = re.sub(rf'(data-node-id="{node_id}")', r'class="reveal reveal-scale hover-lift" \1', html)

html = re.sub(r'(data-node-id="125:624")', r'class="reveal reveal-scale" \1', html)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
