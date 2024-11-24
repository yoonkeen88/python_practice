from tkinter import *

root = Tk()
root.title("listbox")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
# select 은 하나냐 여러개 선택이냐고 
# height 는 몇개까지 보여줄거냐
# height 가 0 이면 전부 보여줌

listbox.insert(0,"사과")
listbox.insert(END,"수박") # 인덱스번호 안넣어주고 그냥 end 라고 해주면
listbox.insert(END,"딸기") # append 처럼 뒤로 들어감
listbox.insert(END,"참외")
listbox.pack()

def btncmd():
    # list 삭제
    # listbox.delete(0)

    # 갯수확인 
    # print(f"list 에는 {listbox.size()}개가 있어요")
    
    # 항목 확인 (시작, 끝)
    # print(f"1~3 element: {listbox.get(0,2)}")

    # 선택항목 확인 curselection 은 위치로 반환 0~END
    print(f"selected element: {listbox.curselection()}")
btn = Button(root, text="Click",command=btncmd)
btn.pack()

root.mainloop()