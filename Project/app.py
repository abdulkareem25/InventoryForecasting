# first make sure that you have installed the packages 
# run the below command to install the required packages
# pip install flask pandas matplotlib statsmodels


from flask import Flask, render_template, request
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import numpy as np

app = Flask(__name__)

# Function to forecast future values
def forecast_sales(data, future_years):
    try:
        # Preparing the data
        data['Date'] = pd.to_datetime(data[['Year', 'Month']].assign(DAY=1))
        data.set_index('Date', inplace=True)
        data = data['Sales']

        # Fit ARIMA model
        model = ARIMA(data, order=(5, 1, 0))
        model_fit = model.fit()

        # Forecast future sales
        forecast = model_fit.forecast(steps=12 * len(future_years))

        # Creating the forecast dataframe
        forecast_df = pd.DataFrame({'Sales': forecast})
        return forecast_df

    except Exception as e:
        print(f"Error in forecast_sales: {e}")
        return None

# Function to format historical and forecasted data
def format_data(historical_data, forecast, future_years):
    if forecast is None:
        raise ValueError("Forecast data is not available")

    # Ensure correct month assignment
    forecast['Year'] = np.repeat(future_years, 12)
    forecast['Month'] = [(i % 12) + 1 for i in range(len(forecast))]  # Generate months cyclically from 1 to 12

    # Combine historical and forecasted data
    forecast.reset_index(drop=True, inplace=True)
    historical_data = historical_data.reset_index(drop=True)

    # Ensure no duplicate combinations of Month and Year
    forecast = forecast.groupby(['Year', 'Month']).first().reset_index()

    # Create full data by appending forecasted data to historical data
    full_data = pd.concat([historical_data, forecast]).drop_duplicates(subset=['Year', 'Month'])

    # Pivot table to create columns for each year
    pivot_df = full_data.pivot(index='Month', columns='Year', values='Sales').reset_index()

    return pivot_df

@app.route('/', methods=['GET', 'POST'])
def index():
    # Load the data
    historical_data = pd.read_csv('D:/Project/my_data.csv')

    # Check if AI-based forecasting is triggered
    if request.method == 'POST':
        future_years = [2024, 2025, 2026]

        # Perform forecasting
        forecast_df = forecast_sales(historical_data, future_years)

        # Format the data to show historical and forecasted data together
        try:
            formatted_data = format_data(historical_data, forecast_df, future_years)
        except ValueError as ve:
            return f"An error occurred: {ve}"

        # Convert DataFrame to HTML
        data_html = formatted_data.to_html(classes='table table-bordered', index=False)

        return render_template('index.html', data_html=data_html)

    # Handle GET request and search functionality
    search_query = request.args.get('search', '')
    if search_query:
        # Implement search logic here (for example, filtering based on search query)
        pass

    # If no search or AI-based forecasting, show the historical data
    data_html = historical_data.to_html(classes='table table-bordered', index=False)

    return render_template('index.html', data_html=data_html)

if __name__ == "__main__":
    app.run(debug=True)
