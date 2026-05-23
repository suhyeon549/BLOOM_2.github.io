with open(r'C:\Users\yeons\.gemini\antigravity\brain\a0de5db8-fcea-4037-b511-d410ef8bf03d\.system_generated\steps\736\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    if 'data-node-id="124:605"' in line:
        for j in range(max(0, i-50), min(len(lines), i+1)):
            print(f'{j}: {lines[j]}')
        break
