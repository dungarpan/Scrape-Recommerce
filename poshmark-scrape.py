from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import hashlib
import time
import csv

PATH = "C:\\Users\\dunga\\Downloads\\chrome-win64\\chromedriver-win64\\chromedriver.exe"

cService = webdriver.ChromeService(executable_path="C:\\Users\\dunga\\Downloads\\chrome-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=cService)

driver.get("https://poshmark.com/category/Men-Jackets_&_Coats")
base_url = "https://poshmark.com/category/Men-"


category = ['Jackets_&_Coats', 'Jeans', 'Pants', 'Shirts', 'Shorts', 'Suits_&_Blazers', 'Sweaters', 'Swim','']
Jackets_and_Coats_cat = ['Bomber_&_Varsity', 'Military_&_Field', 'Pea_Coats', 'Performance_Jackets', 'Puffers', 'RainCoats', 'Ski_&_Snowboard', 'Trench_Coats', 'Vests', 'Windbreakers']
Jeans_cat = ['Bootcut','Relaxed','Skinny','Slim','Slim Straight','Straight']
Pants_cat = ['Cargo','Chinos_&_Khakis','Corduroy','Dress','Sweatpants_&_Joggers']
Shirts_cat = ['Casual_Button_Down_Shirts','Dress_Shirts','Jerseys','Polos','Sweatshirts_&_Hoodies','Tank_Tops','Tees___Long_Sleeve','Tees___Short_Sleeve']
Shorts_cat = ['Athletic','Cargo','Flat_Front','Hybrids','Jean_Shorts']
Suits_and_Blazers_cat = ['Sport_Coats_&_Blazers','Suits','Tuxedos','Vests']
Sweaters_cat = ['Cardigan','Crewneck','Turtleneck','V_Neck','Zip_Up']
Swim_cat = ['Board_Shorts','Hybrids','Rash_Guards','Swim_Trunks']
Blank_cat = ['Agbadas_&_Dashikis','Ao_Dais','Changshans','Hanboks','Kaftans','Keffiyehs','Kilts','Kimonos_&_Yukatas','Kurta_Bottoms','Kurtas','Lederhosen','Nehru_Jackets','Ponchos_&_Serapes','Sherwanis']

category_to_list_mapping = {
    'Jackets_&_Coats': Jackets_and_Coats_cat,
    'Jeans': Jeans_cat,
    'Pants': Pants_cat,
    'Shirts': Shirts_cat,
    'Shorts': Shorts_cat,
    'Suits_&_Blazers': Suits_and_Blazers_cat,
    'Sweaters': Sweaters_cat,
    'Swim': Swim_cat,
    '': Blank_cat
}

category_women = ['Dresses','Intimates_&_Sleepwear','Jackets_&_Coats', 'Jeans', 'Pants_&_Jumpsuits', 'Shorts', 'Skirts', 'Sweaters', 'Swim', 'Tops', '']
Dresses_women_cat = ['Asymmetrical', 'Backless', 'High_Low','Long_Sleeve','Maxi','Midi','Mini','One_Shoulder','Prom','Strapless','Wedding']
Intimates_and_Sleepwear_women_cat = ['Bandeaus','Bras','Chemises_&_Slips','Pajamas','Panties','Robes','Shapewear','Sports_Bra']
Jackets_and_Coats_women_cat = ['Blazers_&_Suit_Jackets','Bomber_Jackets','Capes','Jean_Jackets','Leather_Jackets','Pea_Coats','Puffers','Ski_&_Snow_Jackets','Teddy_Jackets','Trench_Coats','Utility_Jackets','Varsity_Jackets','Vests']
Jeans_women_cat = ['Ankle_&_Cropped','Boot_Cut','Boyfriend','Flare_&_Wide_Leg','High_Rise','Jeggings','Overalls','Skinny','Straight_Leg']
Pants_and_Jumpsuits_women_cat = ['Ankle_&_Cropped','Boot_Cut_&_Flare','Capris','Jumpsuits_&_Rompers','Leggings','Pantsuits','Skinny','Staright_Leg','Track_Pants_&_Joggers','Trousers','Wide_Leg']
Shorts_women_cat = ['Athletic_Shorts','Bermudas','Bike_Shorts','Cargos','High_Waist','Jean_Shorts','Skorts']
Skirts_women_cat = ['A_Line_or_Full','Asymmetrical','Circle_&_Skater','High_Low','Maxi','Midi','Mini','Pencil']
Sweaters_women_cat = ['Cardigan','Cowl_&_Turtlenecks','Crew_&_Scoop_Necks','Off_the_Shoulder_Sweaters','Shrugs_&_Ponchos','V_Necks']
Swim_women_cat = ['Bikinis', 'Coverups', 'One_Pieces', 'Sarongs']
Tops_women_cat = ['Blouses','Bodysuits','Button_Down_Shirts','Camisoles','Crop_Tops','Jerseys','Muscle_Tees','Sweatshirts_&_Hoodies','Tank_Tops','Tees___Long_Sleeve','Tees___Short_Sleeve','Tunics']
Blank_women_cat = ['Ao_Dais','Cheongsams_&_Qipaos','Dirndls','Dupattas_&_Stoles','Hanboks','Harem_Pants','Hijabs','Huipils','Kaftans','Kimonos_&_Yukatas','Kurta_Bottoms','Kurtas','Lehengas','Palazzo_Pants','Patiala_Pants','Salwars','Saree_Blouses','Sarees','Treggings']

women_category_to_list_mapping = {
    'Dresses': Dresses_women_cat,
    'Intimates_&_Sleepwear': Intimates_and_Sleepwear_women_cat,
    'Jackets_&_Coats': Jackets_and_Coats_women_cat,
    'Jeans': Jeans_women_cat,
    'Pants_&_Jumpsuits': Pants_and_Jumpsuits_women_cat,
    'Shorts': Shorts_women_cat,
    'Skirts': Skirts_women_cat,
    'Sweaters': Sweaters_women_cat,
    'Swim': Swim_cat,
    'Tops': Tops_women_cat,
    '': Blank_women_cat
}

c=0
with open('Clothing_Data_new.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for cat in category:
        cat_url = base_url + cat
        for sub_cat in category_to_list_mapping[cat]:
            try:
                url = cat_url + "-" + sub_cat
                driver.get(url)

                # Scroll down to load more content
                last_height = driver.execute_script("return document.body.scrollHeight")
                
                scroll_count = 0
                while True:
                    driver.execute_script("window.scrollBy(0, 500);")
                    time.sleep(1)  # Wait for new content to load
                    driver.execute_script("return document.body.scrollHeight")
                    scroll_count += 1
                    if scroll_count>=10:
                        break

                cloth_card = driver.find_elements(By.CLASS_NAME, "card")
                print(url)
            except:
                print("url not available")
            for i in cloth_card:
                try:

                    c+=1

                    title = i.find_element(By.CLASS_NAME, "title__condition__container").find_element(By.TAG_NAME, "a").text
                    #print(title)

                    prod_url = i.find_element(By.TAG_NAME, "a").get_attribute('href')
                    #print(prod_url)

                    img_url = i.find_element(By.TAG_NAME, "img").get_attribute('src')
                    #print(img_url)

                    price = i.find_element(By.CLASS_NAME, "p--t--1").text
                    #print(price)x

                    size = i.find_elements(By.CLASS_NAME, "m--t--1")[-1].find_element(By.TAG_NAME, "a").text
                    if size.startswith("Size:"):
                        size = size[6:]
                    #print(size)

                    item_id = int(hashlib.md5(prod_url.encode('utf-8')).hexdigest(), 16)
                    #print(item_id)

                    writer.writerow([item_id, title, prod_url, img_url, price, size])

                except:
                    print("Some issue with this")



                #print(c)
        print("---------------------")

base_url = "https://poshmark.com/category/Women-"

with open('Clothing_Data_new.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for cat in category_women:
        cat_url = base_url + cat
        for sub_cat in women_category_to_list_mapping[cat]:
            try:
                url = cat_url + "-" + sub_cat
                driver.get(url)

                # Scroll down to load more content
                last_height = driver.execute_script("return document.body.scrollHeight")
                
                scroll_count = 0
                while True:
                    driver.execute_script("window.scrollBy(0, 500);")
                    time.sleep(1)  # Wait for new content to load
                    driver.execute_script("return document.body.scrollHeight")
                    scroll_count += 1
                    if scroll_count>=10:
                        break

                cloth_card = driver.find_elements(By.CLASS_NAME, "card")
                print(url)
            except:
                print("url not available")
            for i in cloth_card:
                try:

                    c+=1

                    title = i.find_element(By.CLASS_NAME, "title__condition__container").find_element(By.TAG_NAME, "a").text
                    #print(title)

                    prod_url = i.find_element(By.TAG_NAME, "a").get_attribute('href')
                    #print(prod_url)

                    img_url = i.find_element(By.TAG_NAME, "img").get_attribute('src')
                    #print(img_url)

                    price = i.find_element(By.CLASS_NAME, "p--t--1").text
                    #print(price)

                    size = i.find_elements(By.CLASS_NAME, "m--t--1")[-1].find_element(By.TAG_NAME, "a").text
                    if size.startswith("Size:"):
                        size = size[6:]
                    #print(size)

                    item_id = int(hashlib.md5(prod_url.encode('utf-8')).hexdigest(), 16)
                    #print(item_id)

                    writer.writerow([item_id, title, prod_url, img_url, price, size])

                except:
                    print("Some issue with this")



                #print(c)
        print("---------------------")