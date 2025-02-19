from flask import Flask, request, jsonify
import util
from flask_cors import CORS

# flask can help write python service which can send/serve http requests
# configure the interpreter
app = Flask(__name__)
CORS(app)

# Define a route for the root URL "/"
@app.route('/api/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    print("DEBUG: Locations from util.py:", locations)  # Debug log
    if locations is None:
        return jsonify({"error": "Locations not loaded"}), 500
    response = jsonify({'locations': locations})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()
    total_sqft = float(data['total_sqft'])
    location = data['location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    response = jsonify({
        'estimated_price' : util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/api/debug_files')
def debug_files():
    artifacts_path = "./artifacts/"
    try:
        files = os.listdir(artifacts_path)
    except Exception as e:
        files = f"Error accessing artifacts: {str(e)}"

    return jsonify({"files_in_artifacts": files})


import os

if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction")
    util.load_saved_artifacts()
    port = int(os.environ.get("PORT", 10000))  # Render assigns a PORT dynamically
    app.run(host='0.0.0.0', port=port)

