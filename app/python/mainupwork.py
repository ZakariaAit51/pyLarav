from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json


userInfo = {}

try:
    def random_delay():
        time.sleep(random.uniform(1, 2))

    options = ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36")
    chrome = Chrome(options=options)
    chrome.get("https://www.upwork.com/ab/account-security/login")

    try:
        email_input = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.ID, "login_username")))
        email_input.send_keys("breezyrahol@gmail.com")
    except:
        print("Email input field not found")

    try:
        login_button = chrome.find_element(By.ID, "login_password_continue")
        login_button.click()
    except:
        print("Login button not found")

    try:
        password_input = WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.ID, "login_password")))
        password_input.send_keys("freelance@55")
    except:
        print("Password input field not found")

    try:
        password_submit_button = chrome.find_element(By.ID, "login_control_continue")
        password_submit_button.click()
    except:
        print("Password submit button not found")

    try:
        user_name_element = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.up-n-link.profile-title")))
        userInfo['name'] = user_name_element.text
        userInfo['profile_link'] = user_name_element.get_attribute("href")
    except:
        print("User name element not found")

    try:
        chrome.get(f"{userInfo['profile_link']}?viewMode=1")
    except:
        print("Failed to navigate to profile link")

    try:
        location_parent_element = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='d-block d-md-inline-block location']")))
        location_child_elements = location_parent_element.find_elements(By.TAG_NAME, "*")[-3:]
        location_concatenated_text = " ".join(child.text for child in location_child_elements)
        userInfo['location'] = location_concatenated_text
    except:
        print("Location element not found")

    try:
        job_title = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[@class='mb-0 pt-lg-2x h4']")))
        userInfo['job_title'] = job_title.text
    except:
        print("Job title element not found")

    try:
        price_element = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[@role='presentation' and @class='d-inline h5 nowrap']")))
        pricePerHour = price_element.find_elements(By.TAG_NAME, "span")[-1]
        userInfo['price'] = pricePerHour.text
    except:
        print("Price element not found")

    try:
        description = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='text-body text-pre-line break']")))
        userInfo['description'] = description.text
    except:
        print("Description element not found")

    try:
        skills_element = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='d-flex list-unstyled flex-wrap-wrap mb-0 air3-token-wrap']")))
        skills_span_elements = skills_element.find_elements(By.XPATH, ".//span[@class='skill-name d-flex vertical-align-middle air3-token nowrap']")
        skills = [span.text.strip() for span in skills_span_elements]
        userInfo['skills'] = skills
    except:
        print("Skills element not found")

    print(json.dumps(userInfo))


except Exception as e:
    print(f"An error occurred: {e}")

finally:
    chrome.quit()
