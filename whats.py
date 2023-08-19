from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from io import BytesIO
from PIL import Image
from webbrowser import open
import win32clipboard

class PyWp:

    def __init__(self, profile_path=None, profile_name=None) -> None:
        
        #create chromeoptions instance
        self.options = webdriver.ChromeOptions()

        # options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        # options.add_argument('--disable-dev-shm-usage')

        # print(profile_path, profile_name)
        if profile_path is not None and profile_name is not None:
            print("Not None")
            #provide location where chrome stores profiles
            self.options.add_argument(f"--user-data-dir={profile_path}")

            #provide the profile name with which we want to open browser
            self.options.add_argument(f"--profile-directory={profile_name}")

            #specify where your chrome driver present in your pc
        
        self.open_browser()
            

    def open_browser(self, path="https://web.whatsapp.com/"):
        self.driver = webdriver.Chrome(options=self.options)
        #provide website url here
        self.driver.get(path)
        # time.sleep(120)
        input("Press Enter once you log in")


    def close_browser(self):
        self.driver.quit()


    def select_contact(self, phone_no: str):
        try:
            search_box_xpath = "//*[@id='side']/div[1]/div/div/div[2]/div/div[1]"
            search_box = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
            search_box.send_keys(Keys.CONTROL, "a")
            search_box.send_keys(Keys.BACKSPACE)
            for digit in phone_no:
                search_box.send_keys(digit)
                time.sleep(0.25)
            time.sleep(2)
            search_box.send_keys(Keys.ENTER)
            time.sleep(2)
        except:
            print("Not able to find contact ")
            return
        
        time.sleep(2)


    def send_message(self, phone_no: str, message: str):
        self.select_contact(phone_no)
        try:
            message_path = f'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'
            message_element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, message_path)))
            message = f'{message}'
            for letter in message:
                if letter == "\n":
                    message_element.send_keys(Keys.SHIFT, Keys.ENTER)
                else:
                    message_element.send_keys(letter)
                time.sleep(0.25)
            message_element.send_keys(Keys.ENTER)
            time.sleep(3)
        except:
            print("Message Not Sent to ", phone_no)
            return
        time.sleep(4)


    def send_messages_to_multiple_contacts(self, phone_nos: list[str], message: str):
        for phone_no in phone_nos:
            self.send_message(phone_no, message)
            time.sleep(1)


    def send_customized_messages_to_multiple_contacts(self, phone_nos: list[str], names: list[str], message: str=""):
        if len(phone_nos) != len(names):
            print("Error number of contacts should be equal to number of names")
            return ValueError
        
        for phone_no, name in zip(phone_nos, names):
            custom_message = message.replace("{name}", name)
            self.send_message(phone_no, custom_message)
            time.sleep(1)


    def send_image(self, phone_no: str, path: str, caption: str=""):
        path.replace('\\','//')
        
        self.select_contact(phone_no)

        image = Image.open(path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        
        try:
            message_path = f'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'
            message_element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, message_path)))
            message_element.send_keys(Keys.CONTROL, "v")
        except:
            print("Image Not Able to Paste")
            return
        
        try:
            caption_path = f'//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p'
            caption_element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, caption_path)))
            for char in caption:
                if char == "\n":
                    caption_element.send_keys("shift", "enter")
                else:
                    caption_element.send_keys(char)
                
            caption_element.send_keys(Keys.ENTER)
            time.sleep(2)
        except:
            print("Caption Could not be sent")
            return


    def send_image_to_multiple_contacts(self, phone_nos: list[str], path: str, caption: str=""):
        for phone_no in phone_nos:
            self.send_image(phone_no, path, caption)
            time.sleep(1)


    def send_image_to_multiple_contacts_with_custom_messages(self, phone_nos: list[str], names: list[str], path: str, caption: str=""):
        for phone_no, name in zip(phone_nos, names):
            custom_message = caption.replace("{name}", name)
            self.send_image(phone_no, custom_message)
