---
# Homepage
type: widget_page

# Homepage is headless, other widget pages are not.
headless: true

# Define widget order
widgets:
  - name: portfolio
    weight: 10
    active: true
    headless: true
    title: "Projects"
    subtitle: "Various projects utilizing Python and AI"
    design:
      view: compact
      columns: 1
      gap: 20
      background:
        color: "#ffffff"
        text_color_light: false
      card:
        background: "#ffffff"
        border: true
        border_color: "#e8e8e8"
        border_radius: 16
        text_color: "#2c3e50"
        hover: true
        hover_effect: "lift"
        padding: 0
        shadow: true
        shadow_color: "rgba(0,0,0,0.1)"
        shadow_offset: "0 4px 12px"
        transition: "all 0.3s ease"
---
