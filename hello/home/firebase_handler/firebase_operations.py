from firebase_admin import db

# Write data to Firebase
def write_data(data):
    ref = db.reference('/')  # Change to your specific node if needed
    ref.set(data)
    print("Data written successfully.")

# Update specific fields without overwriting all data
def update_data(data):
    ref = db.reference('/')
    ref.update(data)
    print("Data updated successfully.")

# Push new data with an auto-generated key
def push_data(data):
    ref = db.reference('/sensor_logs')
    ref.push(data)
    print("Data pushed successfully.")

# Read data from Firebase
def read_data():
    ref = db.reference('/')
    return ref.get()

from firebase_admin import db

# Function to listen for changes
def listen_for_changes():
    ref = db.reference('/')
    
    # Callback function to handle changes
    def callback(event):
        print(f"Data changed: {event.data}")

    # Attach the listener
    ref.listen(callback)
