import os
import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)

url = "https://notify-api.line.me/api/notify" 
token = os.getenv('Notify_API_TOKEN')
headers = {"Authorization" : "Bearer "+ token} 
message =  os.getenv('MESSAGE')
payload = {"message" :  message} 
r = requests.post(url, headers = headers, params=payload) 
