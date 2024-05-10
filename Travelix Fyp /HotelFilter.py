from selenium import webdriver

driver = webdriver.Chrome()  


driver.get("https://travelix-final-web.vercel.app/")

tourBtn = driver.find_element_by_xpath("//a[@href='/hotel']")
tourBtn.click()

package_name = driver.find_element_by_xpath('//input[@placeholder="Hotel Name..."]')
package_name.send_keys("Grand")

city = driver.find_element_by_xpath('//input[@placeholder="City Name..."]')
city.send_keys("Lahore")

min_price = driver.find_element_by_xpath('//input[@placeholder="Min Price"]')
min_price.send_keys("10000")

max_price = driver.find_element_by_xpath('//input[@placeholder="Max Price"]')
max_price.send_keys("20000")







