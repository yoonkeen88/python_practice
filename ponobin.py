import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.font_manager as fm

# 폰트 설정 (Windows용 경로 예시)
font_path = "C:/Windows/Fonts/malgun.ttf"
if font_path and fm.os.path.exists(font_path):
    fontprop = fm.FontProperties(fname=font_path)
    plt.rc('font', family=fontprop.get_name())

# 확률 계산 및 그래프 표시 함수
def calculate_and_plot(dist_type, entries):
    try:
        if dist_type == "정규분포":
            score = float(entries['score'].get())
            mean = float(entries['mean'].get())
            sd = float(entries['sd'].get())
            z = (score - mean) / sd
            qutle = 1 - norm.cdf(z)

            plt.figure(figsize=(8, 6))
            x = np.arange(-5, 5, 0.01)
            y = norm.pdf(x)
            plt.plot(x, y, label="Normal Distribution")
            plt.fill_between(x, y, where=(x >= z), color="skyblue", alpha=0.5, label=f"P(X ≥ {z:.3f}) = {qutle:.3f}")
            plt.title("정규분포")
            plt.xlabel("표준화 점수")
            plt.ylabel("확률 밀도")
            plt.legend()
            plt.show()

        elif dist_type == "이항분포":
            trials = int(entries['trials'].get())
            prob = float(entries['prob'].get())
            x = int(entries['x'].get())
            binom_pmf = binom.pmf(x, trials, prob)

            plt.figure(figsize=(8, 6))
            x_values = np.arange(0, trials + 1)
            y_values = binom.pmf(x_values, trials, prob)
            plt.bar(x_values, y_values, color="skyblue")
            plt.title("이항분포")
            plt.xlabel("성공 횟수")
            plt.ylabel("확률")
            plt.text(x, binom_pmf, f"P(X={x}) = {binom_pmf:.3f}", color="red")
            plt.show()

        elif dist_type == "포아송분포":
            lamb = float(entries['lambda'].get())
            x = int(entries['x'].get())
            poisson_pmf = poisson.pmf(x, lamb)

            plt.figure(figsize=(8, 6))
            x_values = np.arange(0, x + 10)
            y_values = poisson.pmf(x_values, lamb)
            plt.bar(x_values, y_values, color="skyblue")
            plt.title("포아송분포")
            plt.xlabel("성공 횟수")
            plt.ylabel("확률")
            plt.text(x, poisson_pmf, f"P(X={x}) = {poisson_pmf:.3f}", color="red")
            plt.show()

    except ValueError:
        messagebox.showerror("입력 오류", "올바른 숫자 값을 입력하세요.")

# 분포에 따른 입력 창 생성
def open_input_window(dist_type):
    input_window = tk.Toplevel(root)
    input_window.title(f"{dist_type} 입력")

    entries = {}
    if dist_type == "정규분포":
        tk.Label(input_window, text="점수:").grid(row=0, column=0, padx=5, pady=5)
        entries['score'] = tk.Entry(input_window)
        entries['score'].grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_window, text="평균:").grid(row=1, column=0, padx=5, pady=5)
        entries['mean'] = tk.Entry(input_window)
        entries['mean'].grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_window, text="표준편차:").grid(row=2, column=0, padx=5, pady=5)
        entries['sd'] = tk.Entry(input_window)
        entries['sd'].grid(row=2, column=1, padx=5, pady=5)

    elif dist_type == "이항분포":
        tk.Label(input_window, text="시행 횟수 (n):").grid(row=0, column=0, padx=5, pady=5)
        entries['trials'] = tk.Entry(input_window)
        entries['trials'].grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_window, text="성공 확률 (p):").grid(row=1, column=0, padx=5, pady=5)
        entries['prob'] = tk.Entry(input_window)
        entries['prob'].grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_window, text="성공 횟수 (x):").grid(row=2, column=0, padx=5, pady=5)
        entries['x'] = tk.Entry(input_window)
        entries['x'].grid(row=2, column=1, padx=5, pady=5)

    elif dist_type == "포아송분포":
        tk.Label(input_window, text="람다 (λ):").grid(row=0, column=0, padx=5, pady=5)
        entries['lambda'] = tk.Entry(input_window)
        entries['lambda'].grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_window, text="성공 횟수 (x):").grid(row=1, column=0, padx=5, pady=5)
        entries['x'] = tk.Entry(input_window)
        entries['x'].grid(row=1, column=1, padx=5, pady=5)

    tk.Button(input_window, text="계산하기", command=lambda: calculate_and_plot(dist_type, entries)).grid(row=3, column=0, columnspan=2, pady=20)

# 초기 분포 선택 창
root = tk.Tk()
root.title("확률 계산기")

tk.Label(root, text="분포 선택:").pack(padx=10, pady=10)
combo_dist = ttk.Combobox(root, values=["정규분포", "이항분포", "포아송분포"])
combo_dist.pack(padx=10, pady=10)
combo_dist.current(0)

tk.Button(root, text="확인", command=lambda: open_input_window(combo_dist.get())).pack(pady=20)

root.mainloop()
