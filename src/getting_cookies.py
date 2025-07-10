import undetected_chromedriver as uc
import pickle
import time

# Set up Chrome options
options = uc.ChromeOptions()

# Run in full (non-headless) mode to allow manual login
# You can enable user profile reuse to keep sessions longer
# options.user_data_dir = "selenium-profile"

# Initialize undetected Chrome driver
driver = uc.Chrome(options=options)

# Navigate to Instagram login page
print("Opening Instagram login page...")
driver.get("https://www.instagram.com/")

# Give the user time to manually log in
input("\nLog in manually in the browser window.\nOnce you're fully logged in, press Enter here to save cookies...")

# Optional wait to ensure session is stable
time.sleep(3)

# Save cookies to file
cookies = driver.get_cookies()
with open("insta_cookies.pkl", "wb") as f:
    pickle.dump(cookies, f)

print(f"Saved {len(cookies)} cookies to insta_cookies.pkl")

driver.quit()
print("Chrome session closed.")