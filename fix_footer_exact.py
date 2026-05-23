with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('<!-- Footer -->')
idx_end = html.find('</div>\n  </div>\n</body>')

if idx != -1 and idx_end != -1:
    index_footer = html[idx:idx_end+6]
    print(index_footer.count('<div'), index_footer.count('</div'))
    with open('footer.html', 'w', encoding='utf-8') as f2:
        f2.write(index_footer)
