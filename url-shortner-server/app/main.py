from flask import Flask, redirect, render_template
import firebase_admin
from firebase_admin import db
import os
import json

# Initialize Firebase with credentials from environment or file
firebase_credentials = os.getenv('FIREBASE_CREDENTIALS')

if firebase_credentials:
    # On Render: read from environment variable (JSON string)
    try:
        cred_dict = json.loads(firebase_credentials)
        cred_obj = firebase_admin.credentials.Certificate(cred_dict)
    except (json.JSONDecodeError, ValueError) as e:
        raise RuntimeError(f"Invalid FIREBASE_CREDENTIALS format: {e}")
else:
    # Locally: read from file
    key_path = os.path.join(os.path.dirname(__file__), '..', 'ServiceAccountKey.json')
    key_path = os.path.normpath(key_path)
    cred_obj = firebase_admin.credentials.Certificate(key_path)

# Read database URL from environment or use default
database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise RuntimeError("DATABASE_URL environment variable is not set")

default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': database_url
})

app = Flask(__name__, static_folder='./build/static', template_folder="./build")

@app.route("/")
def hello_world():
    return redirect("/app")

@app.route("/app")
def homepage():
    return render_template('index.html')

@app.route('/<path:generatedKey>', methods=['GET'])
def fetch_from_firebase(generatedKey):
    ref = db.reference("/" + generatedKey)
    data = ref.get()
    if not data:
        return '404 not found'
    else:
        longURL = data['longURL']
        return redirect(longURL)
