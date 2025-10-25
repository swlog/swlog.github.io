---
title: 8퍼즐 프로그램
summary: 파이썬으로 구현한 상태공간 탐색 기반 8퍼즐 프로그램
date: 2025-05-10
type: project
tags:
  - AI
image:
  filename: "puzzle.jpg"
  focal_point: "center"
  preview_only: false
---

## <i class="fab fa-python"></i> 프로젝트 개요

이 프로젝트는 **탐색 알고리즘을 이해하기 위한 Python 프로젝트**로,  
**상태공간 탐색(state-space search)** 개념을 적용한 프로그램입니다.  

8개의 숫자 타일을 한 칸씩 이동시켜 목표 상태를 만드는 고전 퍼즐 문제로,  
처음에는 단순한 배열 이동으로 시작했지만,  
점차 **BFS(너비 우선 탐색)**, **DFS(깊이 우선 탐색)**, **휴리스틱 기반 탐색(A\*)** 개념을 접목하며  
알고리즘의 중요성과 효율성을 체감할 수 있었습니다.  

---

## <i class="fab fa-steam-symbol"></i> 주요 기능

- 8퍼즐 문제의 초기 상태 및 목표 상태 정의  
- 노드 확장 및 자식 상태 생성 로직 구현  
- BFS / DFS 기반 퍼즐 탐색 알고리즘 구현  
- 불가능한 경우(해결 불가능한 상태) 판별 기능  
- 탐색 과정 및 이동 횟수 출력  

---

## <i class="fab fa-dropbox"></i> 코드 다운로드
</> [eightpuzzle.zip 다운로드](/uploads/eightpuzzle.zip)
