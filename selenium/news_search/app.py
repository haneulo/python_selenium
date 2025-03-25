# 네이버 뉴스 기사 크롤링
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

search_query = "속보"
search_link = f"https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={search_query}"

driver.get(search_link)

time.sleep(1)

# 최신순으로 보기
Latest_selector = "#snb > div.mod_group_option_filter._search_option_simple_wrap > div > div.option_area.type_sort > a:nth-child(2)"
Latest_element = driver.find_element(By.CSS_SELECTOR, Latest_selector)
Latest_element.click()

time.sleep(1)

# 스크롤 동작(스크롤 1번당 10개의 뉴스 추가)
for _ in range(2):
    driver.execute_script("window.scrollBy(0,10000);")
    time.sleep(1)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

# 뉴스 타이틀, url, 언론사 출력
articles = soup.select('.news_wrap')

for article in articles:
    title = article.select_one('.news_tit').text
    url = article.select_one('.news_tit')['href']
    news = article.select_one('.info_group > a').text.split(' ')[0].replace('언론사','')
    print(title, url, news)

input()
