import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from PIL import Image






# Load the preprocessed dataset
@st.cache_data #@st.cache
def load_data():
    # Load your preprocessed dataset here
    data = pd.read_csv('dataset.csv')
    return data

# Sidebar - Input parameters
import streamlit as st


# Call  Failure,Complains,Subscription  Length,Charge  Amount,Seconds of Use,Frequency of use,Frequency of SMS,Distinct Called Numbers,Age Group,Tariff Plan,
# Status,Age,Customer Value,FN,FP,Churn
def user_input():
    contract = st.sidebar.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])
    internet_service = st.sidebar.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
    monthly_charges = st.sidebar.slider('Monthly Charges', 18.25, 118.75, 50.00)
    total_charges = st.sidebar.slider('Total Charges', 18.8, 8684.8, 2500.0)
    call_failure = st.sidebar.selectbox('Call Failure', ['Yes', 'No'])
    complains = st.sidebar.selectbox('Complains', ['Yes', 'No'])
    subscription_length = st.sidebar.number_input('Subscription Length (months)', min_value=1, max_value=24, value=12)
    charge_amount = st.sidebar.number_input('Charge Amount', value=0.0)
    seconds_of_use = st.sidebar.number_input('Seconds of Use', value=0)
    frequency_of_use = st.sidebar.number_input('Frequency of Use', value=0)
    frequency_of_sms = st.sidebar.number_input('Frequency of SMS', value=0)
    distinct_called_numbers = st.sidebar.number_input('Distinct Called Numbers', value=0)
    age_group = st.sidebar.selectbox('Age Group', ['Youth', 'Adult', 'Elderly'])
    tariff_plan = st.sidebar.selectbox('Tariff Plan', ['Plan A', 'Plan B', 'Plan C'])
    status = st.sidebar.selectbox('Status', ['Active', 'Inactive'])
    age = st.sidebar.slider('Age', 18, 100, 30)  # Example age slider, adjust as needed
    customer_value = st.sidebar.number_input('Customer Value', value=0.0)
    FN = st.sidebar.number_input('FN', value=0)
    FP = st.sidebar.number_input('FP', value=0)
    contact=st.sidebar.text_input('Contact')
    Churn = st.sidebar.selectbox('Churn', ['Yes', 'No'])
    
    input_data = {
        'Contract': contract,
        'InternetService': internet_service,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'call failure': call_failure,
        'complains': complains,
        'subscription length': subscription_length,
        'charge amount': charge_amount,
        'seconds of use': seconds_of_use,
        'frequency of use': frequency_of_use,
        'frequency of sms': frequency_of_sms,
        'distinct called numbers': distinct_called_numbers,
        'age group': age_group,
        'tariff plan': tariff_plan,
        'status': status,
        'age': age,
        'customer value': customer_value,
        'FN': FN,
        'FP': FP,
        'Contract': contract,
        'Churn': Churn
        
    }
    button = st.button("Show Graph",key = "image_button")
    if(button):
        image = st.image("D:\SPIT-Techsparker - 2\image1.jpg",width=100,use_column_width = True)
    
    

    
    # return input_data


    return pd.DataFrame([input_data])

# Main function
def main():
    # Title
    st.title('Telecommunications Customer Churn Prediction')

    # Description
    st.write('This app predicts customer Churn for a telecommunications company.')

    # Load data
    data = load_data()

    # Show raw data
    if st.checkbox('Show Raw Data'):
        st.write(data)

    # Sidebar - Input parameters
    input_df = user_input()

    # Display input parameters
    st.subheader('User Input Parameters')
    st.write(input_df)

    # Preprocess input data
    # For example: Encoding categorical variables, scaling numerical features

    
    # y = data['Churn']
   # Train model
    
        # Train model
    X = data.drop('Churn', axis=1)
    y = data['Churn']
    
    # img add of graph
    # st.image('D:\SPIT-Techsparker - 2\image1.png', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    # else:
    try:
        X = data.drop('Churn', axis=1)
        model = RandomForestClassifier()
        model.fit(X, y)
    except KeyError:
        st.error("The 'Churn' column is missing in the dataset. Please ensure that it is present.")

    # # Make predictions
    prediction = model.predict(input_df)

    # # Display prediction
    st.subheader('Prediction')
    if prediction[0] == 0:
        st.write('The customer is not likely to Churn.')
    else:
        st.write('The customer is likely to Churn.')
    
try:
    if __name__ == '__main__':
        main()
except:
    print("could not load file")


