import os
from dotenv import load_dotenv
from selenium import webdriver

# load environment variables
load_dotenv()

# get username and password from environment
username = os.getenv("USERNAME")
pwd = os.getenv("PASSWORD")

driver = webdriver.Firefox("/usr/local/bin/")

driver.get("https://instagram.com")