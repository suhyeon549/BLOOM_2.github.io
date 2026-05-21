def px_to_vw(px):
    vw = px * 0.078125
    if vw == 0: return '0vw'
    return f'{vw:.4f}'.rstrip('0').rstrip('.') + 'vw'

def css_block(selector, props):
    lines = []
    for k, v in props.items():
        if isinstance(v, (int, float)):
            lines.append(f"{k}: {px_to_vw(v)};")
        else:
            lines.append(f"{k}: {v};")
    return f"{selector} {{\n  " + "\n  ".join(lines) + "\n}\n"

css_rules = [
    css_block('.team-container', {'height': 3381}),
    css_block('.team-hero-bg', {'width': 1280, 'height': 777, 'left': 0, 'top': 0, 'z-index': 1, 'overflow': 'hidden'}),
    css_block('.team-hero-bg img', {'width': '100%', 'height': '100%', 'object-fit': 'cover'}),
    css_block('.team-hero-title', {'left': '50%', 'top': 418, 'z-index': 10, 'font-size': 36, 'font-weight': 600, 'letter-spacing': '-0.0781vw', 'transform': 'translateX(-50%)', 'white-space': 'nowrap'}),
    css_block('.team-hero-desc', {'left': '50%', 'top': 490, 'z-index': 10, 'font-size': 18, 'font-weight': 500, 'transform': 'translateX(-50%)', 'white-space': 'nowrap'}),
    css_block('.team-bg-strip-1', {'width': 1280, 'height': 248, 'left': 0, 'top': 778, 'background': 'white', 'z-index': 2}),
    css_block('.team-bg-strip-2', {'width': 1280, 'height': 271, 'left': 0, 'top': 2273, 'background': 'white', 'z-index': 2}),
    css_block('.team-bg-half-left', {'width': 1280, 'height': 623, 'left': 0, 'top': 1027, 'background': '#f8f4e7', 'z-index': 2}),
    css_block('.team-bg-half-right', {'width': 1280, 'height': 623, 'left': 0, 'top': 1650, 'background': '#f8f4e7', 'z-index': 2}),
    css_block('.team-line-horiz-1', {'width': 1280, 'height': 1, 'left': 0, 'top': 777, 'z-index': 9999}),
    css_block('.team-line-horiz-2', {'width': 1280, 'height': 1, 'left': 0, 'top': 1026, 'z-index': 9999}),
    css_block('.team-line-horiz-3', {'width': 1280, 'height': 1, 'left': 0, 'top': 2273, 'z-index': 9999}),
    css_block('.team-line-horiz-4', {'width': 1280, 'height': 1, 'left': 0, 'top': 2544, 'z-index': 9999}),
    css_block('.team-vert-left', {'width': 0, 'height': 1247, 'left': 40, 'top': 1026, 'z-index': 9999, 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    css_block('.team-vert-right', {'width': 0, 'height': 1247, 'left': 1240, 'top': 1026, 'z-index': 9999, 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    css_block('.team-vert-inner', {'position': 'relative', 'width': 1247, 'height': 1}),
    css_block('.team-title-1', {'left': 40, 'top': 837, 'font-family': "'Montserrat', sans-serif", 'font-size': 70, 'font-weight': 500, 'letter-spacing': '-0.0781vw', 'text-transform': 'uppercase', 'z-index': 10}),
    css_block('.team-title-1 p', {'line-height': 70}),
    css_block('.team-title-2', {'left': 40, 'top': 2305, 'font-family': "'Montserrat', sans-serif", 'font-size': 70, 'font-weight': 500, 'letter-spacing': '-0.0781vw', 'text-transform': 'uppercase', 'z-index': 10}),
    css_block('.team-title-2 p', {'line-height': 70}),
    css_block('.team-title-desc', {'left': 640, 'top': 837, 'font-size': 18, 'z-index': 10}),
    css_block('.team-person1-img', {'width': 640, 'height': 623, 'left': 0, 'top': 1027, 'z-index': 5}),
    css_block('.team-person1-img img', {'width': '100%', 'height': '100%', 'object-fit': 'cover'}),
    css_block('.team-person1-floral', {'width': 427, 'height': 544, 'left': 853, 'top': 1106, 'z-index': 3, 'opacity': '0.3'}),
    css_block('.team-person1-floral img', {'width': '100%', 'height': '100%', 'object-fit': 'cover'}),
    css_block('.team-person1-role', {'left': 685, 'top': 1241, 'font-family': "'Montserrat', sans-serif", 'font-size': 24, 'font-weight': 600, 'z-index': 10, 'letter-spacing': '-0.1562vw'}),
    css_block('.team-person1-role p', {'line-height': 25}),
    css_block('.team-person1-name', {'left': 685, 'top': 1303, 'font-size': 24, 'font-weight': 500, 'z-index': 10}),
    css_block('.team-person1-desc', {'left': 685, 'top': 1338, 'font-size': 12, 'z-index': 10}),
    css_block('.team-person1-desc p', {'line-height': 18}),
    css_block('.team-person2-img', {'width': 640, 'height': 623, 'left': 640, 'top': 1650, 'z-index': 5}),
    css_block('.team-person2-img img', {'width': '100%', 'height': '100%', 'object-fit': 'cover'}),
    css_block('.team-person2-floral', {'width': 397, 'height': 444, 'left': 0, 'top': 1829, 'z-index': 3, 'opacity': '0.3'}),
    css_block('.team-person2-floral img', {'width': '100%', 'height': '100%', 'object-fit': 'cover'}),
    css_block('.team-person2-role', {'left': 595, 'top': 1864, 'font-family': "'Montserrat', sans-serif", 'font-size': 24, 'font-weight': 600, 'z-index': 10, 'letter-spacing': '-0.1562vw', 'text-align': 'right', 'transform': 'translateX(-100%)'}),
    css_block('.team-person2-role p', {'line-height': 25}),
    css_block('.team-person2-name', {'left': 595, 'top': 1926, 'font-size': 24, 'font-weight': 500, 'z-index': 10, 'text-align': 'right', 'transform': 'translateX(-100%)'}),
    css_block('.team-person2-desc', {'left': 595, 'top': 1961, 'font-size': 12, 'z-index': 10, 'text-align': 'right', 'transform': 'translateX(-100%)'}),
    css_block('.team-person2-desc p', {'line-height': 18}),
    css_block('.team-promise-text', {'left': '50%', 'top': 2486, 'font-size': 14, 'z-index': 10, 'text-align': 'center', 'transform': 'translateX(-50%)'}),
    css_block('.team-bottom-img', {'width': 1280, 'height': 660, 'left': 0, 'top': 2544, 'z-index': 5}),
    css_block('.team-bottom-img img', {'width': '100%', 'height': '100%', 'object-fit': 'cover'}),
    css_block('.team-footer-wrap', {'top': 3204})
]

with open('style.css', 'a', encoding='utf-8') as f:
    f.write('\n\n/* TEAM PAGE SPECIFIC */\n')
    f.write('\n'.join(css_rules))

print('CSS written to style.css')
