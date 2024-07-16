from fastapi import FastAPI, Response ,HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import util


app = FastAPI()
util.load_saved_artifact()

@app.get('/get_location_names')
async def get_location_names():
    locations = util.get_location_names()
    
    response = JSONResponse(content={'locations': locations})

    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

@app.post('/predict_home_price')
async def predict_home_price(request: Request):
    form_data = await request.form()
    
    total_sqft = float(form_data['total_sqft'])
    location = form_data['location']
    size = int(form_data['bhk'])
    bath = int(form_data['bath'])

    estimated_price = util.get_estimated_price(location, total_sqft, size, bath)
    
    response = JSONResponse(content={'estimated_price': estimated_price})
    
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

if __name__ == "__main__":
    print("Starting Python FastAPI Server For Home Price Prediction...")
    util.load_saved_artifact()
    app.run()
