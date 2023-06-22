import numpy as np
import pickle
import pandas as pd
import streamlit as st 
# import tensorflow as tf
import os

import numpy as np




def welcome():
    return "Welcome All"

def predict_solar(data):
    with open('reg.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    prediction = loaded_model.predict([data])
    return prediction




def main():
    st.title("solar power")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">solar power prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    temperature_2_m_above_gnd=st.text_input("temperature_2_m_above_gnd")            
    relative_humidity_2_m_above_gnd=st.text_input("relative_humidity_2_m_above_gnd")      
    mean_sea_level_pressure_MSL=st.text_input("mean_sea_level_pressure_MSL")          
    total_precipitation_sfc=st.text_input("total_precipitation_sfc")              
    snowfall_amount_sfc=st.text_input("snowfall_amount_sfc")                  
    total_cloud_cover_sfc=st.text_input("total_cloud_cover_sfc")              
    high_cloud_cover_high_cld_lay=st.text_input("high_cloud_cover_high_cld_lay")        
    medium_cloud_cover_mid_cld_lay=st.text_input("medium_cloud_cover_mid_cld_lay")       
    low_cloud_cover_low_cld_lay=st.text_input("low_cloud_cover_low_cld_lay")          
    shortwave_radiation_backwards_sfc=st.text_input("shortwave_radiation_backwards_sfc")    
    wind_speed_10_m_above_gnd=st.text_input("wind_speed_10_m_above_gnd")            
    wind_direction_10_m_above_gnd=st.text_input("wind_direction_10_m_above_gnd")        
    wind_speed_80_m_above_gnd=st.text_input("wind_speed_80_m_above_gnd")            
    wind_direction_80_m_above_gnd=st.text_input("wind_direction_80_m_above_gnd")        
    wind_speed_900_mb=st.text_input("wind_speed_900_mb")                    
    wind_direction_900_mb =st.text_input("wind_direction_900_mb")               
    wind_gust_10_m_above_gnd   =st.text_input("wind_gust_10_m_above_gnd")         
    angle_of_incidence    =st.text_input("angle_of_incidence")               
    zenith =st.text_input("zenith")                      
    azimuth =st.text_input("azimuth")                     
    #generated_power_kw  =st.text_input("generated_power_kw")   
    data=[temperature_2_m_above_gnd, relative_humidity_2_m_above_gnd,
                                       mean_sea_level_pressure_MSL,total_precipitation_sfc,
                                       snowfall_amount_sfc,total_cloud_cover_sfc,high_cloud_cover_high_cld_lay,
                                       medium_cloud_cover_mid_cld_lay,low_cloud_cover_low_cld_lay,
                                       shortwave_radiation_backwards_sfc,wind_speed_10_m_above_gnd,
                                       wind_direction_10_m_above_gnd, wind_speed_80_m_above_gnd,
                                       wind_direction_80_m_above_gnd,wind_speed_900_mb,wind_direction_900_mb,
                                        wind_gust_10_m_above_gnd ,angle_of_incidence ,
                                        zenith,azimuth]       
    print(data)       
    result=""
    if st.button("Predict"):
        result=predict_solar(data)

    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=='__main_':
    main()