import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # matplotlib 백엔드를 TkAgg로 설정
import matplotlib.pyplot as plt
from scipy.stats import norm
import tkinter as tk
from tkinter import messagebox

def calculate_and_plot():
    try:
        # 사용자 입력 받기
        score = float(entry_score.get())
        mean = float(entry_mean.get())
        sd = float(entry_sd.get())
        n = int(entry_n.get())
        
        # Z 점수와 분위수 계산
        z = (score - mean) / sd
        qutle = 1 - norm.cdf(z)
        rank = qutle * n
        
        # 새 figure 생성
        plt.figure(figsize=(8, 6))
        
        # x 범위 설정
        x = np.arange(-5, 5, 0.01)
        y = norm.pdf(x)
        
        # 그래프 그리기
        plt.clf()  # 이전 그래프 지우기
        plt.plot(x, y, label="Normal Distribution")
        plt.fill_between(x, y, where=(x >= z), color="skyblue", alpha=0.5, 
                        label=f"P(X ≥ {z:.3f}) = {qutle:.3f}")
        plt.title("정규분포")
        plt.xlabel("표준화 점수")
        plt.ylabel("확률 밀도")
        
        # 분위수 텍스트 추가
        plt.text(z, norm.pdf(z) / 2, 
                f"Z점수: {z:.3f}\n확률: {qutle:.3%}\n예상등수: {rank:.0f}", 
                color="red", fontsize=10)
        
        # z 값 선 그리기
        plt.axvline(x=z, color="blue", linestyle="--", label=f"Z점수: {z:.3f}")
        
        # 범례 표시
        plt.legend()
        
        # 그래프 표시
        plt.show()
        
    except ValueError:
        messagebox.showerror("입력 오류", "올바른 숫자 값을 입력하세요.")

# GUI 설정
root = tk.Tk()
root.title("정규분포 계산기")

# 창 크기 설정과 중앙 배치
window_width = 300
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# GUI 요소 배치
tk.Label(root, text="점수:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="평균:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="표준편차:").grid(row=2, column=0, padx=5, pady=5)
tk.Label(root, text="전체 인원:").grid(row=3, column=0, padx=5, pady=5)

entry_score = tk.Entry(root)
entry_mean = tk.Entry(root)
entry_sd = tk.Entry(root)
entry_n = tk.Entry(root)

entry_score.grid(row=0, column=1, padx=5, pady=5)
entry_mean.grid(row=1, column=1, padx=5, pady=5)
entry_sd.grid(row=2, column=1, padx=5, pady=5)
entry_n.grid(row=3, column=1, padx=5, pady=5)

tk.Button(root, text="계산하기", command=calculate_and_plot).grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()