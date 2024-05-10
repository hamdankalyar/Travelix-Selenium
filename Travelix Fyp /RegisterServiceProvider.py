from selenium import webdriver

driver = webdriver.Chrome() 


driver.get("https://travelix-final-web.vercel.app/")

loginBtn = driver.find_element_by_xpath("//a[@href='/login']")
loginBtn.click()

registerBtn = driver.find_element_by_xpath("//a[@href='/register']")
registerBtn.click()

registerServiceProvider = driver.find_element_by_xpath("//button[@type='button']")
registerServiceProvider.click()

name = driver.find_element_by_xpath("//input[@id='name']")
name.send_keys("Hamdan Kalyar")


email_input = driver.find_element_by_xpath("//input[@id='email']")
email_input.send_keys("hamdan.kalyar@gmail.com")

phone = driver.find_element_by_xpath("//input[@id='phone']")
phone.send_keys("03111111111")

password_input = driver.find_element_by_xpath("//input[@id='password']")
password_input.send_keys("khanjjjj")  

file_path = "/Users/hamdan/Desktop/testing.png"

file = driver.find_element_by_xpath("//input[@id='file']")
file.send_keys(file_path)

street_address = driver.find_element_by_xpath("//input[@name='address']")
street_address.send_keys("Street 1")

account_number = driver.find_element_by_xpath("//input[@name='accountNumber']")
account_number.send_keys("1234567891011")
account_name = driver.find_element_by_xpath("//input[@name='accountName']")
account_name.send_keys("Hamdan234Kalyar")

bank_name = driver.find_element_by_xpath("//input[@name='bankName']")
bank_name.send_keys("HBL")

file = driver.find_element_by_xpath("//input[@id='file2']")
file.send_keys(file_path)
SigninBtn = driver.find_element_by_xpath("//button[@type='submit']")
SigninBtn.click()   
