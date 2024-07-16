import json
import pickle
import numpy as np
__location = None
__model = None
__data_columns = None


def get_location_names():
    return __location

def load_saved_artifact():
    global __data_columns
    global __location

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    global __model
    with open("./artifacts/banglore_home_prices_model.pickle", "rb") as m:
        __model = pickle.load(m)

def get_estimated_price(location, sqft, size, bath):
    global __location

    try:
        index_loc = __location.index(location.lower())
    except:
        index_loc = -1
    # print(index_loc)


    x = np.zeros(len(__data_columns))

    x[0] = size
    x[1] = sqft
    x[2] = bath
    if index_loc > 0:
        x[index_loc] = 1
    return round(__model.predict([x])[0], 2)

if __name__ == "__main__":
    load_saved_artifact()
    print(get_location_names())
    # print(get_estimated_price('1st Phase JP Nagar',1000, 2, 2))
