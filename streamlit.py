import streamlit as st
import pandas as pd
import joblib
df=pd.read_csv("clean_car_data.csv")


car=df["car_model"].unique()
fuel_type=df["fuel"].unique()
seller=df["seller_type"].unique()
transmission_type=df["transmission"].unique()
dealer=df["owner"].unique()

st.title("Car Price Prediction")
st.image("car.jpg")

left,right=st.columns(2)

car_model=left.selectbox (
    "enter the car name",
    car
)
seller_type=left.selectbox (
    "Select the type of seller ",
    seller
)

owner=left.selectbox(
    "Owner",
    dealer
)
fuel=right.selectbox(
    "Fuel Type",
    fuel_type
)
transmission=right.selectbox(
    "transmission",transmission_type
)

Age=right.slider("Age",0,30)

km_driven=st.slider("km_driven",10,15000000)

pipe=joblib.load("car_details.pkl")

new_value = pd.DataFrame(data=[[km_driven,fuel,seller_type,transmission,owner,car_model,Age]],columns=['km_driven','fuel', 'seller_type', 'transmission','owner','car_model','old'])
st.write(new_value)
pred = pipe.predict(new_value)
st.write(pred)





