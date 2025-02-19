import json
import pickle
import numpy as np

#json: Used to read and parse JSON files (for column metadata).
#pickle: Used to deserialize (load) a saved machine learning model.

__locations = None
__data_columns = None
__model = None

# __locations: Stores a list of available locations for making predictions.
# __data_columns: Stores the names of all feature columns used in training the model.
# __model: Stores the loaded machine learning model.

def get_estimated_price(location,sqft,bath,bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

# Returns the list of location names that the model recognizes.
# This function is useful for providing dropdown options in a frontend UI.


import os

ARTIFACTS_PATH = os.path.join(os.path.dirname(__file__), "artifacts")

def load_saved_artifacts():
    global __data_columns, __locations, __model

    with open(os.path.join(ARTIFACTS_PATH, "columns.json"), 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open(os.path.join(ARTIFACTS_PATH, "banglore_home_prices_model.pickle"), 'rb') as f:
        __model = pickle.load(f)

    print("DEBUG: Loaded locations:", __locations)
 # Debugging line
    print("loading saved artifacts...done")



if __name__ == '__main__':
    load_saved_artifacts()
    # loads the model and metadata
    print(get_location_names())
    print(get_estimated_price('Kalhali',1000,2,2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))
