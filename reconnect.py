import hexchat
import time

__module_name__ = "Automatically Reconnect"
__module_version__ = "1.0"
__module_description__ = "Refreshes IRC"

def reconnect(timer):
    hexchat.command('QUIT :Reconnecting...')
    hexchat.command('RECONNECT')

def schedule_reconnect():
    hexchat.hook_timer(14400000, reconnect) #amount of seconds before reconnecting

hexchat.prnt("Auto-reconnect script loaded")
schedule_reconnect()
