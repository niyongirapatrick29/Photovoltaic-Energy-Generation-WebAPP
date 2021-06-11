import streamlit as st
import pandas as pd
import numpy as np
import xlwings as xw
import base64
import operator
# import plotly.express as px
import matplotlib.pyplot as plt

###READ BOOK############



bk = xw.Book("Photovoltaic module_V10.xlsx")
def run_the_app():
    @st.cache
    def load_data(bk):
        return pd.read_excel(bk)
input = bk.sheets['Input']
pv = "WELCOME TO WEBSITE"
st.markdown(
f'<body style="font-size:25px;border: 2px; background-color:skyblue; font-familly: Arial; padding: 10px; "><center>{pv}</center></body>'
, unsafe_allow_html=True)



@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/jepg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

############# Image banner ######################
#st.image("download.jpg", width=698)

#set_png_as_page_bg('images.jpg')


#st.markdown(f'<body style="background-image: url("https://www.undp.org/sites/g/files/zskgke326/files/blogs/shutterstock-Korea-wind-turbines-1831881703.jpg");background-size: cover;"> </body>', unsafe_allow_html=True)

#### Doing multiple columns ###########################
col1, col2 = st.beta_columns(2)

with col1:
        
        pv = "PV1"
        st.markdown(
        f'<body style="font-size:25px;border: 2px; background-color:skyblue; font-familly: Arial; padding: 10px; "><center>{pv}</center></body>'
        , unsafe_allow_html=True)
        
############### Inputs Form for PV1 ########################        
        with st.form(key='my_form'):
                st.text("Facility Name")
                #st.text("Enter a Location")
                location = st.selectbox("", options=["""Select Location""", "Seoul","Chuncheon","Kangrueng","WonJu","DaeJeon","ChungJu","SuSan","DaeGu","PoHang","YoungJu","Busan","JinJu","JeonJu","KwangJu","MokPo","JeJu"])
                #st.subheader("Envelope")
                Envelope_selection = st.selectbox("", options= ["Select Envelope", "North","South","East","West"])
                direction = st.selectbox("", options=["Select Direction", "North", "South", "East", "West"])
                Area = st.number_input("Enter Area", min_value= 0, value= 0, step=0)
                #st.subheader("Azimuth Selection")
                Azimuth = st.selectbox("", options = ["Select Azimuth",0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360])
                Slope = st.number_input("Enter a Slope", key='slope')
                
                Epv = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="PV")
                Epv.dropna(subset=['Model'], inplace=True) 
                Epv = Epv[Epv['Model'] != 'Name']
                def run_the_app():
                        @st.cache
                        def load_data(Epv):
                                time.sleep(2) 
                                return pd.read_excel(Epv)
                #st.subheader("""PV Specification Models""")
                model = st.selectbox("Select PV Model", Epv['Model'].values)
                #st.subheader("Scale")
                Amodule = st.number_input("Enter Number of Modules(EA)", key='Amodule')
                inverter = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="Inverter")
                inverter.dropna(subset=['Name'], inplace=True)
                inverter = inverter[inverter['Name'] != 'Units']
                def run_the_app():
                        @st.cache
                        def load_data(inverter):
                                time.sleep(2) 
                                return pd.read_excel(inverter)
                
                #st.subheader("""Inverter Models""")
                model_units = st.selectbox("Select Inverter Model", inverter['Name'].values)
                Rsurface = st.number_input("Enter Non-vertical Surface Solar Attenuation Rate", key='Rsurface')
                Total_equipment_cost = st.number_input("Enter Total Equipment Cost (KRW)", key='Total equipment cost')
                Equipment_cost = st.number_input("Enter Equipment Cost(Won)", key='Equipment_cost')
                Analysis_period = st.number_input("Enter Analysis period(Won)", key='Analysis_period')
                submit_button = st.form_submit_button(label='Submit')
