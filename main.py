from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Define the website to scrape and path where the chromedriver is located
website = 'https://www.mahahsscboard.in/list_school_static.php?div_id=ISwwYGAKYAo%3D&inst_type=IzonLUMKYAo%3D'
service = Service(executable_path="chromedriver.exe")  # Write the path here

# Correcting the options usage
chroptions = webdriver.ChromeOptions()
chroptions.add_experimental_option("detach", True)
chroptions.add_experimental_option('excludeSwitches', ['enable-logging'])
chroptions.add_argument('--log-level=3')

# Create the Chrome driver with the configured options
driver = webdriver.Chrome(service=service, options=chroptions)

# Open Google Chrome with chromedriver
driver.get(website)


# Find all rows (colleges) in the table
# clgs = driver.find_elements("xpath", '//td[@align="left"]')
clgs = driver.find_elements(By.CLASS_NAME, 'tr')

data =[]
# Print the text of each college
for clg in clgs:
    # This assumes that each row contains multiple cells (td) and you want to print the text of each cell
    # data.append(clg.text)
    data.append(clg.text)



# Create a DataFrame from the data list
df = pd.DataFrame(data, columns=['Colleges'])

# Save the DataFrame to an Excel file
df.to_excel('Pune College List.xlsx', index=False)

# Close the browser window
driver.quit()