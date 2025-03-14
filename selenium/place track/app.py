# 네이버 플레이스 상위 노출 순위 추적 프로그램
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# 1. 네이버 검색창 + 쿼리로 드라이버 get
search_query = "서울 피부과"
search_link = f"https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query={search_query}"
driver.get(search_link)

# 2. place 더보기 탭을 클릭하기 (없다면, 에러)
try:
    # 펼쳐서 더보기 동작
    open_more_selector = "a.YORrF"
    open_more_element = driver.find_element(By.CSS_SELECTOR, open_more_selector)
    print(open_more_element.text)
    open_more_element.click()
except:
    print(f"{search_query} 키워드로 업체의 플레이스 순위를 알 수 없습니다.")

# 펼쳐서 더보기 동작이 로드될 때까지 대기
time.sleep(1)

try:
    # 검색결과 더보기 동작
    see_more_selector = "a.cf8PL"
    see_more_element = driver.find_element(By.CSS_SELECTOR, see_more_selector)
    print(see_more_element.text)
    see_more_element.click()

except:
    print(f"전체 결과가 검색되어, 추가 검색을 할 수 없습니다.")

# 3. 내가 찾으려는 업체의 ID를 기반으로 찾기


# 3-2. 없으면, 인피니티 스크롤 5번정도 실행

# 4. 여러 키워드, 여러 업체의 순위를 찾는 프로그램으로 변경

input()