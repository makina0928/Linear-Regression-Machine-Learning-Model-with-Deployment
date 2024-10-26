import numpy as np
from flask import Flask, render_template, request
import joblib
from src.forms import CarForm
from src.config import Config

app = Flask('Car Price Prediction')
app.config.from_object(Config)

# Load the scaler and the model
scaler = joblib.load('mlmodel/scaling.pkl')
model = joblib.load('mlmodel/car_price_prediction.pkl')

@app.route('/', methods=['GET'])
def home():
    car_form = CarForm()
    if car_form.validate_on_submit():
        car_age = int(car_form.car_age.data)
        car_fuel = car_form.car_fuel.data
        car_doors = int(car_form.car_doors.data)
        car_cc = int(car_form.car_cc.data)
        car_horsepower = int(car_form.car_horsepower.data)
        car_transmission = car_form.car_transmission.data
        car_odometer = int(car_form.car_odometer.data)
        car_weight = car_form.car_weight.data
        car_color = car_form.car_color.data

    return render_template('car.html', form=car_form)

@app.route('/', methods=['POST'])
def result():
    try:
        form = request.form
        fuel = 1 if int(form['car_fuel']) == 1 else 0
        car_transmission = 1 if int(form['car_transmission']) == 1 else 0
        car_color = 1 if int(form['car_color']) == 1 else 0

        # Prepare the input data
        new_car = np.array([
            int(form['car_odometer']),
            fuel,
            int(form['car_doors']),
            car_transmission,
            int(form['car_horsepower']),
            car_color,
            int(form['car_cc']),
            int(form['car_weight']),
            int(form['car_age'])
        ]).reshape(1, -1)

        # Scale the input data
        new_car_scaled = scaler.transform(new_car)

        # Predict the price
        predicted_price = model.predict(new_car_scaled)
        predicted_price = max(0, int(predicted_price))  # Ensure non-negative price

        return render_template('result.html', price=predicted_price)
    except ValueError:
        return render_template('error.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
