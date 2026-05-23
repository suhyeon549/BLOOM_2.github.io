with open(r'C:\Users\yeons\.gemini\antigravity\brain\a0de5db8-fcea-4037-b511-d410ef8bf03d\.system_generated\steps\736\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('data-node-id="124:605"')
print(text[max(0, idx-100):min(len(text), idx+1500)])
