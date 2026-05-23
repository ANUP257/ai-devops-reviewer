import os
import requests

# Intentional bad code for AI to catch!
password = "admin123"
api_key = "hardcoded-secret-key"

def get_data():
    response = requests.get("http://api.example.com/data")
    return response.json()
db_password = "root123"
