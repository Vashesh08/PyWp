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
import json
from selunium_web_element_actions.py import element_interaction

# IMPORTANT FOR DEVELOPERS OR SCRIPT KIDDIES!!!!
# Important GENERIC function used in this script:
# element_interaction(xpath: str, ele_name: str, func_name: str, actions: list[interacts list])
# element_interaction(xpath, ele_name, func_name, actions)

# Important DATA imported and used in this script:
# XPATHS from whatsapp_xpaths.json
# whatsapp_xpaths.json also contain one metadata about the xpaths called "function" which stores
# the function names in which these xpaths are likely or are already in use. This metadata helps
# helps developers or script kiddies to debug in case of whatsapp modifying its user interface
# rending the xpaths useless by letting them change xpaths through function generated custom 
# error.

# If you want to understand the script please checkout these two files:
# selenium_web_element_actions.py
# whatsapp_xpaths.json

class PyWp:

    def __init__(self, profile_path=None, profile_name=None) -> None:
        
        #create chromeoptions instance
        self.options = webdriver.ChromeOptions()

        # options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        # options.add_argument('--disable-dev-shm-usage')

        prefs = {"profile.default_content_setting_values.media_stream_camera" : 1}
        self.options.add_experimental_option("prefs",prefs)
        
        # print(profile_path, profile_name)
        if profile_path is not None and profile_name is not None:
            # print("Not None")
            #provide location where chrome stores profiles
            self.options.add_argument(f"--user-data-dir={profile_path}")

            #provide the profile name with which we want to open browser
            self.options.add_argument(f"--profile-directory={profile_name}")

            #specify where your chrome driver present in your pc
        
        self.open_browser()

        # Purshotam: importing the xpaths for web-app elements (XAPTHS from WHATSAPP_XPATHS.JSON)
        with open('whatsapp_xpaths.json', 'r') as json_file:
            self.xpaths = json.load(json_file)
            

    def open_browser(self, path="https://web.whatsapp.com/"):
        self.driver = webdriver.Chrome(options=self.options)
        #provide website url here
        self.driver.get(path)
        # time.sleep(120)
        input("Press Enter once you log in")

    # Purshotam: Directly referencing nav_xpath from XPATHS dictionary.
    def logout(self):
        this_func_name = logout.__name__
        
        action_click = [ [['click']] ]

        # Ensuring logout by clicking nav_button then log_button and at the end log_confirmation_button
        element_interaction(self.xpaths['nav_xpath']['path'], 'nav', this_func_name, action_click)
        element_interaction(self.xpaths['logout_xpath']['path'], 'logout_button', this_func_name, action_click)
        element_interaction(self.xpaths['logout_confirmation_xpath']['path'], 'logout_confirm', this_func_name, action_click)
        
        time.sleep(25)


    def close_browser(self):
        self.logout()
        self.driver.quit()


    def select_contact(self, phone_no: str):
        this_func_name = select_contact.__name__
        
        try:
            action_opening_search = [ ['ctrl_press','a'], ['key_press',[Keys.BACKSPACE]] ]
            element_interaction(self.xpaths['search_box_xpath']['path'], 'contact_search_box', this_func_name, action_opening_search)
            
            for digit in phone_no:
                action_enter_digit = [ ['key_press',[digit]] ]
                element_interaction(self.xpaths['search_box_xpath']['path'], 'contact_search_box', this_func_name, action_enter_digit)
                search_box.send_keys(digit)
                time.sleep(0.25)
            time.sleep(2)

            action_send = [ ['key_press',[Keys.ENTER]] ]
            element_interaction(self.xpaths['search_box_xpath']['path'], 'contact_search_box', this_func_name, actions)
            time.sleep(2)
        except:
            print("Not able to find contact ")
            return
        
        time.sleep(2)


    def send_message(self, phone_no: str, message: str):
        this_func_name = send_message.__name__
        
        self.select_contact(phone_no)
        try:
            action_send_message = [ ['message', message], ['key_press',[Keys.ENTER]] ]
            element_interaction(self.xpaths['message_xpath']['path'], 'message_box', this_func_name, action_send_message)
            
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
        this_func_name = send_image.__name__
        
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
            action_paste_image = [ ['ctrl_press', 'v'] ]
            element_interaction(self.xpaths['message_xpath']['path'], 'message_box', this_func_name, action_paste_image)
        
        except:
            print("Image Not Able to Paste")
            return
        
        try:
            action_send_image_with_caption = [ ['message',caption], ['key_press',[Keys.ENTER]]]
            element_interaction(self.xpaths['caption_xpath']['path'], 'caption_box', this_func_name, action_send_image_with_caption)
            
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
            self.send_image(phone_no, path, custom_message)
            time.sleep(1)


    def send_video(self, phone_no: str, vid_path: str, caption: str="", wait_time=25):
        this_func_name = send_video.__name__
        
        vid_path.replace('\\','//')
        
        self.select_contact(phone_no)
        action_click = [ ['click'] ]
        action_paste_video = [ ['key_press',[path]] ]
        action_send_video_with_caption = [ ['message',caption], ['key_press',[Keys.ENTER]] ]

        # Opening Attach Button
        try:
            element_interaction(self.xpaths['attachment_xpath']['path'], 'attachment_button', this_func_name, action_click)
        except:
            print("Not Able to open Attachment")
            return
        
        try:
            element_interaction(self.xpaths['video_attachment_xpath']['path'], 'video_attachment_box', this_func_name, action_paste_video)
            time.sleep(5)
        except:
            print("Not Able to Attach Video")
            return
        
        try:
            element_interaction(self.xpaths['caption_xpath']['path'], 'caption_box', this_func_name, action_send_video_with_caption)
            time.sleep(2)
        except:
            print("Image Caption Could not be sent")
            return
        
        time.sleep(max(20, wait_time))


    def send_video_to_multiple_contacts(self, phone_nos: list[str], path: str, caption: str=""):
        for phone_no in phone_nos:
            self.send_video(phone_no, path, caption)
            time.sleep(1)


    def send_video_to_multiple_contacts_with_custom_messages(self, phone_nos: list[str], names: list[str], path: str, caption: str=""):
        for phone_no, name in zip(phone_nos, names):
            custom_message = caption.replace("{name}", name)
            self.send_video(phone_no, path, custom_message)
            time.sleep(1)
                

        
