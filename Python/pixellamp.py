import requests
import random

# IP/Hostname des WLED Mikrocontrollers
wled_api_url = 'http://192.168.1.245/json'

# Anzahl der LEDs
num_leds = 46

# Liste mit LED Index und zufälligem Farbwert
flat_list = [i if i % 2 == 0 else format(random.randint(0, 0xFFFFFF), '06x') for i in range(num_leds * 2)]

# JSON Kommando
wled_json_data = {
    "seg": {
        "i": flat_list
    }
}

# Kommando absetzen
requests.post(wled_api_url, headers={'Content-Type': 'application/json'}, json=wled_json_data)
