1. **Importing Libraries**

   * Imported the `sys` module to configure the console for displaying the Indian Rupee symbol (₹) using UTF-8 encoding.
   * Imported the `pandas` library to create and manage the dataset in a DataFrame.
   * Imported `LinearRegression` from `sklearn.linear_model` to build the machine learning model.

2. **Creating the Dataset**

   * Created a dataset containing **10 house records**.
   * Each record includes:

     * Area (Square Feet)
     * Number of Bedrooms
     * Number of Bathrooms
     * House Price

3. **Creating a DataFrame**

   * Converted the dataset into a **Pandas DataFrame**.
   * Assigned appropriate column names: `Area`, `Bedrooms`, `Bathrooms`, and `Price`.
   * Displayed the dataset to verify the entered data.

4. **Feature and Target Selection**

   * Selected **Area**, **Bedrooms**, and **Bathrooms** as the **input features (X)**.
   * Selected **Price** as the **target variable (y)** that the model will predict.

5. **Training the Model**

   * Created a **Linear Regression** model using the `LinearRegression()` class.
   * Trained the model using the `fit()` method with the dataset.
   * The model learned the relationship between the house features and their prices.

6. **Taking User Input**

   * Asked the user to enter details of a new house:

     * Square Footage
     * Number of Bedrooms
     * Number of Bathrooms

7. **Preparing Input Data**

   * Converted the user-entered values into a new DataFrame.
   * Ensured the column names matched the training dataset for accurate prediction.

8. **Predicting House Price**

   * Used the trained model and the `predict()` method to estimate the price of the new house.
   * Displayed the predicted price in **Indian Rupees (₹)**.

9. **Displaying Model Parameters**

   * Printed the **Intercept**, which represents the model's base value.
   * Printed the **coefficients** for Area, Bedrooms, and Bathrooms to show how each feature influences the predicted house price.

10. **Project Outcome**

    * Successfully built a beginner-level **House Price Prediction System** using **Linear Regression**.
    * Demonstrated the complete machine learning workflow, including **data preparation, feature selection, model training, prediction, and result interpretation** using Python, Pandas, and Scikit-learn.
