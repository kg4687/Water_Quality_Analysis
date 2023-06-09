import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('Water_potablity_trained_model.sav','wb'))

#creating a function for prediction
def water_prediction (input_data):
    input_data_as_np_array = np.asarray(input_data)
    input_data_reshape = input_data_as_np_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    if(prediction[0] ==0):
        return 'Water is not potable'
    else:
        return 'Water is Potable'
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
    potable = ''
    
    #getting input data from the user
    if st.button('Water Quality test result: '):
       potable = water_prediction([pH,Hardness,solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity])
        
    st.success(potable)

#Driver Code
if __name__ == '__main__':
    main()
