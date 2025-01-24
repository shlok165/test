import firebase_admin
from firebase_admin import credentials, db
import os

# Initialize Firebase Admin only once
if not firebase_admin._apps:
    cred_path = os.path.join(os.path.dirname(__file__), 'serviceAccountKey.json')
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://aquaintigrity-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
