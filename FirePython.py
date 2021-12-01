from pyrebase import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCWq0mNjVy_GcjUluOJhrEZY_XhGJBJmAQ",
    "authDomain": "firepython-3941d.firebaseapp.com",
    "projectId": "firepython-3941d",
    "storageBucket": "firepython-3941d.appspot.com",
    "messagingSenderId": "274558622690",
    "appId": "1:274558622690:web:29dcc70f111a3ea1b6b7bb",
    "measurementId": "G-GEV0W2HL1Q",
    "databaseURL": "https://firepython-3941d-default-rtdb.asia-southeast1.firebasedatabase.app/"
  }

firebase = pyrebase.initialize_app(firebaseConfig)


auth = firebase.auth()
db = firebase.database()


def login():
    email = input("Enter Your Email : ")
    password = input("Enter Your Password : ")
    user = auth.sign_in_with_email_and_password(email, password)
    print(user)
    data(user)

def data(user):
    email = input("Enter Your Email : ")
    db.child("USERS").child(email).push(
        {"user":email,
        "Vinu": "Code"}, user['idToken'])
    print("Sucessful!!!")

login()