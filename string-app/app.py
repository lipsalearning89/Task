'''
@summary: This script will return JSON Object when invoked with reverse string
@author: Lipsa Parida
'''
import requests
from flask import Flask
app = Flask(__name__)

# API to return JSON Object with reverse string
@app.route('/')
def reverse_string():
    response = requests.get("http://json-app-service:30000/")
    # JSON Object
    message = {
        'id': 1,
        'message': (response.json()['message'][::-1]),
    }
    return message

if __name__ == "__main__":
    app.run()
