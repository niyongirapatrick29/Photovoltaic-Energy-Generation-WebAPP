import streamlit as st
import pandas as pd
import numpy as np
# import time
# import blinker



st.write("""
 # WELCOME TO WEBSITE
 This is awesome!
 """)


col1, col2 = st.beta_columns(2)
col1.success('PV1')

with col1:
    Epv = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="PV")
    Epv.dropna(subset=['Model'], inplace=True)
    Epv = Epv[Epv['Model'] != 'Name']
    # PV1
    st.subheader("Facility Name")
    location = st.selectbox("", options=["Select location", "Seoul","Chuncheon","Kangrueng","WonJu","DaeJeon","ChungJu","SuSan","DaeGu","PoHang","YoungJu","Busan","JinJu","JeonJu","KwangJu","MokPo","JeJu"])
    st.subheader("Envelope")
    Envelope_selection = st.selectbox("", options= ["Select Envelope", "North","South","East","West"])
    direction = st.selectbox("", options=["Select Direction", "North", "South", "East", "West"])
    Area = st.number_input("Enter Area", min_value= 0, value= 0, step=0)
    st.subheader("Azimuth Selection")
    Azimuth = st.selectbox("", options = ["Select Azimuth",0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360])
    Slope = st.number_input("Enter a Slope", key='slope')

    st.subheader("""PV Specification Models""")
    model = st.selectbox("Select Model", Epv['Model'].values)
    # st.write(model)
    st.subheader("Scale")
    Amodule = st.number_input("Number of modules(EA)", key='Amodule')
    Radd = st.number_input("Additional attenuation rate(%)", key='Radd')

    inverter = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="Inverter")
    inverter.dropna(subset=['Name'], inplace=True)
    inverter = inverter[inverter['Name'] != 'Units']

    st.subheader("""Inverter Models""")
    model_units = st.selectbox("Select Inverter Model", inverter['Name'].values)
    # st.text (Name)
    Rsurface = st.number_input("Non-vertical surface solar attenuation rate", key='Rsurface')
    Total_equipment_cost = st.number_input("Total equipment cost (KRW)", key='Total equipment cost')
    # Getting module efficiency
    pv = Epv[Epv['Model'] == model]["Module efficiency"].values[0]
    #####st.write(pv)
    ################ Getting inverter efficiency##########################################################
    IV = inverter[inverter['Name'] ==model_units]["Inverter's efficiency"].values[0]
    Rloss = 1 - (1 - 0.02) * (1 - 0.03) * (1 - 0.02) * (1 - 0.01) * (1 - 0.015) * (1 - 0.02) * (1 - 0.005) * (1 - 0.03) * IV
    #-----------------------------------------------------------------------------------------------------------------------

    #++++++++++++++++++++++++++[∑(Srad,month X Rcorr)]++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    with col1:
        st.subheader("Are these information you provide all correct? ")
        Radation = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="Radation", skiprows=3,header=[0,1,2])

        #st.table(Radation.head(10))
        #st.table(Radation.columns)
        azdf = pd.concat((Radation[('Month', 'Unnamed: 0_level_1')],Radation[('Azimuth',Azimuth)]),axis=1)
        azdf.rename(columns={'Unnamed: 0_level_2':'Month'}, inplace=True)
        Rcorr = 1
        azdf['pd'] = azdf['Radiation'] * azdf['Correction Rate']
        Srad_month = azdf.groupby(by = 'Month')['pd'].agg(['sum'])
        #st.table(azdf)
        Srad_month.reset_index(inplace=True)
        #st.write(Srad_month)

        #Srad_jan = Srad_month[Srad_month['Month']==1]['sum'][0]
        ##############################Creation and initialization of output view #############################
        output = {'Facility name': ['PV1', 'PV2', 'PV3', 'PV4'], 'Jan.': [0, 0, 0, 0], 'Feb.': [0, 0, 0, 0],
                  'Mar.': [3, 0, 0, 4], 'Apr.': [0, 0, 0, 0], 'May.': [0, 0, 0, 0],
                  'Jun.': [3, 0, 0, 4], 'Jul.': [0, 0, 0, 0], 'Aug.': [0, 0, 0, 0],
                  'Sept.': [3, 0, 0, 4], 'Oct.': [0, 0, 0, 0], 'Nov.': [0, 0, 0, 0],
                  'Dec.': [3, 0, 0, 4]}
        EG = pd.DataFrame(data=output)

        #####################Read sum of product for each month into a dictionary #################
        cols = {}
        for i in range(0,12):
            columns = EG.columns.values
            cols[i+1]=columns[i+1]
            Srad_jan = Srad_month['sum'][i]
            #################### Compute PV1 for all months######################################
            # pv_jan = EPV = [∑(Srad,jan X Rcorr)] X (EPV X (1 - Rsurface) X (1 - Rloss) X (Amodule X (1 - Radd))
            EG[cols[i+1]][0] = (Srad_month['sum'][i]) * pv *(1-Rsurface)* (1-Rloss)*(Amodule) * (1-Radd)

            #st.write(EG[cols[i+1]][0])

        st.write('Rloss = ',(1-Rloss))
        st.write('EPv = ', pv)
        st.write('Rsurface = ', Rsurface)
        st.write('Radd = ', (1-Radd))
        st.write('Amodule = ', Amodule)

        st.checkbox("YES")
        if st.button("SUBMIT PV1"):
            st.write()


#########################################################Output viewer #############################################

st.table(EG)






























































