    # Purshotam: Creating a switch function for common WEB element interaction using a list of actions:
    # Interact types:
    # ['click']                      -> Clicking an xpath
    # ['ctrl_press','key']           -> To use speacial software or system functions
    # ['shift_press','key']          -> To use speacial software or system functions
    # ['alt_press','key']            -> To use speacial software or system functions
    # ['key_press',['keys_strings']] -> Sending keys one by one to an xpath
    # ['message', 'text']             -> Sending text which also contains emojies, to an xpath (whatsapp speacial)
    def element_interaction(self, xpath: str, ele_name: str, func_name: str, actions: list[interacts list]):
        # Initiating webdriver element
        element_xpath = xpath
        element_object = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
        ele_error_suffix = f"[[{ele_name}]] from the function [[{func_name}]]"
        
        # Interacting with the element based on given actions (click, send keys or message)
        for interact in actions:
            if interact[0] == 'click':
                try:
                    element_object.click()
                except:
                    error = f"Program not able to click [[{ele_name}]] from the function [[{func_name}]]"
                    print(error)
                    
            elif interact[0] == 'ctrl_press':
                try:
                    element_object.send_keys(Keys.CONTROL, interact[1])
                except:
                    error = f"Program not able to use Ctrl + [{interact[1]}] on [[{ele_name}]] from the function [[{func_name}]]"
                    print(error)
                    
            elif interact[0] == 'shift_press':
                try:
                    element_object.send_keys(Keys.SHIFT, interact[1])
                except:
                    error = f"Program not able to use SHIFT + [{interact[1]}] on [[{ele_name}]] from the function [[{func_name}]]"
                    print(error)
                    
            elif interact[0] == 'alt_press':
                try:
                    element_object.send_keys(Keys.ALT, interact[1])
                except:
                    error = f"Program not able to use ALT + [{interact[1]}] on [[{ele_name}]] from the function [[{func_name}]]"
                    print(error)
                    
            elif interact[0] == 'key_press':
                try:
                    for key in interact[1]:
                        element_object.send_keys(key)
                except:
                    error = f"Program not able to send keys to [[{ele_name}]] from the function [[{func_name}]]"
                    print(error)
                    
            elif interact[0] == 'message':
                text = interact[1]
                index = 0
                length = len(text)
                while index < length:
                    try:
                        letter = text[index]
                        if letter == ":":
                            element_object.send_keys(letter)
                            index += 1
                            while index < length:
                                letter = text[index]
                                if letter == ":":
                                    element_object.send_keys(Keys.ENTER)
                                    break
                                element_object.send_keys(letter)
                                index += 1
                        elif letter == "\n":
                            element_object.send_keys(Keys.SHIFT, Keys.ENTER)
                        else:
                            element_object.send_keys(letter)
                    except:
                        error = f"Program not able to send message to [[{ele_name}]] from the function [[{func_name}]]"
                        print(error)
                        
            else:
                error = f"Invalid interactions to [[{ele_name}]] from the function [[{func_name}]]"
                print(error)
