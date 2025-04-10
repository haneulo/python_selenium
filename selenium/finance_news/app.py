# 네이버 증권 뉴스 크롤링링
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import pandas as pd
from datetime import datetime

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러메시지 노출 방지
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

data = []
for i in range(1, 1000):
    # day = "2025-04-09"
    # 오늘 날짜로 자동 검색
    day = datetime.now().date()
    search_link = f"https://finance.naver.com/news/mainnews.naver?date={day}&page={i}"

    driver.get(search_link)

    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')

    articles = soup.select(".block1")
    for article in articles:
        title = article.select_one(".articleSubject > a").text
        url = 'https://finance.naver.com/' + article.select_one(".articleSubject > a").attrs['href']
        content = article.select_one(".articleSummary").contents[0].strip()
        press = article.select_one(".press").text.strip()
        date = article.select_one(".wdate").text
        print(title, url, content, press, date)
        data.append([title, url, content, press, date])

    # 마지막 페이지 체크
    if soup.select_one(".pgRR") == None:
        break

# 데이터 프레임 생성
df = pd.DataFrame(data, columns=['제목', '링크', '내용', '언론사', '날짜'])
df

# 엑셀 저장
df.to_excel("naver_finance.xlsx")

