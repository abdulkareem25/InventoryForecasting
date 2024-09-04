# Inventory Forecasting with Flask and ARIMA

This project is an inventory forecasting tool built using Flask, pandas, and the ARIMA model. The tool helps predict future sales based on historical sales data, providing insights into inventory management and demand forecasting.

## Features

- **AI-Based Forecasting:** Utilize the ARIMA model to forecast future sales for selected years.
- **Historical Data Display:** View historical sales data in an organized table format.
- **Interactive User Interface:** Simple, web-based interface built with Flask and Bootstrap for easy navigation and interaction.
- **Data Export:** Displayed data can be easily copied or exported for further analysis.

## Project Structure

- `app.py`: The main Flask application file that handles routing, data processing, and rendering HTML templates.
- `index.html`: The HTML template for the project's user interface, displaying historical and forecasted data in a table format.
- `my_data.csv`: The CSV file containing historical sales data. The data includes monthly sales figures for the years 2021, 2022, and 2023.

## Installation

### Prerequisites

Ensure you have Python installed on your machine. Then, install the required Python packages:

```bash
pip install flask pandas matplotlib statsmodels
