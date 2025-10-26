---
# Homepage
type: widget_page

# Homepage is headless, other widget pages are not.
headless: true

# 위젯 순서 정의
widgets:
  - name: portfolio
    weight: 10
    active: true
    headless: true
    title: "프로젝트"
    subtitle: "Python과 AI를 활용한 다양한 프로젝트들"
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
