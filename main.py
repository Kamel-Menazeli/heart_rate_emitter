import pyrebase
from random import randint
from time import sleep

firebaseConfig = {
    "apiKey": "AIzaSyA9iVMh1oY3F8WQ-cUuPLAtrfY2aUMpX2s",
    "authDomain": "heartrate-8fc50.firebaseapp.com",
    "projectId": "heartrate-8fc50",
    "storageBucket": "heartrate-8fc50.appspot.com",
    "databaseURL": "https://heartrate-8fc50-default-rtdb.europe-west1.firebasedatabase.app/",
    "messagingSenderId": "82089823374",
    "appId": "1:82089823374:web:655c54cc68590867590ddf",
    "measurementId": "G-PM2BCMQ4TM"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

for i in range(1, 100):
    random_value = randint(91, 130)
    data = random_value
    db.child("heart rate values").push(data)
    print(f"heart rate num = {i}: {data}")
    print("-"*50)
    sleep(5)




