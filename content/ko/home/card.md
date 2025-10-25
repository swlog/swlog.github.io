---
widget: blank
headless: true
active: true
title: "프로젝트 모음"
weight: 40
---

<div class="project-grid">
  {{ range (where site.RegularPages "Type" "project") }}
    {{ partial "views/project-card.html" . }}
  {{ end }}
</div>

<style>
.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}
</style>
