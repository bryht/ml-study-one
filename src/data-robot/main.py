import threading
import time
import requests
from decouple import config
from datetime import datetime
import random

class BackgroundTasks(threading.Thread):
    def run(self, *args, **kwargs):
        while True:
            url = config('DATA_INPUT_URL')
            data = {'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'humidity': str(random.randint(20,70)), 'temperature': str(random.randint(0,35))}
            x = requests.post(url, json=data)
            print(x.text)
            time.sleep(10)
t = BackgroundTasks()
t.start()
