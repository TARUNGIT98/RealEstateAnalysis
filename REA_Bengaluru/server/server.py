from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)
# CORS(app) allows requests from any origin

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])  # ✅ Accept only POST requests
def predict_home_price():
    try:
        # ✅ Expecting JSON data, not form data
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided"}), 400  # Bad Request

        # ✅ Extract data safely
        total_sqft = float(data.get('total_sqft', 0))
        location = data.get('location', '')
        bhk = int(data.get('bhk', 0))
        bath = int(data.get('bath', 0))

        if not location:
            return jsonify({"error": "Missing required fields"}), 400  # Bad Request

        # ✅ Call util function for prediction
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)  # ✅ Enable debug mode for better error messages
