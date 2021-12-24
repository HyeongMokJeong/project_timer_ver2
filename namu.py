from selenium import webdriver
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def namu(m,d):
    
    # 크롬 옵션(헤드리스, 유저 에이전트)
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # 사이트 접속
    url = f"https://namu.wiki/w/{m}%EC%9B%94%20{d}%EC%9D%BC"
    driver.get(url)
    driver.implicitly_wait(time_to_wait=3)

    soup = BeautifulSoup(driver.page_source, "lxml")
    visual1 = soup.find("span", attrs={"id":"가상 인물"}).parent.next_sibling
    visual2 = visual1.find_all("li")
    with open("birth_list.txt", "w", encoding='utf-8') as f:
        for v in visual2:
            v = v.get_text()
            if '(' and ')' in v:
                idx1 = v.index("(")
                idx2 = v.index(")")
                v = v[:idx1] + v[idx2+1:]
            if '[' and ']' in v:
                idx1 = v.index("[")
                idx2 = v.index("]")
                v = v[:idx1] + v[idx2+1:]
            f.write(v + '\n')
    os.startfile("birth_list.txt")
    driver.quit()