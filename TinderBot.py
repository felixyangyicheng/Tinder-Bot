from selenium import webdriver
from time import sleep
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # explicite wait, raise exception when the element are not loaded

from secrets import usernameTinder, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome("C:/Users/y.yicheng/Documents/chromedriver.exe") #path in windows, le path de webdriver (/usr/local/bin/chromdriver.exe)
        self.driver.implicitly_wait(10) # seconds 
    def goTo(self):
        self.driver.get('https://tinder.com')
    
    def login(self):
        try:  

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
                email_in.send_keys(usernameTinder)
            
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
        except Exception:
            
            self.relaunchProcess()
        
    def postLogin(self):
        
        self.autorizeGPS()
        self.activateNotification()


    def autorizeGPS(self):
        result="GPS not autorized"
        if(result=="GPS not autorized"):
            try:
                Autorise_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))
            finally:
                Autorise_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
                Autorise_btn.click()
            result="GPS autorized"
            print(result)
            print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
        else:
            print(result)
            print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
        
        
            
            
    def activateNotification(self):
        result="Notification not activated"
        if(result=="Notification not activated"):               
            try:
                Activate_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')))
            finally:
                Activate_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
                Activate_btn.click()
            result="Notification activated"
            print(result)
            print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
        else:
            print(result)
            print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 

            
    def relaunchProcess(self):
        
        self.driver.quit()
        print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
        print("webDriver quited")
        self.__init__()
        self.goTo()
        self.login()
        print("WebDriver restarted")
        print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
        #sleep(3)
        #print("sleep 3 secondes")
        self.postLogin()
        self.auto_swipe()    
        

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
                        self.close_popupWithResult()
                    except Exception:
                        try:

                            self.close_match()
                        except Exception:
                            print("No more new profil")
                            
                            self.relaunchProcess()
                            
                        finally:
                            self.auto_swipe()
                    finally:
                      
                        self.auto_swipe()
                        

    
        
    def close_popupWithResult(self):
        result="Popup not clicked"
        
        if(result=="Popup not clicked"):
            try:
                popup_3=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
                popup_3.click()
                result="Popup closed"
            except:
                try:
                    popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                    popup_3.click()
                    result="Popup closed"
                finally:
                    print(result)
                    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
            finally:
                print(result)
                print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 

    def close_match(self):
        try:
            match_popup=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')))
        finally:
            match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
            match_popup.click()


def main():
    bot = TinderBot()
    bot.goTo()
    bot.login()
    bot.postLogin()
    bot.auto_swipe()    
if __name__ == "__main__":
    main()
        

