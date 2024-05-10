from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# Set up the WebDriver

# Set Chrome options
options = Options()

# # Specify the path to your Chrome user profile
# options.add_argument("user-data-dir=/Users/hamdan/Library/Application Support/Google/Chrome/")
# options.add_argument("profile-directory=Profile 1")
# # Specify a custom user agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

# Set up the WebDriver with the modified options
driver = webdriver.Chrome(options=options)


# Open the initial webpage
driver.get("https://travelix-final-web.vercel.app/")

loginBtn = driver.find_element_by_xpath("//a[@href='/login']")
loginBtn.click()


forgetBtn = driver.find_element_by_xpath("//a[@href='/forget']")
forgetBtn.click()


email_input = driver.find_element_by_xpath("//input[@id='email']")
email_input.send_keys("hamdan.kalyar@gmail.com")

resetBtn = driver.find_element_by_xpath("//button[@type='submit']")
resetBtn.click()   

code = driver.find_element_by_xpath("//input[@id='code']")
code.send_keys("123456")

password_input = driver.find_element_by_xpath("//input[@id='password']")
password_input.send_keys("password12345")

confirm_password = driver.find_element_by_xpath("//input[@id='confirmPassword']")
confirm_password.send_keys("password12345")

resetBtn = driver.find_element_by_xpath("//button[@type='submit']")
resetBtn.click()
