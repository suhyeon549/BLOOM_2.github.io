import re

files = ['index.html', 'shop.html', 'team.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Change the inline style
    html = html.replace(
        'background-color: #F8F4E7;',
        'background-color: transparent; transition: background-color 0.4s ease;'
    )

    script = """
<script>
  document.addEventListener("DOMContentLoaded", () => {
    const header = document.querySelector('.site-header');
    if (header) {
      // Check initial scroll position
      if (window.scrollY > 50) {
        header.style.backgroundColor = '#F8F4E7';
      }
      window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
          header.style.backgroundColor = '#F8F4E7';
        } else {
          header.style.backgroundColor = 'transparent';
        }
      });
    }
  });
</script>
</body>"""
    if "header.style.backgroundColor = '#F8F4E7';" not in html:
        html = html.replace('</body>', script)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Added scroll event listener and transparent header.")
