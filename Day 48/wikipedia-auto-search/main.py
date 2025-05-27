from selenium import webdriver
from selenium.webdriver.common.by import By
#This package is needed to use non-character keyboard keys
from selenium.webdriver.common.keys import Keys


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#If window not maximized, search bar is hidden and causes faiure
driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

#---HOW TO CLICK A LINK---#
# total_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount ul li:nth-of-type(2) a")
# print(total_articles.text)
# total_articles.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python (programming language)" + Keys.ENTER)

# Had to add this to above, otherwise not functional?
#search.send_keys(Keys.ENTER)


# driver.quit()