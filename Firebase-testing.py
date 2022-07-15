from firebase import firebase
import random

firebase = firebase.FirebaseApplication('https://parker-92cd8-default-rtdb.firebaseio.com/', None)



while True:
    #Payment = {"Sr": "1", "App": "Gpay", "Contact": "95xxxxxxx", "Name": "Anas", "Amount": "2000", "Description": "Anything"}
    firebase.put('Data/','parking-3', "full")
    
    print("Done")
            

