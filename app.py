import os
import json
import pandas as pd
from random import seed 
from random import randint
import datetime

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request


seed(1)
df = pd.read_csv('quotes.csv')


app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  if datetime.datetime.today().weekday() == 0 or data['text'] == "@inspireme":
    r = randint(0,1664)
    auth = str(df.iloc[r][0])
    quote = str(df.iloc[r][1])
    msg = quote + " - " + auth
    send_message(msg)


  return "ok", 200



def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()

def log(msg):
  print(str(msg))
  sys.stdout.flush()






