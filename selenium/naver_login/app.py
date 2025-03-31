from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

