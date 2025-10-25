---
widget: blank
headless: true
active: true
title: "My Projects"
weight: 40
---

<div class="project-grid">
  {{ range (where site.RegularPages "Type" "project") }}
    {{ partial "custom/project-card.html" . }}
  {{ end }}
</div>


