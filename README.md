# Customer Churn Prediction

This project focuses on building a machine learning model to predict customer churn. It includes data preprocessing, exploratory data analysis (EDA), and model development using a Random Forest classifier.

## Project Structure

- **`data/`**
  - **`raw/`**: Contains the original, unprocessed customer dataset (`customer-dataset.csv`).
  - **`processed/`**: Stores the cleaned and preprocessed dataset (`processed_customer_data.csv`).
- **`sql/`**: Holds SQL queries for data analysis and exploration (`queries.sql`).
- **`notebooks/`**: Contains Jupyter notebooks for:
  - **`1_data_preprocessing.ipynb`**: Data cleaning, feature engineering, and preprocessing.
  - **`2_exploratory_data_analysis.ipynb`**: Exploratory data analysis and visualization.
  - **`3_churn_prediction_model.ipynb`**: Model building, evaluation, and hyperparameter tuning.
- **`src/`**: Contains the Python script for:
  - **`query_executor.py`**: Executes SQL queries stored in `queries.sql` on the processed data.

## Getting Started

1. **Prerequisites:** Ensure you have the required libraries installed:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```
2. **Data Preparation**:

   1. Place your raw customer data in `data/raw/customer-dataset.csv`.
   2. Run `1_data_preprocessing.ipynb` to clean and preprocess the data.

3. **Exploratory Data Analysis**:

   - Execute `2_exploratory_data_analysis.ipynb` to gain insights into the data and potential churn predictors.

4. **Model Development**:

   - Run `3_churn_prediction_model.ipynb` to build, evaluate, and tune a Random Forest classifier for churn prediction.

5. **SQL Query Execution**:

   - Use `query_executor.py` to run custom SQL queries on the processed data.

## Key Features

- **Data Preprocessing**: Handles missing values, converts data types, and creates new features like Tenure, DaysSinceLastPurchase, and LoyaltyScore.
- **EDA**: Visualizes distributions, relationships, and correlations to understand customer behavior and identify potential churn factors.
- **Modeling**: Implements a Random Forest classifier and explores hyperparameter tuning to optimize performance.
- **SQL Integration**: Allows for flexible data exploration using SQL queries.

---

## Results

- **Churn Rate**: The baseline churn rate is calculated in the EDA notebook.
- **Feature Importance**: The model identifies the most important predictors of churn.
- **Model Performance**: The final model's performance is evaluated using metrics like accuracy, precision, recall, and F1-score.

---

## Future Work

- Experiment with additional machine learning algorithms (e.g., logistic regression, gradient boosting).
- Explore more advanced feature engineering techniques.
- Deploy the model into a production environment for real-time churn prediction.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the MIT License.
