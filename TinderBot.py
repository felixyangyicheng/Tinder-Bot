from selenium import webdriver
from time import sleep
#import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # explicite wait, raise exception when the element are not loaded

from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome("C:/Users/y.yicheng/Documents/chromedriver.exe") #path in windows, le path de webdriver
        self.driver.implicitly_wait(10) # seconds 

    def login(self):
        self.driver.get('https://tinder.com')

        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')))
        finally:
            connexion_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
            connexion_btn.click()
        
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')))
        finally:
            accept_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
            accept_btn.click()
        
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')))
        finally:
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
            fb_btn.click()
        
        sleep(3)
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        

        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
        finally:

            email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
            email_in.send_keys(username)
        
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]')))
        finally:
            pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
            pass_in.send_keys(password)
        
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="u_0_0"]')))
        finally:
            
            login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
            login_btn.click()
        

        self.driver.switch_to_window(base_window)

        

        try:
            Autorise_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))
        finally:
            Autorise_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            Autorise_btn.click()
            def auto_swipe(self):
                while True:
                    sleep(0.5)
                    
                    self.like()
                    
        try:
            Activate_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))
        finally:
            Activate_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            Activate_btn.click()

            
        
        #pyautogui.click(294, 227, clicks = 1, duration = 3)
        #pyautogui.click(310, 252, clicks = 1, duration = 1)

    def like(self):
        

        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                
                try:
                    self.dislike()
                except Exception:
                
                    try:
                        self.close_popup()
                    except Exception:
                        self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        try:
            match_popup=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')))
        finally:
            match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
            match_popup.click()

        


bot = TinderBot()
bot.login()
bot.auto_swipe()