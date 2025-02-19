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
    if __locations is None:
        print("ERROR: Locations not loaded.")
        return []  # Return an empty list instead of None to prevent frontend crashes
    return __locations

def load_saved_artifacts():
    global __data_columns, __locations, __model

    print("DEBUG: Loading saved artifacts...")

    # Ensure correct path resolution
    base_path = os.path.dirname(os.path.abspath(__file__))
    artifacts_path = os.path.join(base_path, "artifacts")

    columns_path = os.path.join(artifacts_path, "columns.json")
    model_path = os.path.join(artifacts_path, "banglore_home_prices_model.pickle")

    # Check if columns.json exists
    if not os.path.exists(columns_path):
        print(f"ERROR: columns.json not found at {columns_path}")
        return

    # Load columns.json
    with open(columns_path, 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # Locations start from index 3
    print(f"DEBUG: Loaded locations: {len(__locations)} locations found.")

    # Check if model exists
    if not os.path.exists(model_path):
        print(f"ERROR: Model file not found at {model_path}")
        return

    # Load model
    with open(model_path, 'rb') as f:
        __model = pickle.load(f)

    print("DEBUG: Loading saved artifacts... Done.")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())  # Should print list of locations or an error message
    print(get_estimated_price('Kalhali', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))
