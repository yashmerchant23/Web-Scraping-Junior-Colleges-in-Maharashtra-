from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Define the website to scrape and path where the chromedriver is located
website = 'https://www.mahahsscboard.in/list_school_static.php?div_id=IS0wYGAKYAo%3D&inst_type=IzonLUMKYAo%3D'
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

index_No =[]
Junior_College =[]
Address =[]
Pin_code=[]
Mobile_no =[]


# Print the text of each college
for clg in clgs:
    # This assumes that each row contains multiple cells (td) and you want to print the text of each cell
    index_No.append(clg.find_elements("xpath", '//tr/td')[1].text)
    Junior_College.append(clg.find_elements("xpath", '//tr/td')[2].text)
    Address.append(clg.find_elements("xpath", '//tr/td')[4].text)
    Pin_code.append(clg.find_elements("xpath", '//tr/td')[5].text)
    Mobile_no.append(clg.find_elements("xpath", '//tr/td')[6].text)
driver.quit()  
   
df = pd.DataFrame({'COLLEGE_NAME': Junior_College,'ADDRESS':Address,'PIN CODE':Pin_code,'MOBILE':Mobile_no})
df.to_excel('Kolhapur College List.xlsx', index=False)
