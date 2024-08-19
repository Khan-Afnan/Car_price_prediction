# Car_price_prediction
This project is a Car Price Prediction application built using Machine Learning, Streamlit, and Python.
The application allows users to predict the price of a used car based on various features like car model, fuel type, seller type, transmission, and more.

# Features
Select car model, fuel type, seller type, transmission type,car's age,kilometres driven and owner type.
Predict the car's selling price using a pre-trained machine learning model.
Simple and intuitive user interface built with Streamlit.

# Technologies Used
Python: The core programming language used for building the model and backend logic.
Streamlit: A Python library used to create a web-based user interface.
Pandas: For data manipulation and preprocessing.
Joblib: To load the pre-trained machine learning model.
Scikit-learn: Used to train and develop the machine learning model.
CSV File: The cleaned dataset (clean_car_data.csv) containing car details used to train the model.


# Make sure you have the following installed:

Python (version 3.7 or above)
Streamlit (pip install streamlit)
Pandas (pip install pandas)
Joblib (pip install joblib)
Scikit-learn (pip install scikit-learn)

# Create a Virtual Environment
python -m venv venv
# Activate the Virtual Environment in Windows
venv\Scripts\activate
# Install Dependencies
pip install -r requirements.txt
# Run the Project
streamlit run streamlit.py


# Dataset
The model was trained on a cleaned dataset of used cars (clean_car_data.csv), which includes features like:
.Car Model
.Fuel Type
.Seller Type
.Transmission
.Owner Type
.Kilometers Driven
.Car Age
The machine learning model is a pre-trained model stored in the file car_details.pkl. It was trained using Scikit-learn. The model is used to predict the price based on the provided inputs.

# File Structure
streamlit.py: The main Streamlit application file.

car_details.pkl: Pre-trained machine learning model.

clean_car_data.csv: Cleaned dataset used to train the model.

README.md: Project documentation.
