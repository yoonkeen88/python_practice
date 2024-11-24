from tkinter import *
root = Tk()
root.title("yoonkeen's gui program")
# root.geometry("640x480") # 알파벳 x로 곱하기 표현 
root.geometry("640x480+100+300") # 가로크기 x 세로크기 + x 좌표 + y 좌표
root.resizable(False,False) # x(너비),y(높이) 값 변경 불가 사용자 임의대로 창 크기 변경 불가로함.

root.mainloop() # mainloop 를 통해 창이 닫히지 않게 해줌
