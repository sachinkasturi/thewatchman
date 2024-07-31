from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

# Define functions to send messages via Telegram
def telegram_bot_sendques(bot_message):
    bot_token = '7434696374:AAEZohkjyvSYqviFQ7RMcIVVY7gwlpr5iQc'
    bot_chatID = '1121025878'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=MarkdownV2&text=' + str(bot_message).replace('.', '\\.')  # Escape the dot character
    response = requests.get(send_text)
    return response.json()

def telegram_bot_sendtext(bot_message):
    bot_token = '7244741562:AAFMffEdd8Cnigb7j9StokLppAaPw3K-ahM'
    bot_chatID = '1121025878'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=MarkdownV2&text=' + str(bot_message).replace('.', '\\.')  # Escape the dot character
    response = requests.get(send_text)
    return response.json()

telegram_bot_sendtext("Started-1")

# Set up the Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# Open the Chegg website and log in
driver.get("https://expert.chegg.com/auth")
time.sleep(3)

print(driver.find_element(By.XPATH, "/html/body").text)

# Username
element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div/form/div[1]/div[2]/div/div/input')  # Replace with the correct XPath
element.send_keys("kartik89562@proton.me")
element.send_keys(Keys.ENTER)
time.sleep(3)

# Password
passw = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div/form/div[1]/div[2]/div[2]/div/div/input')  # Replace with the correct XPath
passw.send_keys("Kartik@741")
passw.send_keys(Keys.ENTER)
time.sleep(3)

telegram_bot_sendtext("Logged-2")

# Navigate to the authoring page
driver.get("https://expert.chegg.com/qna/authoring/answer")
time.sleep(3)

i = 1
while True:
    try:
        driver.get("https://expert.chegg.com/qna/authoring/answer")
        time.sleep(8)
        message = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[1]')
        text_to_copy = message.text
        if text_to_copy == "Thank you for your efforts on Chegg Q&A! Unfortunately, no Qs are available in your queue at the moment.":
            driver.refresh()
            if i <= 2:
                telegram_bot_sendtext(i)
            if i % 60 == 0:
                status = f"UP Running...  {i/60} AP" #Just a status message to show that the code is running. 
                telegram_bot_sendtext(status)
            i += 1
        else:
            telegram_bot_sendques("Question found in cs account")
            time.sleep(660) # The time frame given to u to choose to acceopt the question and answer it before running the iteration again
    except Exception as e:
        time.sleep(1)
# Quit the WebDriver
driver.quit()
