import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('Water_potablity_trained_model.sav','rb'))

#creating a function for prediction
def gold_price_prediction(input_data):
    #changing the input_data to numpy data
    input_data_as_numpy_array = np.asarray(input_data)
    
    #reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    return prediction
def main():
    #giving the title
    st.title('Water Quality Predictor Web App')
    
    #getting input from user
    
    pH = st.text_input('enter the pH value of the water : ')
    Hardness = st.text_input('enter the Hardness value of the water : ')
    solids = st.text_input('enter the solid contents of water : ')
    Chloramines = st.text_input('enter the Chloramines content  value of the water : ')
    Sulfate = st.text_input('enter the Sulfate content value of the water : ')
    Conductivity = st.text_input('enter Conductivity of water')
    Organic_carbon = st.text_input('enter Organic Carbon content')
    Trihalomethanes = st.text_input('Enter Trihalomethants value : ')
    Turbidity = st.text_input('Enter Turbidity value : ')
    
    #code for prediction
    predicted_price = ''
    
    #getting input data from the user
    if st.button('Water is Potable or not: '):
        predicted_price = gold_price_prediction([pH,Hardness,solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity])
        
    st.success(predicted_price)

#Driver Code
if __name__ == '__main__':
    main()
