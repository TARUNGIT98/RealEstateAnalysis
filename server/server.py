from flask import Flask, request, jsonify
import util
from flask_cors import CORS
import os
import json

# Initialize Flask app
app = Flask(__name__)
CORS(app)


# Debugging: Check if the artifacts folder and columns.json exist
@app.route('/api/debug_files')
def debug_files():
    artifacts_path = "./artifacts/"
    try:
        files = os.listdir(artifacts_path)
    except Exception as e:
        files = f"Error accessing artifacts: {str(e)}"

    return jsonify({"files_in_artifacts": files})


# Debugging: Check the content of columns.json
@app.route('/api/debug_columns')
def debug_columns():
    try:
        columns_path = "./artifacts/columns.json"
        if not os.path.exists(columns_path):
            return jsonify({"error": "columns.json not found"})

        with open(columns_path, 'r') as f:
            data = json.load(f)
        return jsonify({"columns_json": data})
    except Exception as e:
        return jsonify({"error": str(e)})


# API Endpoint: Get all location names
@app.route('/api/get_location_names')
def get_location_names():
    locations = util.get_location_names()
    print("DEBUG: Locations from util.py:", locations)  # Debug log

    if locations is None or len(locations) == 0:
        return jsonify({"error": "Locations not loaded or empty"}), 500

    response = jsonify({'locations': locations})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# API Endpoint: Predict home price
@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        data = request.get_json()

        # Check if all required fields exist
        if 'total_sqft' not in data or 'location' not in data or 'bhk' not in data or 'bath' not in data:
            return jsonify({"error": "Missing parameters"}), 400

        total_sqft = float(data['total_sqft'])
        location = data['location']
        bhk = int(data['bhk'])
        bath = int(data['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Start the Flask app
if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction")
    util.load_saved_artifacts()

    port = int(os.environ.get("PORT", 10000))  # Render assigns a PORT dynamically
    app.run(host='0.0.0.0', port=port)
