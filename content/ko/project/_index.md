---
title: "프로젝트"
subtitle: "진행한 주요 프로젝트를 소개합니다"
type: landing
# ✅ 이 페이지는 /project/ 에 해당함
# 홈과 완전히 분리되어 작동합니다.

sections:
  - block: collection
    content:
      title: ""
      text: " 프로젝트 💡"
      filters:
        folders:
          - project          # ✅ content/project/ 폴더 내의 카드 파일들 자동 불러오기
    design:
      view: list       # ✅ grid
      columns: 4             # ✅ 한 줄에 4개 카드
      gap: 20                # ✅ 카드 간격(px)
      fill_image: true       # ✅ 이미지를 카드 배경으로 채움
      aspect_ratio: 16x9     # ✅ 비율 고정 (세로 불균형 방지)
      background:
        color: "#fff2e0"     # ✅ 페이지 전체 배경색 (당신의 톤에 맞춤)
      spacing:
        padding: [10, 0, 40, 0]  # ✅ 위·아래 여백 살짝만 남기기
---