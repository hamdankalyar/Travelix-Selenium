from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()  


driver.get("https://travelix-final-web.vercel.app/")

tourBtn = driver.find_element_by_xpath("//a[@href='/tour']")
tourBtn.click()

package_name = driver.find_element_by_xpath('//input[@placeholder="Tour Package Name..."]')
package_name.send_keys("Golden Triangle")

city = driver.find_element_by_xpath('//input[@placeholder="City Name..."]')
city.send_keys("Karachi")

min_price = driver.find_element_by_xpath('//input[@placeholder="Min Price"]')
min_price.send_keys("1000")

max_price = driver.find_element_by_xpath('//input[@placeholder="Max Price"]')
max_price.send_keys("3000")

select_category = driver.find_element_by_xpath('//select[@class="car-search-select"]')
select_object = Select(select_category)
select_object.select_by_value("2")


select_category.click()


