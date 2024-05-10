from selenium import webdriver



driver = webdriver.Chrome() 


driver.get("https://travelix-final-web.vercel.app/")

loginBtn = driver.find_element_by_xpath("//a[@href='/login']")
loginBtn.click()

registerBtn = driver.find_element_by_xpath("//a[@href='/register']")
registerBtn.click()

name = driver.find_element_by_xpath("//input[@id='name1']")
name.send_keys("Jahanzaib Iqbal")


email_input = driver.find_element_by_xpath("//input[@id='email']")
email_input.send_keys("jazbi.khan@gmail.com")

phone = driver.find_element_by_xpath("//input[@id='phone']")
phone.send_keys("03111111111")

password_input = driver.find_element_by_xpath("//input[@id='password']")
password_input.send_keys("khanjjjj")  

confirm_password = driver.find_element_by_xpath("//input[@id='confirm-password']")
confirm_password.send_keys("khanjjjj")

SigninBtn = driver.find_element_by_xpath("//button[@type='submit']")
SigninBtn.click()   
