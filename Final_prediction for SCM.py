"""
created on 18-04-2023
@author Arnav Saini
"""

import pickle
import numpy as np
import streamlit as st

model=pickle.load(open("D:/Learnbay notes/Machine Learning/Learnbay Interview project_2/Trained_model.sav",'rb'))

def prediction(input):
    arr = np.array(input).reshape(1, -1)

    from sklearn.preprocessing import StandardScaler
    ss = StandardScaler()

    arr = ss.fit_transform(arr)

    result=model.predict(arr)
    return result


def main():
    # giving a title
    st.title('Supply Chain management for a FMCG company')
    st.header('Predicting weight in tons to be stored in Warehouse')

    # taking inpur from the user
    Location_type=st.selectbox('Location_type', ['Urban', 'Rural'])
    if Location_type=='Urban':
        Location_type=1
    else:
        Location_type=0

    WH_capacity_size=st.selectbox('WH_capacity_size', ['small', 'Large','mid'])
    if WH_capacity_size == 'small':
        WH_capacity_size = 1
    else:
        WH_capacity_size = 0

    zone=st.selectbox('zone', ['North','South','East','West'])
    if zone == 'North':
        zone = 1
    else:
        zone = 0

    WH_regional_zone=st.selectbox('WH_regional_zone', ['zone2', 'zone3','zone4'])
    if WH_regional_zone == 'zone2':
        WH_regional_zone = 1
    else:
        WH_regional_zone = 0

    num_refill_req_l3m=st.text_input('refill')
    transport_issue_l1y=st.text_input('transport_issue_l1y')
    Competitor_in_mkt=st.text_input('Competitor_in_mkt')
    retail_shop_num=st.text_input('retail_shop_num')
    wh_owner_type=st.selectbox('wh_owner_type', ['Rented', 'Owned'])
    if wh_owner_type == 'Rented':
        wh_owner_type = 1
    else:
        wh_owner_type = 0

    distributor_num=st.text_input('distributor_num')
    flood_impacted=st.text_input('flood_impacted')
    flood_proof=st.text_input('flood_proof')
    electric_supply=st.text_input('electric_supply')
    dist_from_hub=st.text_input('dist_from_hub')
    workers_num=st.text_input('workers_num')
    storage_issue_reported_l3m=st.text_input('storage_issue_reported_l3m')
    temp_reg_mach=st.text_input('temp_reg_mach')
    approved_wh_govt_certificate=st.selectbox('approved_wh_govt_certificate', ['A', 'B','C'])
    if approved_wh_govt_certificate == 'A':
        approved_wh_govt_certificate = 1
    else:
        approved_wh_govt_certificate = 0
    wh_breakdown_l3m=st.text_input('wh_breakdown_l3m')
    govt_check_l3m=st.text_input('govt_check_l3m')

    #code for prediction
    result = ''

    # creating a button for prediction
    if st.button('Prediction Result'):
        result=prediction([Location_type, WH_capacity_size, zone, WH_regional_zone,num_refill_req_l3m,
                            transport_issue_l1y, Competitor_in_mkt, retail_shop_num, wh_owner_type, distributor_num,
                            flood_impacted, flood_proof,electric_supply, dist_from_hub, workers_num,
                            storage_issue_reported_l3m, temp_reg_mach, approved_wh_govt_certificate,
                           wh_breakdown_l3m, govt_check_l3m ])

    st.success(result)

if __name__=='__main__':
    main()

# after this , just open terminal and write
# streamlit run 'file location of web app.py'