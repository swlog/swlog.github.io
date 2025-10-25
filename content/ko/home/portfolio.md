<!-- ---
# A section created with the Portfolio widget.
# This section displays content from `content/project/`.
# See https://docs.hugoblox.com/widget/portfolio/
widget: portfolio

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 20

title: ''
subtitle: ''

content:
  # Page type to display. E.g. project.
  page_type: projects

  # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
  filter_default: 0

  # Filter toolbar (optional).
  # Add or remove as many filters (`filter_button` instances) as you like.
  # To show all items, set `tag` to "*".
  # To filter by a specific tag, set `tag` to an existing tag name.
  # To remove the toolbar, delete the entire `filter_button` block.
  filter_button:
    - name: All
      tag: '*'
    - name: Machine Learning
      tag: ML
    - name: Computer Vision
      tag: CV
    - name: NLP
      tag: NLP
design:
  columns: '1'
  view: grid
  flip_alt_rows: true
  background: {}
  spacing: {padding: [0, 0, 0, 0]}
--- -->

---
widget: portfolio
headless: true
weight: 20
title: "프로젝트"
subtitle: "제가 만든 프로젝트 모음입니다."

content:
  page_type: projects     # ✅ 폴더명 일치
  filter_button: []       # ✅ 필터 탭 숨기기 (원하면 유지 가능)
  count: 4                # ✅ 홈에서 4개만 보여주기 (선택)
design:
  columns: '2'            # ✅ 가로 2개씩 카드 배치
  view: card              # ✅ 이미지 카드형으로 보기
  flip_alt_rows: false
  spacing: {padding: [0, 0, 0, 0]}
---
