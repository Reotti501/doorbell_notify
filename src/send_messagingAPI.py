import os
import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)

# Send LINE message
def line_message():
    url = "https://api.line.me/v2/bot/message/push"
    access_token = os.getenv('Messaging_API_TOKEN')
    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
    }
    # Loop through user_ids
    user_ids = os.getenv('USER_IDS').split(',')
    for user_id in user_ids:
        payload = {
            "to": user_id,
            "messages": [
                {
                    "type": "text",
                    "text": os.getenv('MESSAGE'),
                }
            ]
        }
        response = requests.post(url, headers=headers, json=payload)
        print("Response:", response.text)
        retry_count = 0
        # Retry 3 times if status code is not 200 series
        while retry_count < 3 and not (200 <= response.status_code < 300):
            response = requests.post(url, headers=headers, json=payload)
            print("Failed to send LINE message: " + response.status_code + ", " + response.text)
            print("Retry count: " + str(retry_count))
            retry_count += 1

        if 200 <= response.status_code < 300:
            print("Success to send LINE message")
        else:
            print("Failed to send LINE message: " + response.status_code + ", " + response.text)

line_message()