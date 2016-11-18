import sys
import time
import os
import subprocess
from datetime import datetime

import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton




def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    ct = msg[content_type].lower()
    print ct

    if ct == '/lock':
        try:
            command = 'gnome-screensaver-command -l' 
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output = process.communicate()[0]
            bot.sendMessage(chat_id,'Screen Locked!')
        except Exception as e:
            bot.sendMessage(chat_id,'Error: {}'.format(e))

    if ct == 'shutdown':
        pass

    if ct == '/fecha':
        now = datetime.now()
        bot.sendMessage(chat_id,str(now))

    if '/get' in ct:
        bot.sendMessage(chat_id,'Searching ...')
        ct1 =ct.replace('/get ','')
        ct1 = ct1.replace(' ', '+')
        

        print 'ct1', ct1
        url = 'https://www.google.cl/search?q='+ct1+'&tbm=isch'
        print 'ct2', url
        bot.sendMessage(chat_id, url)
        bot.sendPhoto(chat_id=chat_id, photo=str(url))





#TOKEN = sys.argv[1]  # get token from command-line
TOKEN = 'insert_token'

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)


print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
