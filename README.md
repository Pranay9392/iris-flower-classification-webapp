# Iris Flower Classification Web App

This project implements a machine learning model to classify iris flowers into three species (*setosa*, *versicolor*, and *virginica*) based on sepal and petal measurements.

## Key Steps:

1. **Data Loading and Exploration:** Loaded the Iris dataset, examined its structure, and checked for missing values and duplicates.
2. **Data Visualization:** Created histograms to visualize the distribution of sepal and petal measurements.
3. **Data Preprocessing:** Encoded the 'Species' column using Label Encoding.
4. **Model Training:** Trained a Logistic Regression model on the dataset.
5. **Model Evaluation:** Evaluated the model's accuracy using the test data.
6. **Model Saving:** Saved the trained model using pickle for future use.

---

## Flask Web Application

The project includes a Flask-based web application to provide a user-friendly interface for iris flower classification.

### Features:
- **Input Form:** A form for users to input sepal and petal measurements.
- **Prediction Output:** Displays the predicted iris species based on the input.

### Steps to Build:
1. Install required dependencies:  
   ```bash
   pip install flask numpy pandas scikit-learn
   ```
2. Create a `Flask` application:
   - Build an input form in `index.html`.
   - Load the trained Logistic Regression model using `pickle`.
   - Implement a route (`/predict`) to handle form submissions and make predictions.
3. Start the Flask server:  
   ```bash
   python app.py
   ```

---

## Deployment on Render

The project is deployed on [Render](https://render.com) for easy accessibility.

### Deployment Steps:
1. **Set Up Render Account:**
   - Sign up on Render and create a new web service.
2. **Prepare Your Code for Deployment:**
   - Ensure your code is in a GitHub repository.
   - Include a `requirements.txt` file listing all dependencies.
   - Use a `Procfile` with the following content:  
     ```
     web: python app.py
     ```
3. **Deploy on Render:**
   - Link your GitHub repository to Render.
   - Configure the build environment (e.g., select Python runtime).
   - Deploy the app and access the provided URL.

---

## Usage:

The project includes a trained Logistic Regression model that can predict the species of an iris flower given its sepal length, sepal width, petal length, and petal width. Users can:
1. Run the Flask web application locally.
2. Use the deployed web app on Render to make predictions without running the code locally.

