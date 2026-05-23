import re
with open('shop.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'(data-node-id="132:111".*?height:\s*)25\.3125vw', r'\g<1>25.390625vw', text, flags=re.DOTALL)
text = re.sub(r'left:\s*-0\.078125vw;\s*width:\s*25\.46875vw;\s*height:\s*25\.46875vw;\s*top:\s*38\.046875vw;', r'left: 0vw; width: 25.390625vw; height: 25.390625vw; top: 38.125vw;', text, flags=re.DOTALL)

def expand_img(m):
    block = m.group(0)
    block = block.replace('width: 100%; height: 100%;', 'width: 102%; height: 102%; top: -1%; left: -1%;')
    return block

text = re.sub(r'<div[^>]*data-node-id="132:11[1-4]".*?</div>', expand_img, text, flags=re.DOTALL)

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Fixed')
