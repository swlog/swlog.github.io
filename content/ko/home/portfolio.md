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

  filter_button:            # ✅ 필터 탭 3개만
    - name: All
      tag: '*'
    - name: Python
      tag: Python
    - name: AI
      tag: AI

design:
  columns: '1'              # ✅ 가로 2개 카드
  view: grid                # ✅ 카드형 (이미지 표시)
  flip_alt_rows: false
  spacing: {padding: [0, 0, 0, 0]}
---