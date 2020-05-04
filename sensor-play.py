import urllib.request
import time
from pythonosc import udp_client
from pythonosc import osc_message_builder

link = "http://192.168.1.7:8080/"
def getData():
    with urllib.request.urlopen(link) as url:
        data = url.read()
        print(data)
        return data

while True:
    sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
    data=getData().decode()
    sender.send_message('/trigger/hollow', [float(data), 5.5])
    time.sleep(3)
