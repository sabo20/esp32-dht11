import machine
import dht
import time
d = dht.DHT11(machine.Pin(23))

while True:
    # reading
    d.measure()
    # get data
    temp = d.temperature()
    hum = d.humidity()
    print("{\"t\":\"", temp, "\",\"h\":\"", hum, "\"}")
    # sleep for 5 min
    time.sleep(5)  #  300 sec -> 5 min
