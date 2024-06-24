from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html')


html_content = driver.page_source


with open('webpage.html', 'w', encoding='utf-8') as file:
    file.write(html_content)
print("Webpage saved")

driver.quit()


