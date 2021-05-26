col2.success( "Select Other PV If Necessary")

if __name__ == '__main__':
    main()

with col2:
    def main():
        menu = ['Select Other PV', 'PV2', 'PV3', 'PV4']
        choice = st.selectbox("", menu)
        # st.s(label="menu")
        st.write()

        if choice == "Select Other PV":

            st.write("")

        elif choice == "PV2":

            df = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="PV")
            df.dropna(subset=['Model'], inplace=True)
            df = df[df['Model'] != 'Name']

            st.subheader("Envelope")
            Envelope_selection1 = st.text_input("Enter Envelope selection", key='Envelope_selection2')
            direction1 = st.text_input("Enter Direction", key='Direction2')
            Azimuth1 = st.number_input("Enter Azimuth", key='Azimuth2')
            Slope1 = st.number_input("Enter a Slope", key='slope2')
            Area1 = st.number_input("Enter Area", key='Area2')

            st.subheader("Installation slope")
            Azimuth_u0 = st.number_input("Enter Azimuth", key='Azimuth_2', min_value=0, max_value=360)
            Slope_e0 = st.number_input("Enter Slope", key='slope_2')
            st.subheader("""PV Specification""")
            st.subheader("Models")
            model1 = st.selectbox("Select Model", df['Model'].values, key="model2")
            st.write(model)
            st.subheader("Scale")
            Number_of_modules1 = st.number_input("Number of modules(EA)", key='Number_of_modules2')
            st.subheader("Shading Information")
            panel_length1 = st.number_input("Panel length(m)", key='panel_length2')
            facility_height1 = st.number_input("Facility height(m)", key='facility_height2')
            obstacle_distance1 = st.number_input("Obstacle distance(m)", key='obstacle_distance2')
            obstacle_height1 = st.number_input("Obstacle height(m)", key='obstacle_height2')
            Additional_attenuation_rate1 = st.number_input("Additional attenuation rate(%)",
                                                           key='Additional attenuation rate2')

            df = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="Inverter")
            df.dropna(subset=['Name'], inplace=True)
            df = df[df['Name'] != 'Units']

            st.subheader("""Inverter Models""")
            model_units1 = st.selectbox("Select Inverter Model", df['Name'].values, key="model_units2")
            # st.text (Name)
            Non_vertical_surface1 = st.number_input("Non-vertical surface solar attenuation rate",
                                                    key='Non_vertical_surface2')
            Total_equipment_cost1 = st.number_input("Total equipment cost (KRW)", key='Total equipment cost2')



        elif choice == "PV3":
            st.subheader(" ")
            df = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="PV")
            df.dropna(subset=['Model'], inplace=True)
            df = df[df['Model'] != 'Name']

            st.subheader("Envelope")
            Envelope_selection1 = st.text_input("Enter Envelope selection", key='Envelope_selection3')
            direction1 = st.text_input("Enter Direction", key='Direction3')
            Azimuth1 = st.number_input("Enter Azimuth", key='Azimuth3')
            Slope1 = st.number_input("Enter a Slope", key='slope3')
            Area1 = st.number_input("Enter Area", key='Area3')

            st.subheader("Installation slope")
            Azimuth_u0 = st.number_input("Enter Azimuth", key='Azimuth_3', min_value=0, max_value=360)
            Slope_e0 = st.number_input("Enter Slope", key='slope_3')
            st.subheader("""PV Specification""")
            st.subheader("Models")
            model1 = st.selectbox("Select Model", df['Model'].values, key="model3")
            st.write(model)
            st.subheader("Scale")
            Number_of_modules1 = st.number_input("Number of modules(EA)", key='Number_of_modules3')
            st.subheader("Shading Information")
            panel_length1 = st.number_input("Panel length(m)", key='panel_length3')
            facility_height1 = st.number_input("Facility height(m)", key='facility_height3')
            obstacle_distance1 = st.number_input("Obstacle distance(m)", key='obstacle_distance3')
            obstacle_height1 = st.number_input("Obstacle height(m)", key='obstacle_height3')
            Additional_attenuation_rate1 = st.number_input("Additional attenuation rate(%)",
                                                           key='Additional attenuation rate3')

            df = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="Inverter")
            df.dropna(subset=['Name'], inplace=True)
            df = df[df['Name'] != 'Units']
            df
            st.subheader("""Inverter Models""")
            model_units1 = st.selectbox("Select Inverter Model", df['Name'].values, key="model_units3")
            # st.text (Name)
            Non_vertical_surface1 = st.number_input("Non-vertical surface solar attenuation rate",
                                                    key='Non_vertical_surface3')
            Total_equipment_cost1 = st.number_input("Total equipment cost (KRW)", key='Total equipment cost3')
        else:
            st.subheader(" ")
            df = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="PV")
            df.dropna(subset=['Model'], inplace=True)
            df = df[df['Model'] != 'Name']

            st.subheader("Envelope")
            Envelope_selection1 = st.text_input("Enter Envelope selection", key='Envelope_selection4')
            direction1 = st.text_input("Enter Direction", key='Direction4')
            Azimuth1 = st.number_input("Enter Azimuth", key='Azimuth4')
            Slope1 = st.number_input("Enter a Slope", key='slope4')
            Area1 = st.number_input("Enter Area", key='Area4')

            st.subheader("Installation slope")
            Azimuth_u0 = st.number_input("Enter Azimuth", key='Azimuth_0', min_value=0, max_value=360)
            Slope_e0 = st.number_input("Enter Slope", key='slope_0')
            st.subheader("""PV Specification""")
            st.subheader("Models")
            model1 = st.selectbox("Select Model", df['Model'].values, key="model4")
            st.write(model)
            st.subheader("Scale")
            Number_of_modules1 = st.number_input("Number of modules(EA)", key='Number_of_modules4')
            st.subheader("Shading Information")
            panel_length1 = st.number_input("Panel length(m)", key='panel_length4')
            facility_height1 = st.number_input("Facility height(m)", key='facility_height4')
            obstacle_distance1 = st.number_input("Obstacle distance(m)", key='obstacle_distance4')
            obstacle_height1 = st.number_input("Obstacle height(m)", key='obstacle_height4')
            Additional_attenuation_rate1 = st.number_input("Additional attenuation rate(%)",
                                                           key='Additional attenuation rate4')

            df = pd.read_excel("Photovoltaic module_V10.xlsx", sheet_name="Inverter")
            df.dropna(subset=['Name'], inplace=True)
            df = df[df['Name'] != 'Units']

            st.subheader("""Inverter Models""")
            model_units1 = st.selectbox("Select Inverter Model", df['Name'].values, key="model_units4")
            # st.text (Name)
            Non_vertical_surface1 = st.number_input("Non-vertical surface solar attenuation rate",
                                                    key='Non_vertical_surface4')
            Total_equipment_cost1 = st.number_input("Total equipment cost (KRW)", key='Total equipment cost4')