####################    Other PVs Menu Form    ##################
with col2:
        @st.cache
        def load_data(option):
                        time.sleep(2) 
                        return pd.read_excel(option)
        op = ['Select Other PV', 'PV2', 'PV3','PV4']
        option = st.selectbox("",op)      
        
        
        if option!=op[0]:    
                with st.form(key=option):
                        st.text("Facility Name")
                        #st.subheader("Enter a Location")
                        location = st.selectbox("", options=["Select Location", "Seoul","Chuncheon","Kangrueng","WonJu","DaeJeon","ChungJu","SuSan","DaeGu","PoHang","YoungJu","Busan","JinJu","JeonJu","KwangJu","MokPo","JeJu"])
                        #st.subheader("Envelope")
                        Envelope_selection = st.selectbox("", options= ["Select Envelope", "North","South","East","West"])
                        direction = st.selectbox("", options=["Select Direction", "North", "South", "East", "West"])
                        Area = st.number_input("Enter Area", min_value= 0, value= 0, step=0)
                        #st.subheader("Azimuth Selection")
                        Azimuth = st.selectbox("", options = ["Select Azimuth",0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360])
                        Slope = st.number_input("Enter a Slope", key='slope')
                        Epv = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="PV")
                        Epv.dropna(subset=['Model'], inplace=True) 
                        Epv = Epv[Epv['Model'] != 'Name']
                        def run_the_app():
                                @st.cache
                                def load_data(Epv):
                                        time.sleep(2) 
                                        return pd.read_excel(Epv)
                        #st.subheader("""PV Specification Models""")
                        model = st.selectbox("Select PV Model", Epv['Model'].values)
                        #st.subheader("Scale")
                        Amodule = st.number_input("Enter Number of Modules(EA)", key='Amodule')
                        inverter = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="Inverter")
                        inverter.dropna(subset=['Name'], inplace=True)
                        inverter = inverter[inverter['Name'] != 'Units']
                        def run_the_app():
                                @st.cache
                                def load_data(inverter):
                                        time.sleep(2) 
                                        return pd.read_excel(inverter)
                        #st.subheader("""Inverter Models""")
                        model_units = st.selectbox("Select Inverter Model", inverter['Name'].values)
                        Rsurface = st.number_input("Enter Non-vertical Surface Solar Attenuation Rate", key='Rsurface')
                        Total_equipment_cost = st.number_input("Enter Total Equipment Cost (KRW)", key='Total equipment cost')
                        Equipment_cost = st.number_input("Enter Equipment Cost(Won)", key='Equipment_cost')
                        Analysis_period = st.number_input("Enter Analysis period(Won)", key='Analysis_period')
                        submit_button1 = st.form_submit_button(label='Compare PV1 and '+option)
########################    Other PVs Selection   ######################
                        if submit_button1 and option=="PV2":
                
                
                                input.range('D3:D13').value = [[location],[Envelope_selection],[direction],[Area],[Azimuth],[Slope],[model],[Amodule],[model_units],[Rsurface],[Total_equipment_cost]]
                                #input.range('L4:L6').value = [[Equipment_cost],[Analysis_period]]

                        if submit_button1 and option=="PV3":

                                input.range('E3:E13').value = [[location],[Envelope_selection],[direction],[Area],[Azimuth],[Slope],[model],[Amodule],[model_units],[Rsurface],[Total_equipment_cost]]
                               
                        if submit_button1 and option=="PV4":
                                input.range('F3:F13').value = [[location],[Envelope_selection],[direction],[Area],[Azimuth],[Slope],[model],[Amodule],[model_units],[Rsurface],[Total_equipment_cost]]
                                

########################    writting inputs into pv1   ################ 
if submit_button:

        input = bk.sheets['Input']
        input.range('C3:C10').value = [[location],[Envelope_selection],[direction],[Area],[Azimuth],[Slope],[model],[Amodule]]
        input.range('C16:C18').value = [[model_units],[Rsurface],[Total_equipment_cost]]
        input.range('L4:L6').value = [[Equipment_cost],[Analysis_period]]
                
################### OUTPUT################################
        
st.subheader("Energy generation (kWh)")

input.range("A27:M31").options(pd.DataFrame).value
st.subheader("Net profit for 30 years")
input.range("A37:E40").options(pd.DataFrame).value
#input.range("A33:E44").options(pd.DataFrame).value                         




########################## graph #################
st.set_option('deprecation.showPyplotGlobalUse', False)
# create dataframe
df = pd.DataFrame([
        ['INV', 100.00 ,150.00],
        ['WRK', 200.00, 250.00],
        ['CMP', 300.00 ,350.00],
        ['JRB' ,400.00 ,450.00]],

        columns=['Job Stat', 'Revenue' ,'Total Income'])

df = input.range("A27:M31").options(pd.DataFrame).value

import seaborn as sns
import pandas as pd

pv1 = df[0:1][:]
pv2 = df[1:2][:]
pv3 = df[2:3][:]
pv4 = df[3:4][:]


df_revised = pd.concat([pv1, pv2,pv3,pv4])
df_revised.reset_index(inplace=True)
df_ = df_revised.T
df_.reset_index(inplace=True)

cols = np.array(df_[df_['index']=="Facility name"].values)

data =  np.array(df_[df_['index']!="Facility name"].values)

p = {'Months':data[0:,0], 'PV1':data[0:,1],'PV2':data[0:,2],'PV3':data[0:,3],'PV4':data[0:,4]}

#pvs = pd.DataFrame(p)
pvs = pd.DataFrame(data=p)


#pvs.plot.bar(rot=10, title="Energy Generation")

#plot.show(block=True)


#col = df[df['']]


plt.subplot(x="Months", y= "PV1",data=pvs)
plt.subplot(x="Months", y= "PV2",data=pvs)
plt.subplot(x="Months", y= "PV3",data=pvs)
plt.subplot(x="Months", y= "PV4",data=pvs)
st.pyplot()



#################image bckground #################

