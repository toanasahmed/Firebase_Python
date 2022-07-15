"""
LIBRARIES:
Firebase: https://morioh.com/p/4dca3ded4cea 
TTYUSB: https://diyi0t.com/arduino-to-raspberry-pi-serial-communication/
"""
from firebase import firebase

import json
import serial

ser = serial.Serial('/dev/ttyACM0',9600)
i = 0

while(True):
    from firebase import firebase
    
    x=(ser.readline().decode('utf-8').rstrip())
    #print(x)
    i = i + 1
    if(i > 10):
        if ser.isOpen():
            y = json.loads(x)
            firebase = firebase.FirebaseApplication('https://dronedata-b013d.firebaseio.com/', None)
            firebase.put('/Data','Temperature', y["Temperature"])
            firebase.put('/Data','Humidity', y["Humidity"])
            firebase.put('/Data','Dust', y["Dust"])
            firebase.put('/Data','CO', y["CO"])
            firebase.put('/Data','CH4', y["CH4"])
            print('Record Updated')            
