#GPIO04 = D2 =Data of DHT22

import machine
import dht
import utime

dh = dht.DHT22(machine.Pin(4))

while True:
    dh.measure()
    utime.sleep_ms(2000)
    tem = dh.temperature()
    hum = dh.humidity()
    print('Humidity:',hum, 'TEMPERATURE:',tem)