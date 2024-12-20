from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\\Users\\dunga\\Downloads\\chrome-win64\\chromedriver-win64\\chromedriver.exe"

cService = webdriver.ChromeService(executable_path="C:\\Users\\dunga\\Downloads\\chrome-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=cService)

driver.get("https://www.rentacenter.com/en/furniture/living-rooms/c/1001?page=0")

# Find number of pages
ul_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "pagination"))
)
print(ul_element.text)
# Find all li elements within the ul element
li_elements = ul_element.find_elements(By.TAG_NAME, "li")
no_of_pages= int(li_elements[-2].text)
print("Hellopages: ", no_of_pages)



for page in range(no_of_pages):
    driver.get("https://www.rentacenter.com/en/furniture/living-rooms/c/1001?page="+str(page))
    elements = driver.find_elements(By.CLASS_NAME, "list-group-item")

    c=0
    for element in elements:
        print(c)

        desc_text = element.find_element(By.CLASS_NAME, "desc_txt")
        title = desc_text.find_element(By.TAG_NAME, "p").text
        print("title", title)

        if title == "":
            break

        link = element.find_element(By.TAG_NAME, "a")
        href = link.get_attribute('href')
        print("Link:", href)

        link = element.find_element(By.TAG_NAME, "img")
        src = link.get_attribute('src')
        print("SRC", src)



        c+=1
        print()
    print("page", page)
    # Click on the <a> tag



