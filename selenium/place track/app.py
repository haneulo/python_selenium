# 네이버 플레이스 상위 노출 순위 추적 프로그램
import time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# 4. 여러 키워드, 여러 업체의 순위를 찾는 프로그램으로 변경
search_querys = ["서울 피부과", "서울 카페"]
company_ids = ["12771704", "1490432811"]
for company_id, search_query in zip(company_ids, search_querys):
    # 1. 네이버 검색창 + 쿼리로 드라이버 get
    search_link = f"https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query={search_query}"
    driver.get(search_link)

    # 2. place 더보기 탭을 클릭하기 (없다면, 에러)
    try:
        # 펼쳐서 더보기 동작
        open_more_selector = "a.YORrF, a.FtXwJ"
        open_more_element = driver.find_element(By.CSS_SELECTOR, open_more_selector)
        # print(open_more_element.text)
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
        continue

    # 3. 업체의 ID를 기반으로 찾기
    time.sleep(2)
    company_id_selector = f"a[href*='/{company_id}?entry=pll']"

    # 3-2. 없으면, 인피니티 스크롤 5번정도 실행
    for _ in range(5):
        company_elements = driver.find_elements(By.CSS_SELECTOR, company_id_selector)

        if len(company_elements) < 1:
            print("순위권에 업체가 없어서, 스크롤을 합니다")
            scrollY = 20000
            # driver.execute_script("window.scrollBy(0,20000);")
            ActionChains(driver).scroll_by_amount(200,scrollY).perform()
            time.sleep(3)
    if len(company_elements) < 1:
        print("쿼리 검색결과로는 순위가 잡히지않는 업체입니다.")
        continue

    company_element = random.choice(company_elements)
    for _ in range(5):
        target_company_element = company_element.find_element(By.XPATH, './..')
        tagname = target_company_element.get_attribute("tagName")
        if tagname == "LI":
            print("li 태그를 잘 찾았습니다.")
            break
        company_element = target_company_element

    all_list_selector = "#_list_scroll_container > div > div > div.place_business_list_wrapper > ul > li"
    all_list_element = driver.find_elements(By.CSS_SELECTOR, all_list_selector)
    rank = 1
    for each_element in all_list_element:
        try:
            # 광고 element는 순위에서 제외
            each_element.find_element(By.CSS_SELECTOR, "a.gU6bV")
            continue
        except:
            pass
        if each_element == target_company_element:
            break
        rank += 1
    print(f"{search_query} // 현재 {rank} 등에 노출되고 있습니다")

input()