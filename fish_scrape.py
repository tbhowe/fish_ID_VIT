#%%

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import time

class GetImages:

    def __init__(self, chromedriver_path: str, opts=None): 
        self.keyword=keyword
        self.suffix=' fish'
        self.chromedriver_path='/Users/rrritalin/miniconda3/envs/zoopla/bin/chromedriver'
        # self.chromedriver_path=chromedriver_path
        self.base_url='https://images.google.com/'
        self.download_path='images/'
        self.driver =webdriver.Chrome(self.chromedriver_path)

    def get_search_page(self):
        '''Method to open the search page on google images '''
        self.driver.get('https://images.google.com/')
        self.driver.maximize_window()

    def accept_cookies(self):
        '''Method to accept the GFPR cookies on google images page '''
        delay = 2
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]')))
            print("cookiebox Ready!")
            try:
                accept_cookies_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]') 
                WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]'))) 
                self.driver.execute_script("arguments[0].click();", accept_cookies_button)
                time.sleep(1)

            except NoSuchElementException:
                print("cookie button not present")
            
        except TimeoutException:
            print("No GDPR cookie box appeared!")
        
    def enter_search(self):
        '''method to enter search term into image search box'''
        search_box=self.driver.find_element(by=By.XPATH, 
                                            value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search_box.send_keys(self.keyword + self.suffix)
        search_box.send_keys(Keys.ENTER)
    
    def get_images(self, keyword: str, limit: int):
        '''method to get top n images from keyword, where n is the value passed in limit argument'''
        if os.path.exists(self.download_path + self.keyword +'/' )==False:
            os.makedirs(self.download_path + self.keyword +'/' )
        
        for image_number in range(1, limit+1):
            try:
                img = self.driver.find_element(By.XPATH, value=
                                            '//*[@id="islrg"]/div[1]/div[' +
                                            str(image_number) + ']/a[1]/div[1]/img')  
                time.sleep(0.1) 

                img.screenshot( self.download_path + 
                                self.keyword + '/img_' + str(image_number) + '.png')

                time.sleep(0.2)
            except:
                continue

    def close_driver(self):
        '''method for closing the driver'''
        self.driver.close()

    def scroll_to_bottom(self):
        '''method to get more images by scrolling to bottom and clicking button'''
        pass
                                        
'pike, perch, zander, chub, barbel, pollack, plaice, mackerel, gurnard, scad'


if __name__ == "__main__":
    fish_types=['pike','perch','zander','carp','chub','barbel','mackerel','gurnard','scad','ballan']
    limit=200
    for fish in fish_types:
        fish_images=GetImages( chromedriver_path='/Users/rrritalin/miniconda3/envs/zoopla/bin/chromedriver')
        keyword=fish_types(fish)
        fish_images.get_search_page()
        fish_images.accept_cookies()
        fish_images.enter_search()
        fish_images.get_images(keyword,limit)
        fish_images.close_driver()

# %%
