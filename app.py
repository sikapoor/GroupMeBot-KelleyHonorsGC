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

"""
data = {
  "attachments": [],
  "avatar_url": "http://i.groupme.com/123456789",
  "created_at": 1302623328,
  "group_id": "52652881",
  "id": "52652881",
  "name": "John",
  "sender_id": "12345",
  "sender_type": "user",
  "source_guid": "GUID",
  "system": false,
  "text": "Hello world ☃☃",
  "user_id": "1234567890"
}
"""



@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  # We don't want to reply to ourselves!
  if datetime.datetime.today().weekday() == 0 or data['text'] == "@inspireme":
    r = randint(0,1664)
    auth = str(df.iloc[r][0])
    quote = str(df.iloc[r][1])
    msg = quote + " - " + auth
    send_message(msg)

    """
    msg = '{}, you sent "{}".'.format(data['name'], data['text'])
    msg = "Forty hour workweeks are a relic of the Industrial Age. Knowledge workers function like athletes — train and sprint, then rest and reassess."
    send_message(msg)
    """

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

"""
Registering my bot

  {"meta":{"code":201},"response":{"bot":{"name":"Inspi_bot",
  "bot_id":"50d85fe0f44b61086376584a48",
  "group_id":"52652881","group_name":"Soon to be TS fans","avatar_url":null,
  "callback_url":null,
  "dm_notification":false}}}(base) Simars-MacBook-Pro:gmbot simar$ 
"""





