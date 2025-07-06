import undetected_chromedriver as uc
import requests
import pickle
import time
from datetime import datetime

# Set up headless, stealthy Chrome options
options = uc.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--window-size=1920,1080")  # Optional but helps evade bot detection

# Launch undetected Chrome
print("Starting headless browser...")
driver = uc.Chrome(options=options)

# Step 1: Load Instagram base page
driver.get("https://www.instagram.com/")
time.sleep(3)

# Step 2: Load saved cookies
with open("insta_cookies.pkl", "rb") as f:
    cookies = pickle.load(f)

for cookie in cookies:
    # Required by Instagram
    if "sameSite" in cookie:
        del cookie["sameSite"]
    driver.add_cookie(cookie)

# Step 3: Go to the DMs page
print("Navigating to DMs page...")
driver.get("https://www.instagram.com/direct/inbox/")
time.sleep(5)

print("Current title:", driver.title)

# Discord webhook setup
discordWebhook = "<replace-this-with-your-discord-server's-webhook>"
message = {
    "content": "💌 they texted u bruh — " + datetime.now().strftime("%b %d %Y, %I:%M%p")
}

current_title = driver.title
empty_title = "Inbox • Chats"  # baseline tab title when idle

# Step 4: Monitor title changes to detect new DMs
try:
    print("👀 Monitoring for new DMs...")
    notified = False  # Flag to avoid repeated alerts
    while True:
        new_title = driver.title
        print("Current tab title:", new_title)

        # When title shows a new message (e.g., "(1) Inbox • Chats")
        if new_title.startswith("(") and not notified:
            print("🔔 New DM detected!")
            requests.post(discordWebhook, json={
                "content": "💌 they texted u bruh — " + datetime.now().strftime("%b %d %Y, %I:%M%p")
            })
            notified = True  # Prevent multiple alerts for same DM

        # When title returns to normal (inbox viewed), reset flag
        if not new_title.startswith("("):
            notified = False

        time.sleep(60)  # Check every minute
except KeyboardInterrupt:
    print("⛔ Monitoring stopped by user.")
finally:
    driver.quit()
    print("🔒 Browser closed.")