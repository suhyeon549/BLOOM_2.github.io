import re

with open('shop.html', 'r', encoding='utf-8') as f:
    html = f.read()

def add_class(node_id, cls):
    global html
    if re.search(rf'class="[^"]*"{re.escape(f" data-node-id=\"{node_id}\"")}', html):
        html = re.sub(rf'class="([^"]*?)"([^>]*?data-node-id="{node_id}")', rf'class="\1 {cls}" \2', html)
    else:
        html = re.sub(rf'(data-node-id="{node_id}")', rf'class="{cls}" \1', html)

tags_bg = [
    "134:265", "134:266", "134:267", "134:268", 
    "134:269", "134:270", "134:271", "134:272", 
    "134:330", "134:331", "134:332", "134:333", 
]
for tid in tags_bg:
    add_class(tid, "reveal reveal-scale hover-lift")

tags_text = [
    "134:276", "134:277", "134:278", "134:279",
    "134:283", "134:288", "134:289", "134:290",
    "134:294", "134:295", "134:296", "134:297"
]
for tid in tags_text:
    add_class(tid, "reveal reveal-scale")

add_class("134:275", "reveal reveal-up delay-100")
add_class("134:282", "reveal reveal-up delay-100")
add_class("134:293", "reveal reveal-up delay-100")

add_class("134:350", "reveal reveal-up")
add_class("134:280", "reveal reveal-up")
add_class("134:291", "reveal reveal-up")

add_class("134:235", "reveal reveal-up")
add_class("134:246", "reveal reveal-up delay-100")
add_class("134:334", "reveal reveal-up delay-200")

for tid in ["134:343", "134:344", "134:345"]:
    add_class(tid, "reveal reveal-up")
for tid in ["134:346", "134:347", "134:348", "134:349"]:
    add_class(tid, "reveal reveal-up delay-100")

for tid in ["134:351", "134:352", "134:353"]:
    add_class(tid, "reveal reveal-scale delay-200")

add_class("134:298", "reveal reveal-up")
add_class("134:299", "reveal reveal-up delay-100")

add_class("125:669", "reveal reveal-up")
add_class("125:671", "reveal reveal-up delay-100")
add_class("125:668", "reveal reveal-up delay-200")

# Add hover effect to the three main cards in Frame 6
add_class("134:302", "hover-lift")
add_class("134:300", "hover-lift")
add_class("134:301", "hover-lift")

# Add hover effect to bottom big image
add_class("125:679", "img-zoom-wrap hover-scale")
add_class("125:680", "img-zoom-wrap")

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Detailed animations added.")
