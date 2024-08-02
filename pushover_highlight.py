import hexchat
import requests

__module_name__= "Pushover Notifications"
__module_version__ = "1.3"
__module_description__ = "Send Pushover notifications"

pushover_user_key = ""
pushover_api_token = ""

def pushover_notify(title, message):
    url = "https://api.pushover.net/1/messages.json"
    data = {
        "token": pushover_api_token,
        "user": pushover_user_key,
        "title": title,
        "message": message,
        "priority": 1  # Set priority to 1
    }
    requests.post(url, data=data)

def on_highlight(word, word_eol, userdata):
    title = "Message Highlighted in Hexchat "
    message = f"Highlight from {word[0]}: {word[1]}"
    pushover_notify(title, message)
    return hexchat.EAT_NONE

hexchat.hook_print("Channel Msg Hilight", on_highlight)
hexchat.hook_print("Channel Action Hilight", on_highlight)

hexchat.prnt(__module_name__ + " loaded.")
