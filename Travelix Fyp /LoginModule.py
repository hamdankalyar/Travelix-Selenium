from selenium import webdriver



driver = webdriver.Chrome()  


driver.get("https://travelix-final-web.vercel.app/")

loginBtn = driver.find_element_by_xpath("//a[@href='/login']")
loginBtn.click()

email_input = driver.find_element_by_xpath("//input[@id='email']")
email_input.send_keys("hamdan.kalyar@gmail.com")

password_input = driver.find_element_by_xpath("//input[@id='password']")
password_input.send_keys("your_password_here")

SigninBtn = driver.find_element_by_xpath("//button[@type='submit']")
SigninBtn.click()   
