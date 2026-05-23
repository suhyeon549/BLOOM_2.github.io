import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

def add_delay(node_id, delay):
    global html
    html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{node_id}")', rf'class="\1 delay-{delay}" \2', html)

tags_text = [
    ("134:276", "100"), ("134:277", "200"), ("134:278", "300"), ("134:279", "400"),
    ("134:283", "100"), ("134:288", "200"), ("134:289", "300"), ("134:290", "400"),
    ("134:294", "100"), ("134:295", "200"), ("134:296", "300"), ("134:297", "400")
]
for tid, delay in tags_text:
    add_delay(tid, delay)

tags_bg = [
    ("134:265", "100"), ("134:266", "200"), ("134:267", "300"), ("134:268", "400"),
    ("134:269", "100"), ("134:270", "200"), ("134:271", "300"), ("134:272", "400"),
    ("134:330", "100"), ("134:331", "200"), ("134:332", "300"), ("134:333", "400")
]
for tid, delay in tags_bg:
    add_delay(tid, delay)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
