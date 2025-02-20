import os
import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)

def get_location_names():
    global __locations

    print("DEBUG: Getting locations...")
    print(f"DEBUG: __locations variable = {__locations}")

    if __locations is None:
        print("ERROR: Locations not loaded!")
        return None

    return __locations


def load_saved_artifacts():
    global __data_columns, __locations, __model

    artifacts_dir = os.path.dirname(__file__)  # Get the current directory
    columns_path = os.path.join(artifacts_dir, "artifacts", "columns.json")

    print(f"DEBUG: Looking for columns.json at {columns_path}")

    if not os.path.exists(columns_path):
        print(f"ERROR: columns.json NOT FOUND at {columns_path}")
        return

    # Load the columns.json file
    try:
        with open(columns_path, 'r') as f:
            data = json.load(f)
            __data_columns = data['data_columns']
            __locations = __data_columns[3:]  # Skip sqft, bath, bhk
    except Exception as e:
        print(f"ERROR: Failed to read columns.json -> {e}")
        return

    print(f"DEBUG: Loaded locations: {__locations}")

    # Load the model
    model_path = os.path.join(artifacts_dir, "artifacts", "banglore_home_prices_model.pickle")

    if not os.path.exists(model_path):
        print(f"ERROR: Model file NOT FOUND at {model_path}")
        return

    try:
        with open(model_path, 'rb') as f:
            __model = pickle.load(f)
    except Exception as e:
        print(f"ERROR: Failed to load model -> {e}")
        return

    print("DEBUG: Successfully loaded model and artifacts")
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())  # Should print list of locations or an error message
    print(get_estimated_price('Kalhali', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))
