from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time

CHROME_DRIVER_PATH = "C:/Utvikling/chromedriver.exe"


class Search:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.password = "Password123"
        self.f_name = "Ola"
        self.l_name = "Nordmann"
        self.paramount = None
        self.netflix = None
        self.youtube = None
        self.spotify = None
        self.viaplay = None
        self.disney = None
        self.amazon = None
        self.apple = None
        self.dplay = None
        self.hulu = None
        self.hbo = None
        self.tv2 = None

    def check_amazon(self, email):
        self.driver.get('https://www.amazon.com/gp/video/signup')
        self.driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys(email)
        self.driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        try:
            self.driver.find_element(By.XPATH, '//*[@id="auth-error-message-box"]')
            self.amazon = False
        except NoSuchElementException:
            self.amazon = True
        print(self.amazon)

    def check_netflix(self, email):
        self.driver.get('https://www.netflix.com/no/login')
        self.driver.find_element(By.XPATH, '//*[@id="id_userLoginId"]').send_keys(email)
        self.driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div[3]/div/div/d'
                                           'iv[1]/form/button').click()
        time.sleep(2)
        try:
            text = self.driver.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/div/div[2]').text
            if text == "Beklager, vi finner ingen konto tilknyttet denne e-postadressen. Prøv på nytt eller opprett en ny konto.":
                self.netflix = False
        except NoSuchElementException:
            self.netflix = True
        print(self.netflix)

    def check_viaplay(self, email):
        self.driver.get('https://checkout.viaplay.no/register/1234')
        try:
            self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
            self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        except NoSuchElementException:
            pass
        self.driver.find_element(By.XPATH, '//*[@id="RegisterForm_email"]').send_keys(email)
        self.driver.find_element(By.XPATH, '//*[@id="RegisterForm_password"]').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//*[@id="register-form"]/div[4]/div').click()
        self.driver.find_element(By.XPATH, '//*[@id="register-form-submit"]').click()
        time.sleep(3)
        try:
            viaplay_text = self.driver.find_element(By.XPATH,'//*[@id="register-form"]/div[1]/div[2]/div[5]/span').text
            if viaplay_text[:8] == 'E-posten':
                self.viaplay = True
            else:
                self.viaplay = False
        except NoSuchElementException:
            self.viaplay = False
        print(self.viaplay)
    def check_hbo(self, email):
        self.driver.get('https://www.hbomax.com/subscribe')
        self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="planSelected"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys(self.f_name)
        self.driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys(self.l_name)
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//*[@id="createAccount"]').click()
        time.sleep(2)
        try:
            hbo_text = self.driver.find_element(By.XPATH, '//*[@id="generalError"]/span').text
            if hbo_text == 'Vi fant en konto med den e-postadressen. Bruk en annen e -postadresse eller prøv å logge inn.':
                self.hbo = True
            else:
                self.hbo = False
        except NoSuchElementException:
            self.hbo = False
        print(self.hbo)
#    def run_functions(self, email):
#        if __name__ == "__main__":
#            Thread(target=Search.check_amazon(email).start()
#            Thread(target=Search.check_netflix(email).start()
#            Thread(target=Search.check_viaplay(email).start()
#            Thread(target=Search.check_hbo(email).start()
