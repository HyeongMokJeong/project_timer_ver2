from re import search
from tkinter import *
from PIL.ImageOps import grayscale
from namu import *
from cafe import *
from requests.api import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.filepost import choose_boundary


root = Tk()
root.title("Timer Helper") #이름
root.geometry("250x250+800+350") #크기 (가로x세로 + x좌표 + y좌표)
root.resizable(False, False) #창 크기 변경 불가

# 타이틀 라벨
title_label = Label(root, text='* '*15 + '\n애게타이머 도우미\n' + '* '*15)
title_label.pack()

# 실행 함수
def start_today():
    lnk = link.get()
    namu(month, day)
    cafe(year,month, day, lnk)
    root.quit()

def start_tomm():
    lnk = link.get()
    namu(t_month, t_day)
    cafe(t_year,t_month, t_day, lnk)
    root.quit()

# 엔트리 지우는 함수
def handle_click(event):
    link.delete(0, "end")
    link.unbind("<Button-1>")

# 링크 텍스트 엔트리
link = Entry(root,width=30) #entry는 한줄 입력
link.insert(0, "검색할 키워드를 입력하세요.")
link.pack(padx=15, pady=8)
link.bind("<Button-1>", handle_click)

# 버튼

start_btn_tomm = Button(root, text='내일 GO!', width=7, height=1, command=start_tomm)
start_btn_tomm.pack(pady=5)

start_btn_today = Button(root, text='오늘 GO!', width=7, height=1, command=start_today)
start_btn_today.pack(pady=5)

end_btn = Button(root, text="종료", width=5, height=1, command=root.quit)
end_btn.pack(pady=5)

    

root.mainloop() #루프를 통해 창 닫히지 않게 해줌