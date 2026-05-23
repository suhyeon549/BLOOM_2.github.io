import re

with open(r'C:\Users\yeons\.gemini\antigravity\brain\a0de5db8-fcea-4037-b511-d410ef8bf03d\.system_generated\steps\577\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'<div[^>]*data-node-id="124:429"[^>]*>', text)
if match:
    print(match.group(0))
else:
    print("Not found")

# also let's just find the w-[1920px] or similar
widths = re.findall(r'w-\[(\d+)px\]', text)
if widths:
    widths = [int(w) for w in widths]
    print("Max width:", max(widths))
