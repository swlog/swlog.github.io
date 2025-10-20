---
# Homepage
type: widget_page

# Homepage is headless, other widget pages are not.
headless: true

---
title: "Home"
sections:
  - block: about.avatar
    id: about
  - block: hero
    id: slider
    design:
      slider:
        enable: true
        interval: 5000
        loop: true
    slides:
      - background:
          image: "uploads/slide1.jpeg"
      - background:
          image: "uploads/slide2.jpeg"
      - background:
          image: "uploads/slide3.jpeg"
---

---
