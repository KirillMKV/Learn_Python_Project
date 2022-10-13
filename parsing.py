import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
# from Screenshot import Screenshot
import logging

# logging

logging.basicConfig(filename='selenium_log.log',
                    level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s:%(message)s')

# using stealth https://pypi.org/project/selenium-stealth/

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# parsing
driver = webdriver.Chrome(options=options,
                          executable_path='/home/kirillmkv/PycharmProjects/Learn_Python/BS_test/chromedriver')
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
url = 'https://www.lowes.com/pd/Owens-Corning-Garage-Door-Insulation-Kit-R-8-66-sq-ft-Single-Faced-Fiberglass-Roll-Insulation-with-with-Sound-Barrier-22-in-W-x-4-5-ft-L/1243805'
driver.get(url)
price_dollars = driver.find_element(By.CLASS_NAME, "item-price-dollar").text.replace('$', '').replace(' ', '')
price_cents = driver.find_element(By.CLASS_NAME, 'item-price-cent').text.replace(' ', '')
price = str(price_dollars)+str(price_cents)
print(price_dollars, price_cents)
print(price)
print(type(price))
print(f'Price is {float(price)}')

item_number = driver.find_element(By.NAME, 'Item #')
print(str(item_number))
time.sleep(5)
driver.quit()

# screenshot
# ob = Screenshot.Screenshot()
# img_url = ob.full_Screenshot(driver, save_path=r'.', image_name='Myimage.png')
# print(img_url)

