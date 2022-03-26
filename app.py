import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image
from datetime import datetime,date,time

model = pickle.load(open('LightRCV.pkl','rb'))
def predict_price(year,month,citygroup,type1,years_old):
    x = np.zeros(36)
    x[0] = citygroup     
    x[1] = type1 
    x[2] = year
    x[3] = month
    x[4] = years_old
    return model.predict([x])[0]

def main():
    
    html_temp = """   
    <div style="background-color:#025246 ;padding:1px">
    <h2 style="color:white;text-align:center;">Restaurant Revenue Prediction </h2>
    </div>
    """


    st.markdown("""
    <style>
    body {
        color: #fff;
        background-color: #5F9EA0;

        
    } .stButton>button {
    color: #000000;
    border-radius: 50%;
    height: 4em;
    width: 5em;
    } 
    </style>
        """, unsafe_allow_html=True)

    

    img = 'https://storage.googleapis.com/kaggle-competitions/kaggle/4272/media/TAB_banner2.png'
    st.image(img, width = 700)    
    st.markdown(html_temp, unsafe_allow_html=True)

    option = st.sidebar.selectbox("Select any option",("Predict","Load Dataset","Summary"))

    

    if option == 'Predict':
        if st.checkbox('Show Description' ):
            st.subheader(' To predict revenue of the restaurant in a given year ')

        city = st.selectbox('Location',('İstanbul', 'Ankara', 'Diyarbakır', 'Tokat', 'Gaziantep',
       'Afyonkarahisar', 'Edirne', 'Kocaeli', 'Bursa', 'İzmir', 'Sakarya',
       'Elazığ', 'Kayseri', 'Eskişehir', 'Şanlıurfa', 'Samsun', 'Adana',
       'Antalya', 'Kastamonu', 'Uşak', 'Muğla', 'Kırklareli', 'Konya',
       'Karabük', 'Tekirdağ', 'Denizli', 'Balıkesir', 'Aydın', 'Amasya',
       'Kütahya', 'Bolu', 'Trabzon', 'Isparta', 'Osmaniye'))
       
        date = st.date_input('Restaurant opening Date')
        
        citygroup = st.selectbox('City Group',("Big City","Other"))
        type1 = st.selectbox('Restaurant Type',('Food Court','In line','Mobile','Drive Thru'))
        
        year = date.year
        month = date.month
        years_old = 2021 - year

        if citygroup == 'Big City' and (city == 'İstanbul' or city == 'Ankara' or city == 'İzmir'):  
            citygroup = 0
        else:
            citygroup = 1
        
        if type1 == 'Food Court':
            type1 = 1
        elif type1 == 'In line':
            type1 = 2
        elif type1 == 'Mobile':
            type1 = 3
        else:
            type1 =0
        

        if st.button("Predict"):
            output=predict_price(year,month,citygroup,type1,years_old)
            predicted = int(output)
            st.success('Approximate Annual Revenue is $ {}'.format(predicted))


    
    data = pd.read_csv('train.csv')
     

    if option == "Load Dataset":
        st.text(" ")
        st.text('Read first 100 rows...!') 
        st.subheader(' Raw data ')    
        st.write(data.head(100))  

    if option=="Summary":
        st.text(" ")
        st.write("Introduction :")
        st.write("Food industry plays a crucial part in the enhancement of the country’s economy.  This mainly plays a key role in metropolitan cities. Where restaurants are essential parts of social gatherings and in recent days there are different varieties of quick-service restaurants like food trucks and takeaways. With this recent rise in restaurant types, it is difficult to decide when and where to open a new restaurant.")
        st.write("Overview :")
        st.write("Over 1,200 quick service restaurants across the globe, TFI is the company where it owns several well-known restaurants across different parts of the Europe and Asia.They employ over 20,000 people in Europe and Asia and make significant daily investments in developing new restaurant sites. We have been encountered with four different types of restaurants. They are inline, mobile, drive-thru, and food court. So deciding to open a new restaurant is challenging with these emerging quick-service restaurants. In recent days, even restaurant sites also include a large investment of time and capital. Geographical locations and cultures also impact the long-time survival of the firm. With the subjective data, it is difficult to extrapolate the place where to open a new restaurant. So TF1 needs a model such that they can effectively invest in new restaurant sites. This competition is to predict the annual restaurant sales of 100,000 regional locations.")
        st.write("Data Overview :")
        st.write("Id: Restaurant ID")
        st.write("Open Date: Opening date of a restaurant")
        st.write("City: City where restaurant is located")
        st.write("City Group: Type of the city. Big cities, or Other.")
        st.write("Type: Type of the restaurant. FC: Food Court, IL: Inline, DT: Drive Thru, MB: Mobile")
        st.write("P1- P37: There are three categories of these obfuscated data.")
        st.write("Demographic data are gathered from third party providers with GIS systems. These include population in any given area, age and gender distribution, development scales. Real estate data mainly relate to the m2 of the location, front facade of the location, car park availability. Commercial data mainly include the existence of points of interest including schools, banks, other QSR operators.")
        st.write("Revenue: The revenue column indicates transformed revenue of the restaurant in a given year and is the target of predictive analysis")




if __name__=='__main__':
    main()