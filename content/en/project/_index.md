---
title: "Projects"
subtitle: "An overview of major projects at a glance"
type: landing
image:
  filename: "/uploads/backgroundImg2.jpg"
  focal_point: "Smart"
  preview_only: true
  caption: "Project Portfolio - Python, AI, Algorithms"
  alt_text: "Project and development-related image"

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
            <h1 class="hero-title">Portfolio</h1>
            <p class="hero-subtitle">Introducing various projects utilizing Python and AI 💡</p>
            <a href="#projects" class="hero-cta">
              <i class="fas fa-arrow-down"></i> View Projects
            </a>
          </div>
        </div>
    design:
      background:
        color: "transparent"
        text_color_light: true
      spacing:
        padding: ["0", "0", "0", "0"]
  

  # Individual project sections (for anchors)
  - block: markdown
    content:
      title: "Rock-Paper-Scissors Game"
      text: |
        ## 🎮 Rock-Paper-Scissors Game
        
        A GUI-based rock-paper-scissors game built with Python’s tkinter.
        
        **Key Features:**
        - Rock-paper-scissors gameplay between user and computer  
        - Intuitive GUI interface  
        - Game statistics and win rate tracking  
        
        **Tech Stack:** Python, tkinter, GUI Programming
        
        [Learn More →](/project/01-rps/)
    design:
      background:
        color: "#f8f9fa"
        text_color_light: false
      spacing:
        padding: ["60px", "0", "60px", "0"]
    id: "rps-game"

  - block: markdown
    content:
      title: "Movie Review Sentiment Analysis"
      text: |
        ## 🎬 Movie Review Sentiment Analysis
        
        A sentiment analysis project for movie reviews using Natural Language Processing (NLP).
        
        **Key Features:**
        - Preprocessing of movie review text  
        - Sentiment classification model construction  
        - Positive/Negative sentiment categorization  
        
        **Tech Stack:** Python, NLP, Machine Learning, Data Analysis
        
        [Learn More →](/project/02-movie/)
    design:
      background:
        color: "#ffffff"
        text_color_light: false
      spacing:
        padding: ["60px", "0", "60px", "0"]
    id: "movie-review"

  - block: markdown
    content:
      title: "8-Puzzle Program"
      text: |
        ## 🧩 8-Puzzle Program
        
        A puzzle-solving program that utilizes search algorithms.
        
        **Key Features:**
        - Implementation of the A* algorithm  
        - Design of heuristic functions  
        - Optimal path search  
        
        **Tech Stack:** Python, Algorithms, A* Search, Heuristics
        
        [Learn More →](/project/03-8-puzzle/)
    design:
      background:
        color: "#f8f9fa"
        text_color_light: false
      spacing:
        padding: ["60px", "0", "60px", "0"]
    id: "eight-puzzle"

  - block: markdown
    content:
      title: "Gomoku Game AI"
      text: |
        ## ⚫ Gomoku Game AI
        
        A Gomoku (Five-in-a-Row) game AI project using artificial intelligence.
        
        **Key Features:**
        - Implementation of the Minimax algorithm  
        - Game tree search  
        - AI vs Player mode  
        
        **Tech Stack:** Python, AI, Minimax Algorithm, Game Tree
        
        [Learn More →](/project/04-omok/)
    design:
      background:
        color: "#ffffff"
        text_color_light: false
      spacing:
        padding: ["60px", "0", "60px", "0"]
    id: "omok-ai"
---
