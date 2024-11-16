import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("Path/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendance-fyp-default-rtdb.firebaseio.com"
})

ref = db.reference('Students')
data = {
    "S21NINFT1M1004":
        {
            "name": "GHULAM MUSTAFA",
            "Gender": "Male",
            "starting_year": 2024,
            "total_attendance": 0,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "S21NINFT1M1003":
        {
            "name": "HAMZA LATIF",
            "Gender": "Male",
            "starting_year": 2024,
            "total_attendance": 0,
            "standing": "Good",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

}

for key, value in data.items():
    ref.child(key).set(value)
