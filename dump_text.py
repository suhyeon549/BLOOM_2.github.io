import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.findall(r'<div[^>]*data-node-id="([^"]+)"[^>]*>.*?<p[^>]*>(.*?)</p>', html, re.DOTALL)
with open('dump.txt', 'w', encoding='utf-8') as out:
    for node_id, text in matches:
        text_clean = re.sub(r'<[^>]+>', '', text).strip()
        if len(text_clean) > 0:
            out.write(f"{node_id}: {text_clean}\n")
