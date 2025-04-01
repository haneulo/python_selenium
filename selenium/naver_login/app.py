from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러메시지 노출 방지
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

# 이동하려는 해당 웹페이지 주소
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

# 아이디 입력창 선택
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()

# 아이디 입력
id.send_keys("네이버 id")

time.sleep(2)

# 비밀번호 입력창 선택
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()

# 비밀번호 입력
pw.send_keys("네이버 pw")

time.sleep(2)

# 로그인 버튼 선택
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
login_btn.click()



