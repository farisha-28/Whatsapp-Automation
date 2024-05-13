from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

with open('message.txt', 'r') as file:
    msg = file.read()

# quote encodes the msg
# print(quote(msg));
msg = quote(msg)
numbers = []
with open('number.txt', 'r') as file:
    for num in file.readlines():
        numbers.append(num.rstrip())
print(numbers)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(30)

for n in numbers:

    link2 = f'https://web.whatsapp.com/send/?phone=880{n}&text={msg}'
    driver.get(link2)
    time.sleep(100)
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(5)

time.sleep(2000)