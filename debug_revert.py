with open('shop.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'data-node-id="125:673"', text)
if m:
    idx = text.find(m.group(0))
    print("Found 125:673 at", idx)
    print(text[idx-200:idx+300])

# check where 132:111 is
m2 = re.search(r'data-node-id="132:111"', text)
if m2:
    idx2 = text.find(m2.group(0))
    print("Found 132:111 at", idx2)
