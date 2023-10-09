#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


driver.get('https://www.archdaily.com/')


search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search ArchDaily']")
search_box.send_keys('London')
search_box.send_keys(Keys.RETURN)


time.sleep(5)


images = driver.find_elements(By.CSS_SELECTOR, 'img')


os.makedirs('archdaily_images', exist_ok=True)


for i, image in enumerate(images):
    image_url = image.get_attribute('src')
    if image_url and image_url.startswith('https://'):
        image_filename = f'archdaily_images/image_{i}.jpg'
        response = requests.get(image_url)
        with open(image_filename, 'wb') as f:
            f.write(response.content)
            print(f'Downloaded {image_url} to {image_filename}')


driver.quit()

