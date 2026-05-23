import re

with open('update_frame5.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Point back to 1202 output
text = text.replace(r'steps\1306\output.txt', r'steps\1202\output.txt')

# The new HTML in 1202 has data-node-id="125:673"
text = text.replace(r'data-node-id="134:235"', r'data-node-id="125:673"')

# But we must search for 134:235 in shop.html because that's what's currently there!
# The script currently has: old_frame5_match = re.search(r'<div[^>]*?data-node-id="125:673"[^>]*?>.*?data-node-id="125:676"', shop_html, re.DOTALL)
# Wait, because we just replaced 134:235 with 125:673 on the line above, it now says:
# old_frame5_match = re.search(r'<div[^>]*?data-node-id="125:673"[^>]*?>.*?data-node-id="125:676"', shop_html, re.DOTALL)
# So we need to change it back to 134:235 ONLY for this specific line!
text = text.replace(
    r'old_frame5_match = re.search(r\'<div[^>]*?data-node-id="125:673"[^>]*?>.*?data-node-id="125:676"\', shop_html, re.DOTALL)',
    r'old_frame5_match = re.search(r\'<div[^>]*?data-node-id="134:235"[^>]*?>.*?data-node-id="125:676"\', shop_html, re.DOTALL)'
)

with open('update_frame5.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("update_frame5.py is prepared for revert")
