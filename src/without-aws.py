from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from datetime import datetime
import time

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Start code:
driver = webdriver.Chrome(options=options)

# You now control the manually opened Chrome window
# driver.get("https://www.instagram.com/")
print("original title: ", driver.title)

discordWebhook = "<replce-this-with-your-discord-servrer's-webhook>"

message = {
    "content": "💌 they texted u bruh — " + datetime.now().strftime("%b %d %Y, %I:%M%p")
}

current_title = driver.title
empty_title = "Inbox • Chats"

try:
    while True:
        if ((driver.title != current_title) and (driver.title != empty_title)):
            # debugging
            print("current tab title: ", driver.title)
            requests.post(discordWebhook, json=message)
            current_title = driver.title
        time.sleep(60) #1 minute
except KeyboardInterrupt:
    print("Stopped by user.")