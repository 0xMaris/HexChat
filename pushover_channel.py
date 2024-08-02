import hexchat
import requests

__module_name__ = "Highlight and Pushover Notification"
__module_version__ = "1.2"
__module_description__ = "Highlights messages in a specific channel and sends Pushover notifications on highlight"

network_name = ""  # Replace with your network name
channel_names = ["#channel1", "#channel2"]  # Replace with your channel names
pushover_user_key = ""
pushover_api_token = ""

def pushover_notify(title, message):
    url = "https://api.pushover.net/1/messages.json"
    data = {
        "token": pushover_api_token,
        "user": pushover_user_key,
        "title": title,
        "message": message,
    }
    requests.post(url, data=data)

def on_highlight(word, word_eol, userdata, current_channel):
    title = "Hexchat Notification " + current_channel
    message = f"Highlight from {word[0]}: {word[1]}"
    pushover_notify(title, message)
    return hexchat.EAT_NONE

def highlight_specific_channels_cb(word, word_eol, userdata):
    current_network = hexchat.get_info('network')
    current_channel = hexchat.get_info('channel')

    if current_network == network_name and current_channel in channel_names:
        hexchat.command('GUI COLOR 3')  # 3 is the color index for highlight
        on_highlight(word, word_eol, userdata, current_channel)  # Trigger the Pushover notification
    else:
        hexchat.prnt(f"Message from {current_network}/{current_channel} ignored")

    return hexchat.EAT_NONE

hexchat.hook_print('Channel Message', highlight_specific_channels_cb)
hexchat.hook_print('Channel Msg Hilight', highlight_specific_channels_cb)
hexchat.hook_print('Channel Action', highlight_specific_channels_cb)
hexchat.hook_print('Channel Action Hilight', highlight_specific_channels_cb)
