css_to_add = """
/* =========================================
   Scroll Animations & Interactions
   ========================================= */

.reveal {
  opacity: 0;
  transition: opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1), translate 0.8s cubic-bezier(0.25, 1, 0.5, 1), scale 0.8s cubic-bezier(0.25, 1, 0.5, 1);
  will-change: opacity, translate, scale;
}

.reveal.active {
  opacity: 1;
}

/* Slide Up */
.reveal-up {
  translate: 0 40px;
}
.reveal-up.active {
  translate: 0 0;
}

/* Subtle Scale In */
.reveal-scale {
  scale: 0.95;
}
.reveal-scale.active {
  scale: 1;
}

/* Sequential Delays */
.delay-100 { transition-delay: 100ms; }
.delay-200 { transition-delay: 200ms; }
.delay-300 { transition-delay: 300ms; }
.delay-400 { transition-delay: 400ms; }

/* =========================================
   Hover Effects
   ========================================= */

/* Hover Lift (Cards, Features) */
.hover-lift {
  transition: translate 0.4s ease, box-shadow 0.4s ease;
}
.hover-lift:hover {
  translate: 0 -5px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.08);
}

/* Custom image wrappers that overflow hidden should be careful with hover-scale so image scales inside */
.img-zoom-wrap {
  overflow: hidden;
}
.img-zoom-wrap img {
  transition: scale 0.8s ease;
}
.img-zoom-wrap:hover img {
  scale: 1.05;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_to_add)
print("CSS animations added.")
