AI Car Price Predictor

Project Description
This project is a full-stack web application built with Django that integrates a custom machine learning model to estimate the market value of automobiles. Users can interact with a clean, modern web interface to input car specifications (such as Horsepower, Engine Size, and Curb Weight) and instantly receive a price prediction. The application also logs all predictions to a database to display a recent prediction history.

Goal & Objective
The primary objective of this project is to bridge the gap between data science and web development by training a machine learning regression model and successfully deploying it into a production-ready web application. It demonstrates end-to-end ML lifecycle management: from raw data preprocessing and feature engineering to model serialization and web-based inference.


The Dataset
**Dataset URL:** [Insert Link to your dataset or Kaggle/UCI source here]

The dataset contains various attributes of automobiles, including technical specifications, physical dimensions, and pricing data. Below is a breakdown of the key features used and processed in this project:

| Feature | Description |
| :--- | :--- |
| **price** | The target variable; the price of the vehicle. |
| **horsepower** | The power produced by the car's engine. |
| **engine-size** | The total volume of the cylinders in the engine (cc). |
| **curb-weight** | The weight of the vehicle without occupants or baggage (lbs). |
| **length, width, height** | The physical dimensions of the car, later combined into a single feature. |
| **city-mpg / highway-mpg** | Fuel efficiency in city and highway conditions. |
| **make** | The manufacturer of the vehicle (e.g., Toyota, BMW, Audi). |
| **fuel-system** | The type of fuel injection system used. |
| **num-of-cylinders** | The number of cylinders in the vehicle's engine. |



Data Cleaning and Preparation
To ensure the machine learning model performs optimally, the raw dataset underwent a rigorous pipeline of cleaning and preparation techniques:

1. **Standardizing Missing Values:** Replaced all `?` placeholder strings with standard `NaN` values.
2. **Target Variable Cleansing:** Dropped any rows where the target variable (`price`) was missing, as they cannot be used for supervised training. Duplicate rows were also removed.
3. **Data Imputation:** * Handled missing numerical data by injecting the **median** value of the respective column.
   * Handled missing categorical/text data by injecting the **mode** (most frequent) value.
4. **Outlier Clipping:** Applied statistical clipping to numerical columns, capping extreme outliers below the 1st percentile and above the 99th percentile to prevent skewed training.
5. **Feature Engineering:**
   * Created a `volume` feature by multiplying `length`, `width`, and `height`.
   * Created an `mpg_ratio` feature by dividing `highway-mpg` by `city-mpg`.
6. **Categorical Encoding:** Applied **One-Hot Encoding** (`pd.get_dummies`) to convert all text-based categories (like car make and fuel system) into numerical binary columns.
7. **Feature Scaling:** Used `MinMaxScaler` to normalize all numerical features to a proportional scale between 0 and 1, ensuring no single feature dominated the model due to large raw numbers.
8. **Feature Selection:** Calculated the correlation of all variables against `price` and filtered the dataset to strictly the **Top 15 features** to optimize model efficiency and reduce noise.


 Algorithms and Model Evaluation

**Algorithm Used: Gradient Boosting Regressor**
For this experiment, a **Gradient Boosting Regressor** (`GradientBoostingRegressor` from scikit-learn) was utilized. This is an advanced ensemble learning technique that builds multiple decision trees sequentially, with each new tree attempting to correct the mathematical errors made by the previous ones.

**Metrics for Model Performance Evaluation**
The dataset was split using an 80/20 Train-Test split. The model's predictive performance was evaluated using two primary regression metrics:

**R-Squared ($R^2$):** Measures the proportion of the variance in the car prices that is predictable from the independent variables. A higher percentage indicates a better fit.
**Root Mean Squared Error (RMSE):** Measures the average magnitude of the errors in the predicted prices, expressed in the same units as the target variable (Dollars).
