---
widget: portfolio
headless: true
active: true
title: "My Projects"
weight: 40
view: project-card
---

<div class="project-grid">
  {{ range (where site.RegularPages "Type" "project") }}
    {{ partial "custom/project-card.html" . }}
  {{ end }}
</div>

