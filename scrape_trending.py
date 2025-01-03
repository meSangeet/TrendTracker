from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import json
from pymongo import MongoClient
from datetime import datetime
import uuid

def get_trending_topics():
    # Set up the WebDriver with Service
    service = Service('')
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # # Open Twitter
    driver.get("https://twitter.com/login")
    time.sleep(2)

    # # Log in to Twitter (fill in your credentials)
    username = driver.find_element(By.NAME, "text")
    username.send_keys("")
    username.send_keys(Keys.RETURN)
    time.sleep(2)

    password = driver.find_element(By.NAME, "password")
    password.send_keys("")
    password.send_keys(Keys.RETURN)
    time.sleep(5)

    # Fetch the trending topics
    trends = driver.find_elements(By.XPATH, "//div[@data-testid='trend']")
    top_trends = [trend.text for trend in trends[:5]]

    # Fetch the IP address used by the request (via ProxyMesh or any IP service)
    response = requests.get('https://httpbin.org/ip')
    ip_address = response.json()['origin']

    # Create a unique ID for the session
    unique_id = str(uuid.uuid4())

    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Close the browser
    driver.quit()

    # Prepare the result in JSON format
    result = {
        "unique_id": unique_id,
        "time": current_time,
        "trends": top_trends,
        "ip": ip_address
    }

    return json.dumps(result)

# Execute the function and print the result
if __name__ == "__main__":
    print(get_trending_topics())