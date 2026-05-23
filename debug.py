with open(r'C:\Users\yeons\.gemini\antigravity\brain\a0de5db8-fcea-4037-b511-d410ef8bf03d\.system_generated\steps\577\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('data-node-id="124:497"')
print(text[max(0, idx-500):min(len(text), idx+1000)])
