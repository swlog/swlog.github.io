---
widget: markdown
headless: true
active: true
weight: 1
title: ""
css_class: fullwidth
design:
  spacing:
    padding: [0, 0, 0, 0]
---

<style>
.fullbleed {
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  max-width: 100vw;
  overflow: hidden;
}

#homeCarousel .carousel-item {
  min-height: 100vh;
  background-size: cover;
  background-position: center;
  color: #fff;
  text-align: center;
  position: relative;
}

#homeCarousel .carousel-caption {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -42%);
  width: 90%;
  max-width: 900px;
  text-shadow: 0 2px 12px rgba(0,0,0,.6);
  opacity: 0;
  transition: opacity .5s ease, transform .6s ease;
}
#homeCarousel .carousel-item.active .carousel-caption {
  opacity: 1;
  transform: translate(-50%, -50%);
}

#homeCarousel .carousel-item .carousel-caption h1,
#homeCarousel .carousel-item .carousel-caption p,
#homeCarousel .carousel-item .carousel-caption a {
  opacity: 0;
  transform: translateY(14px);
}
#homeCarousel .carousel-item.active .carousel-caption h1 {
  opacity: 1;
  transform: none;
  transition: all .6s ease .05s;
}
#homeCarousel .carousel-item.active .carousel-caption p {
  opacity: 1;
  transform: none;
  transition: all .6s ease .18s;
}
#homeCarousel .carousel-item.active .carousel-caption a {
  opacity: 1;
  transform: none;
  transition: all .6s ease .3s;
}

#homeCarousel .carousel-indicators [data-bs-target] {
  width: 36px;
  height: 6px;
  border-radius: 999px;
  background: rgba(255,255,255,.45);
  opacity: 1;
  transition: all .3s ease;
}
#homeCarousel .carousel-indicators .active {
  width: 56px;
  background: rgba(255,255,255,.85);
}

@media (max-width: 992px) {
  #homeCarousel .carousel-item {min-height: 60vh;}
  #homeCarousel .carousel-caption h1 {font-size: 2rem;}
}
</style>

<div class="fullbleed">
  <div id="homeCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel" data-bs-interval="5000">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="0" class="active"></button>
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="1"></button>
      <button type="button" data-bs-target="#homeCarousel" data-bs-slide-to="2"></button>
    </div>

    <div class="carousel-inner">
      <!-- 슬라이드 1 -->
      <div class="carousel-item active" style="background-image:linear-gradient(rgba(0,0,0,.4), rgba(0,0,0,.4)), url('/uploads/slide1.jpeg');">
        <div class="carousel-caption">
          <h1 class="display-3 fw-semibold">나의 포트폴리오</h1>
          <p class="lead">프로젝트와 배움을 통해 성장한 흔적을 담았습니다.</p>
          <a class="btn btn-primary btn-lg" href="/about/">소개 보기</a>
        </div>
      </div>

      <!-- 슬라이드 2 -->
      <div class="carousel-item" style="background-image:linear-gradient(rgba(0,0,0,.4), rgba(0,0,0,.4)), url('/uploads/slide2.jpeg');">
        <div class="carousel-caption">
          <h1 class="display-3 fw-semibold">활동 & 취미</h1>
          <p class="lead">즐거움과 휴식이 있는 개발자의 일상</p>
          <a class="btn btn-outline-light btn-lg" href="/post/">기록 보기</a>
        </div>
      </div>

      <!-- 슬라이드 3 -->
      <div class="carousel-item" style="background-image:linear-gradient(rgba(0,0,0,.4), rgba(0,0,0,.4)), url('/uploads/slide3.jpeg');">
        <div class="carousel-caption">
          <h1 class="display-3 fw-semibold">연락하기</h1>
          <p class="lead">협업과 피드백은 언제나 환영합니다.</p>
          <a class="btn btn-primary btn-lg" href="/contact/">Contact</a>
        </div>
      </div>
    </div>

    <button class="carousel-control-prev" type="button" data-bs-target="#homeCarousel" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#homeCarousel" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
    </button>
  </div>
</div>
