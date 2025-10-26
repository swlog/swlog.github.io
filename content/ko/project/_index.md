<!-- ---
title: "프로젝트"
subtitle: "진행한 주요 프로젝트들을 한눈에 보기"
type: landing
image:
  filename: "/uploads/backgroundImg2.jpg"
  focal_point: "Smart"
  preview_only: true
  caption: "프로젝트 포트폴리오 - Python, AI, 알고리즘"
  alt_text: "프로젝트 및 개발 관련 이미지"

sections:
  - block: markdown
    content:
      text: |
        <style>
        .hero-section {
          background-image: url('/uploads/backgroundImg2.jpg');
          background-size: cover;
          background-position: center;
          background-repeat: no-repeat;
          background-attachment: fixed;
          display: flex;
          align-items: center;
          justify-content: center;
          text-align: center;
          color: white;
          position: relative;
        }
        .hero-section::before {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: rgba(0, 0, 0, 0.4);
          z-index: 1;
        }
        .hero-content {
          position: relative;
          z-index: 2;
          max-width: 800px;
          padding: 2rem;
        }
        .hero-title {
          font-size: 3.5rem;
          font-weight: bold;
          margin-bottom: 1rem;
          text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        }
        .hero-subtitle {
          font-size: 1.5rem;
          margin-bottom: 2rem;
          text-shadow: 1px 1px 2px rgba(0,0,0,0.7);
        }
        .hero-cta {
          background: linear-gradient(45deg, #007bff, #0056b3);
          color: white;
          padding: 1rem 2rem;
          border-radius: 50px;
          text-decoration: none;
          font-weight: bold;
          font-size: 1.1rem;
          display: inline-block;
          transition: transform 0.3s ease, box-shadow 0.3s ease;
          box-shadow: 0 4px 15px rgba(0,123,255,0.3);
        }
        .hero-cta:hover {
          transform: translateY(-2px);
          box-shadow: 0 6px 20px rgba(0,123,255,0.4);
          color: white;
          text-decoration: none;
        }
        @media (max-width: 768px) {
          .hero-title {
            font-size: 2.5rem;
          }
          .hero-subtitle {
            font-size: 1.2rem;
          }
        }
        </style>
        
        <div class="hero-section">
          <div class="hero-content">
            <h1 class="hero-title">포트폴리오</h1>
            <p class="hero-subtitle">Python과 AI를 활용한 다양한 프로젝트들을 소개합니다💡</p>
            <a href="#projects" class="hero-cta">
              <i class="fas fa-arrow-down"></i> 프로젝트 보기
            </a>
          </div>
        </div>
    design:
      background:
        color: "transparent"
        text_color_light: true
      spacing:
        padding: ["0", "0", "0", "0"]
  

  # 개별 프로젝트 섹션들 (앵커용)
  - block: markdown
    content:
      title: "가위바위보 게임"
      text: |
        ## 🎮 가위바위보 게임
        
        Python의 tkinter를 활용한 GUI 기반 가위바위보 게임입니다.
        
        **주요 기능:**
        - 사용자와 컴퓨터 간의 가위바위보 게임
        - 직관적인 GUI 인터페이스
        - 게임 결과 통계 및 승률 계산
        
        **기술 스택:** Python, tkinter, GUI 프로그래밍
        
        [자세히 보기 →](/project/01-rps/)
    design:
      background:
        color: "#f8f9fa"
        text_color_light: false
      spacing:
        padding: ["60px", "0", "60px", "0"]
    id: "rps-game"

  - block: markdown
    content:
      title: "영화 리뷰 감성 분석"
      text: |
        ## 🎬 영화 리뷰 감성 분석
        
        자연어 처리를 활용한 영화 리뷰 텍스트의 감성 분석 프로젝트입니다.
        
        **주요 기능:**
        - 영화 리뷰 텍스트 전처리
        - 감성 분석 모델 구축
        - 긍정/부정 감성 분류
        
        **기술 스택:** Python, 자연어처리, 머신러닝, 데이터분석
        
        [자세히 보기 →](/project/02-movie/)
    design:
      background:
        color: "#ffffff"
        text_color_light: false
      spacing:
        padding: ["60px", "0", "60px", "0"]
    id: "movie-review"

  - block: markdown
    content:
      title: "8퍼즐 프로그램"
      text: |
        ## 🧩 8퍼즐 프로그램
        
        탐색 알고리즘을 활용한 8퍼즐 게임 해결 프로그램입니다.
        
        **주요 기능:**
        - A* 알고리즘 구현
        - 휴리스틱 함수 설계
        - 최적 경로 탐색
        
        **기술 스택:** Python, 알고리즘, A* 탐색, 휴리스틱
        
        [자세히 보기 →](/project/03-8-puzzle/)
    design:
      background:
        color: "#f8f9fa"
        text_color_light: false
      spacing:
        padding: ["60px", "0", "60px", "0"]
    id: "eight-puzzle"

  - block: markdown
    content:
      title: "오목 게임 AI"
      text: |
        ## ⚫ 오목 게임 AI
        
        인공지능을 활용한 오목 게임 AI 개발 프로젝트입니다.
        
        **주요 기능:**
        - 미니맥스 알고리즘 구현
        - 게임 트리 탐색
        - AI vs 사용자 대전
        
        **기술 스택:** Python, AI, 미니맥스 알고리즘, 게임 트리
        
        [자세히 보기 →](/project/04-omok/)
    design:
      background:
        color: "#ffffff"
        text_color_light: false
      spacing:
        padding: ["60px", "0", "60px", "0"]
    id: "omok-ai"
---
 -->

<section id="projects" class="project-grid">
  {{ range (where site.RegularPages "Type" "project") }}
    {{ $item := . }}
    {{ $has_attachments := partial "functions/has_attachments" $item }}

    {{ $link := $item.RelPermalink }}
    {{ $target := "" }}
    {{ if $item.Params.external_link }}
      {{ $link = $item.Params.external_link }}
      {{ $target = "target=\"_blank\" rel=\"noopener\"" }}
    {{ end }}

    {{/* Summary */}}
    {{ $summary := "" }}
    {{ if $item.Params.summary }}
      {{ $summary = $item.Params.summary | markdownify | emojify }}
    {{ else if $item.Params.abstract }}
      {{ $summary = $item.Params.abstract | markdownify | emojify }}
    {{ else if $item.Summary }}
      {{ $summary = $item.Summary }}
    {{ end }}

    {{ $resource := partial "blox-core/functions/get_featured_image.html" $item }}

    <div class="card-simple view-card">
      {{ with $resource }}
        {{ $image := .Resize "550x" }}
        {{ if ne $image.MediaType.SubType "gif" }}{{ $image = $image.Process "webp" }}{{ end }}
        <a href="{{ $link }}" {{ $target | safeHTMLAttr }} class="card-image hover-overlay">
          <img src="{{ $image.RelPermalink }}" height="{{ $image.Height }}" width="{{ $image.Width }}" alt="{{ $item.Title }}" class="img-responsive" loading="lazy" style="border-radius:12px;">
        </a>
      {{ end }}

      <div class="card-text">
        <h4 class="card-title mt-3 mb-2">
          <a href="{{ $link }}" {{ $target | safeHTMLAttr }}>{{ $item.Title | markdownify | emojify }}</a>
        </h4>

        {{ with $summary }}
          <p class="card-summary">{{ . }}</p>
        {{ end }}

        {{ if $has_attachments }}
          <div class="btn-links">
            {{ partial "page_links" (dict "page" $item "is_list" 1) }}
          </div>
        {{ end }}
      </div>
    </div>
  {{ end }}
</section>

<style>
.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 25px;
  padding: 40px 0;
}
.card-simple {
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  overflow: hidden;
  transition: transform .25s ease, box-shadow .25s ease;
}
.card-simple:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}
.card-title a {
  color: #222;
  text-decoration: none;
}
.card-title a:hover {
  color: #007bff;
}
.card-summary {
  font-size: 0.95rem;
  color: #555;
}
</style>
