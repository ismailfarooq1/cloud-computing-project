from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ML_SERVICES = [
    "http://ml-service-1:8080/predict",
    "http://ml-service-2:8080/predict",
    "http://ml-service-3:8080/predict",
]

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    data = request.json
    response = requests.post(ML_SERVICES[0], json=data)  # Round-robin or load balancing logic
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
