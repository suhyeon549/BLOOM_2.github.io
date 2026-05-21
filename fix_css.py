def v(px): return f"{px * 0.078125:.4f}".rstrip('0').rstrip('.') + 'vw'

css = """
/* TEAM PAGE SPECIFIC */
.team-container { height: """ + v(3381) + """; }
.team-hero-bg { width: 100vw; height: """ + v(777) + """; left: 0; top: 0; z-index: 1; overflow: hidden; }
.team-hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.team-hero-title { left: 50%; top: """ + v(418) + """; z-index: 10; font-size: """ + v(36) + """; font-weight: 600; letter-spacing: -0.0781vw; transform: translateX(-50%); white-space: nowrap; color: #2b201f; }
.team-hero-desc { left: 50%; top: """ + v(490) + """; z-index: 10; font-size: """ + v(18) + """; font-weight: 500; transform: translateX(-50%); white-space: nowrap; color: #2b201f; }
.team-bg-strip-1 { width: 100vw; height: """ + v(248) + """; left: 0; top: """ + v(778) + """; background: white; z-index: 2; }
.team-bg-strip-2 { width: 100vw; height: """ + v(271) + """; left: 0; top: """ + v(2273) + """; background: white; z-index: 2; }
.team-bg-half-left { width: 100vw; height: """ + v(623) + """; left: 0; top: """ + v(1027) + """; background: #f8f4e7; z-index: 2; }
.team-bg-half-right { width: 100vw; height: """ + v(623) + """; left: 0; top: """ + v(1650) + """; background: #f8f4e7; z-index: 2; }
.team-line-horiz-1 { width: 100vw; height: """ + v(1) + """; left: 0; top: """ + v(777) + """; z-index: 9999; }
.team-line-horiz-2 { width: 100vw; height: """ + v(1) + """; left: 0; top: """ + v(1026) + """; z-index: 9999; }
.team-line-horiz-3 { width: 100vw; height: """ + v(1) + """; left: 0; top: """ + v(2273) + """; z-index: 9999; }
.team-line-horiz-4 { width: 100vw; height: """ + v(1) + """; left: 0; top: """ + v(2544) + """; z-index: 9999; }
.team-vert-left { width: 0; height: """ + v(1247) + """; left: """ + v(40) + """; top: """ + v(1026) + """; z-index: 9999; display: flex; align-items: center; justify-content: center; }
.team-vert-right { width: 0; height: """ + v(1247) + """; left: """ + v(1240) + """; top: """ + v(1026) + """; z-index: 9999; display: flex; align-items: center; justify-content: center; }
.team-vert-inner { position: relative; width: """ + v(1247) + """; height: """ + v(1) + """; }
.team-title-1 { left: """ + v(40) + """; top: """ + v(837) + """; font-family: 'Montserrat', sans-serif; font-size: """ + v(70) + """; font-weight: 500; text-transform: uppercase; z-index: 10; line-height: """ + v(70) + """; color: #2b201f; }
.team-title-2 { left: """ + v(40) + """; top: """ + v(2305) + """; font-family: 'Montserrat', sans-serif; font-size: """ + v(70) + """; font-weight: 500; text-transform: uppercase; z-index: 10; line-height: """ + v(70) + """; color: #2b201f; }
.team-title-desc { left: """ + v(640) + """; top: """ + v(837) + """; font-size: """ + v(18) + """; z-index: 10; line-height: """ + v(28) + """; color: #2b201f; }
.team-person1-img { width: """ + v(640) + """; height: """ + v(623) + """; left: 0; top: """ + v(1027) + """; z-index: 5; }
.team-person1-img img { width: 100%; height: 100%; object-fit: cover; }
.team-person1-floral { width: """ + v(427) + """; height: """ + v(544) + """; left: """ + v(853) + """; top: """ + v(1106) + """; z-index: 3; opacity: 0.3; pointer-events: none; }
.team-person1-floral img { width: 100%; height: 100%; object-fit: cover; }
.team-person1-role { left: """ + v(685) + """; top: """ + v(1241) + """; font-family: 'Montserrat', sans-serif; font-size: """ + v(24) + """; font-weight: 600; z-index: 10; letter-spacing: -0.0781vw; line-height: """ + v(30) + """; color: #2b201f; }
.team-person1-name { left: """ + v(685) + """; top: """ + v(1303) + """; font-size: """ + v(24) + """; font-weight: 500; z-index: 10; line-height: """ + v(32) + """; color: #2b201f; }
.team-person1-desc { left: """ + v(685) + """; top: """ + v(1338) + """; font-size: """ + v(12) + """; z-index: 10; line-height: """ + v(18) + """; color: #2b201f; }
.team-person2-img { width: """ + v(640) + """; height: """ + v(623) + """; left: """ + v(640) + """; top: """ + v(1650) + """; z-index: 5; }
.team-person2-img img { width: 100%; height: 100%; object-fit: cover; }
.team-person2-floral { width: """ + v(397) + """; height: """ + v(444) + """; left: 0; top: """ + v(1829) + """; z-index: 3; opacity: 0.3; pointer-events: none; }
.team-person2-floral img { width: 100%; height: 100%; object-fit: cover; }
.team-person2-role { left: """ + v(595) + """; top: """ + v(1864) + """; font-family: 'Montserrat', sans-serif; font-size: """ + v(24) + """; font-weight: 600; z-index: 10; letter-spacing: -0.0781vw; text-align: right; transform: translateX(-100%); line-height: """ + v(30) + """; color: #2b201f; }
.team-person2-name { left: """ + v(595) + """; top: """ + v(1926) + """; font-size: """ + v(24) + """; font-weight: 500; z-index: 10; text-align: right; transform: translateX(-100%); line-height: """ + v(32) + """; color: #2b201f; }
.team-person2-desc { left: """ + v(595) + """; top: """ + v(1961) + """; font-size: """ + v(12) + """; z-index: 10; text-align: right; transform: translateX(-100%); line-height: """ + v(18) + """; color: #2b201f; }
.team-promise-text { left: 50%; top: """ + v(2486) + """; font-size: """ + v(14) + """; z-index: 10; text-align: left; transform: translateX(-50%); line-height: """ + v(22) + """; color: #2b201f; }
.team-bottom-img { width: 100vw; height: """ + v(660) + """; left: 0; top: """ + v(2544) + """; z-index: 5; }
.team-bottom-img img { width: 100%; height: 100%; object-fit: cover; }
.team-footer-wrap { top: """ + v(3204) + """; }
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css)
print("Done")
