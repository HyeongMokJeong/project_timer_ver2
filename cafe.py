from selenium import webdriver
from datetime import datetime
import time, pygetwindow, pyperclip, datetime
from selenium import webdriver
from selenium import webdriver
import pyautogui, time, subprocess, chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

global year, month, day, t_year, t_month, t_day, chk


# 시간 설정(오늘)
tm = time.localtime(time.time())
year = tm.tm_year
month = tm.tm_mon
day = tm.tm_mday

# 시간 설정(내일)
tm = time.localtime(time.time()+86400)
t_year = tm.tm_year
t_month = tm.tm_mon
t_day = tm.tm_mday

# 카페 함수
def cafe(y,m,d,key):
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동

    option = Options()
    option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    try:
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    driver.implicitly_wait(10)
    driver.maximize_window()

    # 작성 글 보기 
    url = "https://cafe.naver.com/CafeMemberNetworkView.nhn?m=view&clubid=19543191&memberid=jhm1062&networkSearchKey=Article&networkSearchType=7"
    driver.get(url)
    driver.implicitly_wait(5)

    # # 전날 게시글 클릭
    # img = pyautogui.locateOnScreen("title.png")
    # pyautogui.moveTo(img)
    # pyautogui.click()

    # 양식 불러오기 테스트
    driver.execute_script('window.open("https://cafe.naver.com/ca-fe/cafes/19543191/articles/27690800/modify");')
    time.sleep(3)
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')

    # 새 탭에서 글쓰기 열기
    driver.execute_script('window.open("https://cafe.naver.com/ca-fe/cafes/19543191/menus/217/articles/write?boardType=L");')
    time.sleep(2)
    driver.switch_to_window(driver.window_handles[1])

    # 말머리 및 공개 설정
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/ul/li[2]/button").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div/div[2]/div[2]/div[2]/div[1]/button").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/label").click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/label').click()

    # 제목
    title = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div/div[2]/div[1]/div[1]/div[2]/div/textarea")
    title.click()
    title.send_keys(f"[{m}월 {d}일]")

    # 태그 입력
    tag = driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div/div[2]/div[1]/div[3]/div/div")
    tag.click()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/section/div/div[2]/div[1]/div[3]/div/div/input").send_keys("애게타이머")
    time.sleep(1)

    # 양식 내용 붙여넣기
    img = pyautogui.locateCenterOnScreen("text.png", confidence=0.7)
    pyautogui.click(img)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)

    # 생일 목록 복사
    win = pygetwindow.getWindowsWithTitle('birth_list')[0]
    win.activate()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)

    # 양식에 입력
    img = pyautogui.locateCenterOnScreen("birth.png", confidence=0.7)
    pyautogui.click(img)
    pyautogui.press('end')
    pyautogui.press('down')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)

    # 일차 수정
    pyautogui.press('pageup')
    img = pyautogui.locateCenterOnScreen("ff.png", confidence=0.7)
    pyautogui.click(img)
    pyautogui.press('end')
    pyautogui.press('backspace', 7)
    pyperclip.copy(f"{y}년 {m}월 {d}일]")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('down')
    pyautogui.press('end')
    pyautogui.press('backspace')

    # 오늘 날짜/비교할 날짜 - 게시판
    n = datetime.datetime.now()
    if d == t_day:
        now = n + datetime.timedelta(days=1)
    elif d == day:
        now = n
    date_to_compare = datetime.datetime.strptime("20130710", "%Y%m%d")
    date_diff = now - date_to_compare
    pyperclip.copy(f"{date_diff.days}일")
    pyautogui.hotkey("ctrl", "v")

    # 오늘 날짜/비교할 날짜 - 타이머
    pyautogui.press('down')
    pyautogui.press('backspace')

    n = datetime.datetime.now()
    if d == t_day:
        now = n + datetime.timedelta(days=1)
    elif d == day:
        now = n
    date_to_compare = datetime.datetime.strptime("20131021", "%Y%m%d")
    date_diff = now - date_to_compare
    pyperclip.copy(f"{date_diff.days}일")
    pyautogui.hotkey("ctrl", "v")

    # 미방 이미지 넣기
    pyautogui.press('up', 3)
    pyautogui.press('enter', 3)
    pyautogui.press('up', 3)
    img = pyautogui.locateCenterOnScreen("photo.png", confidence=0.7)
    pyautogui.click(img)
    time.sleep(2)
    img = pyautogui.locateCenterOnScreen("download.png", confidence=0.7)
    pyautogui.click(img)
    time.sleep(1)
    img = pyautogui.locateCenterOnScreen("timerimg.png", confidence=0.7)
    pyautogui.click(img)
    pyautogui.press('enter')
    time.sleep(2)
    img = pyautogui.locateCenterOnScreen("timerimg2.png", confidence=0.7)
    pyautogui.click(img)
    time.sleep(1)
    img = pyautogui.locateCenterOnScreen("middle.png")
    pyautogui.click(img)

    driver.execute_script(f'window.open("https://www.youtube.com/results?search_query={key}");')
    driver.implicitly_wait(5)
    driver.switch_to_window(driver.window_handles[0])

    # 전날 게시글 클릭
    time.sleep(1)
    img = pyautogui.locateCenterOnScreen("title.png", confidence=0.7)
    pyautogui.click(img)
    driver.close()