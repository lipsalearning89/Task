'''
@summary: This script will return JSON Object when invoked
@author: Lipsa Parida
'''
from flask import Flask
app = Flask(__name__)

# JSON Object
message = {
    "id": 1,
    "message": "The quick brown fox jumps over the lazy dog"
}

# API to return JSON Object
@app.route('/')
def json_generator():
    return message

if __name__ == "__main__":
    app.run()
