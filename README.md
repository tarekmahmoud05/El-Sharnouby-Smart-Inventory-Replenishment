# 🏭 El Sharnouby – Smart Inventory & Replenishment System

An end-to-end AI-driven inventory management and replenishment system that uses **Global LightGBM Quantile Regression** to forecast product demand and generate dynamic inventory replenishment recommendations across multiple business locations.

The system combines time-series forecasting, inventory simulation, and a Flask-based web application to support data-driven supply chain decisions, helping businesses determine **what to order, how much to order, where to replenish, and when**.

## 🚀 Project Overview

Traditional inventory management often relies on fixed reorder levels and historical averages, which may not adequately capture demand variability, seasonality, or supplier lead times.

This project addresses these challenges through a machine learning-based forecasting approach combined with an inventory replenishment simulation.

A global LightGBM model learns demand patterns using historical inventory data, generating quantile-based demand forecasts. These forecasts are then integrated into an order-up-to inventory policy that considers current stock levels, incoming orders, and supplier lead times.

The resulting replenishment recommendations are presented through an interactive web dashboard, allowing users to monitor inventory requirements across different business locations.

## ✨ Key Features

- **Demand Forecasting:** Global LightGBM models using Quantile Regression to estimate expected demand and higher-demand scenarios.
- **Time-Series Feature Engineering:** Historical demand lags, rolling averages, rolling standard deviations, supplier lead times, and monthly seasonality features.
- **Dynamic Inventory Replenishment:** An order-up-to inventory policy that calculates replenishment quantities based on forecasted demand and inventory position.
- **Lead Time Integration:** Accounts for supplier lead times and incoming pipeline orders when calculating replenishment requirements.
- **Inventory Simulation:** Simulates inventory movements, fulfilled demand, ending stock, replenishment orders, and lost sales.
- **Multi-Location Monitoring:** Generates location-specific replenishment recommendations.
- **BOM Integration:** Includes a Bill of Materials (BOM)-based calculation for estimating upstream raw material requirements.
- **Interactive Web Dashboard:** Displays replenishment recommendations, projected ending stock, active reporting period, and total ordering requirements.

## 🧠 Machine Learning Approach

### Global LightGBM Quantile Regression

The project uses a global LightGBM Gradient Boosting Decision Tree (GBDT) model trained on historical inventory data across multiple products and locations.

Instead of training an independent model for every product-location combination, the global approach learns shared demand patterns across the available inventory records.

Two quantile regression models are trained:

| Quantile | Purpose |
|---|---|
| 0.50 | Median demand estimation |
| 0.90 | Higher-demand estimation for replenishment planning |

### Feature Engineering

The forecasting model uses the following features:

- `lag_1`: Previous month's demand.
- `lag_2`: Demand from two months earlier.
- `lag_12`: Demand from the same month in the previous year.
- `rolling_mean_3`: Three-month rolling average of historical demand.
- `rolling_std_3`: Three-month rolling standard deviation.
- `lead_time`: Supplier lead time in days.
- `month_num`: Calendar month to capture seasonal patterns.

### Model Configuration

- Algorithm: LightGBM
- Boosting Type: Gradient Boosting Decision Trees (GBDT)
- Objective: Quantile Regression
- Quantiles: 0.50 and 0.90
- Number of Estimators: 200
- Learning Rate: 0.05
- Random State: 42

The dataset is divided chronologically, using observations before October 2025 for training and observations from October 2025 onward for testing.

## 📦 Inventory Replenishment Logic

The forecasting results are integrated into an order-up-to inventory policy.

For each product and business location, the simulation:

1. Tracks available inventory and incoming pipeline orders.
2. Accounts for supplier lead times and expected incoming quantities.
3. Calculates fulfilled demand and lost sales.
4. Uses the 90th-percentile demand forecast to determine the target inventory level.
5. Calculates the required replenishment quantity based on the inventory position.

The replenishment quantity is calculated using:

`Order Quantity = max(0, Target Inventory - Inventory Position)`

Where:

- **Target Inventory:** Forecasted demand multiplied by the supplier lead-time period plus one replenishment period.
- **Inventory Position:** Available ending stock plus outstanding pipeline orders.

This approach generates dynamic ordering recommendations rather than relying on fixed inventory thresholds.

## 🖥️ Web Application

The project includes a Flask-based web application with an interactive dashboard.

### Dashboard Features

- Business location selection.
- Latest available reporting month.
- Number of products requiring replenishment.
- Total recommended ordering units.
- Product-level replenishment recommendations.
- Projected ending inventory.
- Clear identification of products requiring immediate replenishment.

### Application Architecture

The application uses:
- **Flask:** Backend API and web application routing.
- **Pandas:** Loading and processing exported inventory data.
- **JSON:** Communication between the forecasting pipeline and web application.
- **HTML, JavaScript, and Tailwind CSS:** Interactive frontend interface.

## 🛠️ Technologies & Tools

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | LightGBM |
| Data Processing | Pandas, NumPy |
| Forecasting | Time-Series Feature Engineering, Quantile Regression |
| Inventory Optimization | Order-Up-To Policy, Inventory Simulation |
| Backend | Flask, REST API |
| Frontend | HTML, JavaScript, Tailwind CSS |
| Data Storage | JSON |
| Development Environment | Jupyter Notebook, Google Colab |

## 📂 Project Structure

```text
El-Sharnouby-Smart-Inventory-Replenishment/
│
├── Final_elsharnouby.ipynb
│   └── Data preprocessing, feature engineering,
│       demand forecasting, and inventory simulation
│
├── app.py
│   └── Flask backend and REST API endpoints
│
├── app_data/
│   ├── sim_results.json
│   └── product_master.json
│
├── templates/
│   └── index.html
│       └── Interactive inventory dashboard
│
└── .gitignore.txt
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/tarekmahmoud05/El-Sharnouby-Smart-Inventory-Replenishment.git

cd El-Sharnouby-Smart-Inventory-Replenishment
```

### 2. Install Dependencies

```bash
pip install flask pandas numpy lightgbm
```

### 3. Run the Web Application

Ensure the exported JSON files are available inside the `app_data/` directory.

Start the Flask application:

```bash
python app.py
```

### 4. Access the Dashboard

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

Select a business location to view its latest replenishment recommendations.

### 5. Reproducing the Forecasting Pipeline

To reproduce the machine learning and inventory simulation workflow:

1. Open `Final_elsharnouby.ipynb` in Google Colab or a compatible Jupyter environment.
2. Provide the required source CSV datasets.
3. Execute the notebook cells to perform preprocessing, feature engineering, model training, and inventory simulation.
4. Export the resulting simulation data and product master data into the `app_data/` directory.

The notebook currently expects the source datasets to be available in the Google Colab `/content/` directory.

## 📊 Project Outcomes

The system produces:

- Quantile-based demand forecasts.
- Product-level inventory replenishment quantities.
- Location-specific ordering recommendations.
- Simulated ending inventory levels.
- Lost-sales estimates.
- Upstream raw material requirement calculations through BOM integration.

These outputs provide a foundation for improving inventory visibility and supporting more informed supply chain replenishment decisions.

## 👨‍💻 Author

**Tarek Mahmoud Younes**

Electrical and Electronics Engineering Student | AI & Machine Learning Enthusiast

[GitHub Profile](https://github.com/tarekmahmoud05)

---

*This project demonstrates the application of machine learning, time-series forecasting, and inventory simulation to a practical supply chain management problem.*