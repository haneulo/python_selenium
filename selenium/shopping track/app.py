# 네이버 스마트스토어 상품 순위 추적 프로그램
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

search_query = ["꿀사과"]
target_prod_code = ["81372721469"]

for search_query, target_prod_code in zip(search_query, target_prod_code):
    real_rank = -1
    rank = -1
    for pageindex in range(1, 15):
        # 1. url로 1페이지 방문
        shopping_link = f"https://search.shopping.naver.com/search/all?adQuery=%EA%BF%80%EC%82%AC%EA%B3%BC&frm=NVSCTAB&origQuery=%EA%BF%80%EC%82%AC%EA%B3%BC&pagingIndex={pageindex}&pagingSize=40&productSet=total&query={search_query}&sort=rel&timestamp=&viewType=list"
        driver.get(shopping_link)
        time.sleep(3)

        # 2. 페이지를 4번 밑으로 내리기 (상품 더 불러오기)
        for _ in range(4):
            driver.execute_script("window.scrollBy(0,10000);")
            time.sleep(0.5) # 데이터 로딩 대기 0.5초

        # 3. 타켓 상품이 페이지에 노출되고 있는지 확인하기
        # 4. 없다면 -> url로 next page 방문
        try:
            target_prod_selector = f"a[data-i='{target_prod_code}']"
            target_prod_element = driver.find_element(By.CSS_SELECTOR, target_prod_selector)
            rank = target_prod_element.get_attribute('data-shp-contents-rank')
            real_rank = (int(pageindex) - 1) * 44 + int(real_rank)
            break
        except:
            print(f"{pageindex} 페이지에서 타겟 상품을 찾지 못했습니다.")
            # next page 방문 해야 함.

    # 광고 상품은 rank 셀렉터가 없어 순위에서 제외됨
    print("내 상품의 진짜 등수는", real_rank, "등입니다")
    print(f"내 상품은 {pageindex} 페이지의 {rank}등에 노출되고 있습니다")
input()