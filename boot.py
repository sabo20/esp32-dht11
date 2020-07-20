import network
import ujson

# reading config file
try:
    # Config esp32
    f = open('config.json', 'r')
    config = ujson.loads(f.read())
    # Credenziali router
    ssid = config['wifi']['ssid']
    password = config['wifi']['password']
    f.close()
except OSError as e:
    print('Oops! Impossible to connect to wifi, verify your credential.')

# connection to local wifi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())
