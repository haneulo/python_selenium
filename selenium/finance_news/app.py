# 네이버 증권 뉴스 크롤링링
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러메시지 노출 방지
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

search_date = "2025-04-01"
search_link = f"https://finance.naver.com/news/mainnews.naver?date={search_date}"

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

