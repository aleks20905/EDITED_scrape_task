from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html')


mainWraper = driver.find_elements(By.CLASS_NAME, "pdp_call_detail")

elements = []
for i in range(len(mainWraper)):
    elements.append(mainWraper[i].text)

print(elements)


driver.quit()

# ['29 Reviews\n
# BGN 115.00\n
# COLOUR:\n
# Blue Mix\n
# SIZE\
# nSize chart\n
# Select Size\n
# S-Regular Out of Stock\n
# M-Regular\nL-Regular\n
# XL-Regular\n
# 2XL-Regular Out of Stock\n
# 3XL-Regular\n
# 4XL-Regular Out of Stock\n
# 5XL-Regular Out of Stock\n
# Notify me when back in stock\n
# Add to bag\n
# Save item for later\n
# Free Express delivery over 200 BGN']


