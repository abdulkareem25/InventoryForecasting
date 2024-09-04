Inventory Forecasting with Flask and ARIMA
This project is an inventory forecasting tool built using Flask, pandas, and the ARIMA model. The tool helps predict future sales based on historical sales data, providing insights into inventory management and demand forecasting.

Features
AI-Based Forecasting: Utilize the ARIMA model to forecast future sales for selected years.
Historical Data Display: View historical sales data in an organized table format.
Interactive User Interface: Simple, web-based interface built with Flask and Bootstrap for easy navigation and interaction.
Data Export: Displayed data can be easily copied or exported for further analysis.
Project Structure
app.py: The main Flask application file that handles routing, data processing, and rendering HTML templates.
index.html: The HTML template for the project's user interface, displaying historical and forecasted data in a table format.
my_data.csv: The CSV file containing historical sales data. The data includes monthly sales figures for the years 2021, 2022, and 2023.
Installation
Prerequisites
Ensure you have Python installed on your machine. Then, install the required Python packages:

bash
Copy code
pip install flask pandas matplotlib statsmodels
Running the Application
Clone the repository to your local machine.
Navigate to the project directory.
Place your historical sales data in the my_data.csv file.
Run the Flask application:
bash
Copy code
python app.py
Open a web browser and go to http://127.0.0.1:5000/ to access the application.
Data Format
The input data (my_data.csv) should follow this format:

csv
Copy code
Month,Year,Sales
1,2021,204.97
2,2021,208.22
...
12,2023,337.79
Month: The month of the year (1-12).
Year: The corresponding year for the sales data.
Sales: The sales figure for that month.
How It Works
Forecasting
The application uses the ARIMA (AutoRegressive Integrated Moving Average) model to forecast future sales.
Users can trigger AI-based forecasting by clicking the "Trigger AI-Based Forecasting" button.
The model generates monthly sales forecasts for the years 2024, 2025, and 2026, which are then displayed alongside the historical data.
Data Display
The forecasted data is combined with historical data and presented in a tabular format.
Each year's sales data is displayed in a separate column, allowing easy comparison between years.
Usage
Viewing Data: By default, the application displays the historical sales data.
Triggering Forecast: Click on the "Trigger AI-Based Forecasting" button to generate and view future sales forecasts.
Searching Data (Planned): The application includes a search functionality, which can be implemented to filter data based on user queries.
Future Enhancements
Search Functionality: Implement a search feature to filter sales data based on month or sales values.
Improved Forecasting: Experiment with different ARIMA parameters or integrate other forecasting models for better accuracy.
Enhanced UI: Add more interactive elements, such as charts or graphs, to visualize sales trends.
Contributing
Feel free to fork this repository and contribute to the project. Pull requests are welcome for any improvements or bug fixes.
