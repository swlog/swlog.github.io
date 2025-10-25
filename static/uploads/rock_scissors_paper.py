import tkinter as tk
import random

#초기 점수
user_score = 0
comp_score = 0
draw_score = 0 #무승부 점수

def play(uChoice):
        global user_score, comp_score, draw_score
        cChoice = random.choice(["가위", "바위", "보"])
        result_text.set(f"컴퓨터: {cChoice}")
        
        if uChoice == cChoice:
                outcome = "무승부!"
                draw_score += 1
                color = "gray"

        elif (uChoice == "가위" and cChoice == "보") or \
             (uChoice == "바위" and cChoice == "가위") or \
             (uChoice == "보" and cChoice == "바위"):
             outcome = "사용자 승리!"
             user_score += 1
             color = "red"

        else:
            outcome = "컴퓨터 승리!"
            comp_score += 1
            color = "blue"

        score_text.set(f"사용자: {user_score} / 컴퓨터: {comp_score} / 무승부: {draw_score}")
        result_label.config(text=outcome,fg = color)
# GUI 창 생성
win = tk.Tk()
win.title("가위바위보 게임")
win.geometry("300x270")

# 텍스트 변수
result_text = tk.StringVar()
score_text = tk.StringVar(value="사용자: 0 / 컴퓨터: 0 / 무승부: 0")

# 버튼 생성
tk.Label(win, text="가위바위보 중 하나를 선택하세요!", font=("맑은 고딕", 12)).pack(pady=10)
tk.Button(win, text="✌ 가위", width=10, command=lambda: play("가위")).pack(pady=5)
tk.Button(win, text="✊ 바위", width=10, command=lambda: play("바위")).pack(pady=5)
tk.Button(win, text="🖐 보", width=10, command=lambda: play("보")).pack(pady=5)

# 결과 출력
tk.Label(win, textvariable=result_text, font=("맑은 고딕", 11)).pack(pady=5)
tk.Label(win, textvariable=score_text, font=("맑은 고딕", 11)).pack(pady=5)
result_label = tk.Label(win, text="", font=("맑은 고딕", 12, "bold"))
result_label.pack(pady=5)
win.mainloop()