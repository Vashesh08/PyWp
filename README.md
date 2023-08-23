# PyWp
Sending Automated Whatsapp Messages To Contacts Using Python.

Contact Needs to be already saved in Your Phone

Press Enter on cmd once you login to WhatsApp

# Cloning The Repository
```
git clone https://github.com/Vashesh08/PyWp.git
```

# Install The Dependencies
```
pip install -r PyWp\requirements.txt
```

# Usage
```
from whats import PyWp

pywp = PyWp()

# Send a WhatsApp Message to a Contact
pywp.send_message("+910123456789", "Hello")

# Send Same Message To Multiple Contacts
pywp.send_messages_to_multiple_contacts(["+910123456789", "910123456789"], "Hello")

# Send a Image to a Contact
pywp.send_image("+910123456789", r"C:\Users\path_to_image", "Caption")

# Send Same Image to Multiple Contacts
pywp.send_image_to_multiple_contacts(["+910123456789", "910123456789"], r"C:\Users\path_to_image", "caption")

# Send a Video to a Contact
pywp.send_video("+910123456789", r"C:\Users\path_to_video", "Caption")

# Send Same Video to Multiple Contacts
pywp.send_video_to_multiple_contacts(["+910123456789", "910123456789"], r"C:\Users\path_to_video", "caption")

# To logout of Whatsapp and close browser
pywp.close_browser()
```
