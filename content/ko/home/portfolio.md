---
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
  page_type: project

  # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
  filter_default: 0

  # Filter toolbar (optional).
  # Add or remove as many filters (`filter_button` instances) as you like.
  # To show all items, set `tag` to "*".
  # To filter by a specific tag, set `tag` to an existing tag name.
  # To remove the toolbar, delete the entire `filter_button` block.
  filter_button:
    - name: 모두
      tag: '*'
    - name: 파이썬
      tag: PYTHON
    - name: 인공지능
      tag: AI
   
design:
  view: card
  columns: 3                # ✅ 3열 카드
  fill_image: true
  aspect_ratio: 16x9
  show_summary: true
  show_date: false
  show_read_more: false
  card_style: shadow        # ✅ 그림자 효과
  spacing:
    padding: [10, 10, 10, 10]
---
