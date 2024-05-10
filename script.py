

from selenium import webdriver
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # Update the path if necessary

# Open the initial webpage
driver.get("https://www.adamchoi.co.uk")

# Wait for elements to load
time.sleep(5)

# Find the first row and last column that contains the link
tbody = driver.find_element_by_tag_name('tbody')
first_row = tbody.find_elements_by_tag_name('tr')[0]
last_column = first_row.find_elements_by_tag_name('td')[-1]

# Click the link in the last column of the first row
last_column.click()

# Wait for the new tab to open
time.sleep(5)

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Now find the table on the new tab
table = driver.find_element_by_css_selector('.tableinpanel')

# Get all rows in the table
rows = table.find_elements_by_tag_name('tr')

# Iterate over each row and get the columns
for row in rows:
    cols = row.find_elements_by_tag_name('td')
    col_data = [col.text for col in cols]
    print(col_data)

# Close the new tab and switch back to the original tab if necessary
driver.close()
driver.switch_to.window(driver.window_handles[0])

# Continue with other operations on the original tab if needed
