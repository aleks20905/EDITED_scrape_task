from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html')



name = driver.find_element(By.CSS_SELECTOR, 'h1.product-name').text  # Name

price = None # Price

colour = None # colour

sizes = None # sizes

reviews_count =  None # reviews

reviews_score = None # score


product_info = {
    "name": name,
    "price": price,
    "colour": colour,
    "size": sizes,
    "reviews_count": reviews_count,
    "reviews_score": reviews_score
}
print(product_info)

driver.quit()



# mainWraper = driver.find_elements(By.CLASS_NAME, "pdp_call_detail")

# elements = []
# for i in range(len(mainWraper)):
#     elements.append(mainWraper[i].text)

# print(elements)

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


