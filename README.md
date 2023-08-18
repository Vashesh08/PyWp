# PyWp
Sending Automated Whatsapp Messages To Contacts Using Python.

Contact Needs to be already saved in Your Phone

Press Enter on cmd once you login to WhatsApp

# Cloning The Repository
```
git clone https://github.com/Vashesh08/PyWp.git
```

# Usage
```
import pywp.whats as PyWp

# Send a WhatsApp Message to a Contact
PyWp.PyWp().send_message("+910123456789", "Hello")

# Send Same Message To Multiple Contacts
PyWp.PyWp().send_messages_to_multiple_contacts(["+910123456789", "910123456789"], "Hello")

# Send a Image/Video in WhatsApp to a Contact
PyWp.PyWp().send_image_or_video("+910123456789", r"C:\Users\path_to_image_or_video", "Caption")

# Send a Image/Video in WhatsApp to Multiple Contacts
PyWp.PyWp().send_image_or_video_to_multiple_contacts(["+910123456789", "910123456789"], r"C:\Users\path_to_image_or_video", "caption")
```
