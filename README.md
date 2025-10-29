# 🌡️ ESP8266 DHT22 Temperature & Humidity Sensor — MicroPython

## 🧠 Overview
This project shows how to interface a **DHT22 (AM2302)** sensor with an **ESP8266** using **MicroPython**.  
It reads **temperature** and **humidity** values every 2 seconds and displays them on the **Thonny IDE console**.

---

## ⚙️ Hardware Setup

| Component | ESP8266 Pin | Description |
|------------|-------------|--------------|
| DHT22 (Data) | GPIO4 (D2) | Sensor data output |
| VCC | 3.3V | Power supply |
| GND | GND | Common ground |

🪛 **Connections:**
- DHT22 **VCC → 3.3V**
- DHT22 **GND → GND**
- DHT22 **Data → GPIO4 (D2)**  
- Add a **10kΩ pull-up resistor** between **VCC** and **Data** for stable readings.

---

## 🧩 Code

```python
# GPIO04 = D2 = Data of DHT22

import machine
import dht
import utime

dh = dht.DHT22(machine.Pin(4))

while True:
    dh.measure()
    utime.sleep_ms(2000)
    tem = dh.temperature()
    hum = dh.humidity()
    print('Humidity:', hum, 'TEMPERATURE:', tem)
