from flask import Flask,jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST','GET'])
def getHealthTest():
    try:
        
        
        message = "Welcome , This is Flask API"

    except Exception as e:
        message = e

    return message        

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8080)    
    