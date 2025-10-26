---
title: 오목 게임 AI
summary: 파이썬 기반의 Alpha-Beta 탐색과 휴리스틱 평가 함수를 적용한 오목 인공지능
date: 2025-05-20
type: project
tags:
  - AI
image:
  filename: "omok.jpg"
  focal_point: "center"
  preview_only: false
---



## <i class="fab fa-python"></i> 프로젝트 개요

이 프로젝트는 **AI 탐색 알고리즘을 적용한 오목 게임 인공지능**으로,  
기본적인 규칙 기반 플레이어를 넘어서 **휴리스틱 평가 + Alpha-Beta 가지치기**를 통해  
효율적인 수읽기 기능을 구현한 프로젝트입니다.  

AI가 스스로 돌을 두는 로직을 직접 설계하면서,  
단순한 조건문이 아닌 **탐색 깊이·평가 함수·가지치기** 개념을 실제 코드에 적용했습니다.  

---

## <i class="fab fa-steam-symbol"></i> 주요 기능

- **후보수 생성 (Candidate Moves)** : 주변 돌 반경을 기반으로 효율적인 착수 후보 계산  
- **평가 함수 (Evaluation Function)** : 돌의 개수, 열린 끝(Open Ends), 연속 패턴 등을 점수화  
- **Alpha-Beta 가지치기 탐색** : 불필요한 탐색을 줄여 연산 효율 극대화  
- **즉시 승리·방어 수 탐지** : AI가 다음 한 수로 승리/패배를 판단해 방어 수행  
- **탐색 깊이 조절 (MAX_DEPTH)** : 상황에 따라 탐색 깊이를 유연하게 조절  

---

## <i class="fab fa-dropbox"></i> 코드 다운로드
</> [user_agent.py 다운로드](/uploads/user_agent.py)

---