import requests
import json
import random
import logging
import sys
from datetime import datetime
import time

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
    level=logging.INFO,
)

def get_quote():
    try:
        url = "https://type.fit/api/quotes"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        quotes = json.loads(response.text)
        my_quote = quotes[random.randrange(len(quotes)-1)]
        logger.info(my_quote)
        return my_quote["text"], my_quote["author"]
    except:
        print("Error occured: retry")
        return "None", "None"

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # date_today = now.

for i in range(5):
    quote, author = get_quote()
    print(quote, author)
    time.sleep(3)