import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from joblib import load

# Loading the Model and Scaler File
model_loaded = load('model.joblib')
scaler = load(scaler.joblib)

# Mean Values for the other features columns
mean_values = {
    'Marital_status': 1.178571,
    'Application_mode': 18.669078,
    'Application_order': 1.727848,
    'Course': 8856.642631,
    'Daytime_evening_attendance': 0.890823,
    'Previous_qualification': 4.577758,
    'Previous_qualification_grade': 132.613314,
    'Nacionality': 1.873192,
    'Mothers_qualification': 19.561935,
    'Fathers_qualification': 22.275316,
    'Mothers_occupation': 10.960895,
    'Fathers_occupation': 11.032324,
    'Admission_grade': 126.978119,
    'Displaced': 0.548373,
    'Educational_special_needs': 0.011528,
    'Debtor': 0.113698,
    'Tuition_fees_up_to_date': 0.880651,
    'Gender': 0.351718,
    'Scholarship_holder': 0.248418,
    'Age_at_enrollment': 23.265145,
    'International': 0.024864,
    'Curricular_units_1st_sem_credited': 0.709991,
    'Curricular_units_1st_sem_enrolled': 6.270570,
    'Curricular_units_1st_sem_evaluations': 8.299051,
    'Curricular_units_1st_sem_approved': 4.706600,
    'Curricular_units_1st_sem_grade': 10.640822,
    'Curricular_units_1st_sem_without_evaluations': 0.137658,
    'Curricular_units_2nd_sem_credited': 0.541817,
    'Curricular_units_2nd_sem_enrolled': 6.232143,
    'Curricular_units_2nd_sem_evaluations': 8.063291,
    'Curricular_units_2nd_sem_approved': 4.435805,
    'Curricular_units_2nd_sem_grade': 10.230206,
    'Curricular_units_2nd_sem_without_evaluations': 0.150316,
    'Unemployment_rate': 11.566139,
    'Inflation_rate': 1.228029,
    'GDP': 0.001969
}

# App's Title
st.title('Status Predictions (Graduated, Enrolled & Dropout) For Students')

# Value Imputation for the Prediction Columns
curricular_units_1st_sem_approved = st.number_input('Berapa banyak mata kuliah yang diambil pada kurikulum Semester 1', min_value=0)
curricular_units_1st_sem_grade = st.number_input('Rata-Rata nilai pada Semester 1', min_value=0.0, format="%.2f")
curricular_units_2nd_sem_approved = st.number_input('Berapa banyak mata kuliah yang diambil pada Semester 2', min_value=0)
curricular_units_2nd_sem_grade = st.number_input('Rata-Rata nilai pada Semester 2', min_value=0.0, format="%.2f")

# Making a new dataframe from the user's inputation
data_baru = pd.DataFrame({
    'Marital_status': [mean_values['Marital_status']],
    'Application_mode': [mean_values['Application_mode']],
    'Application_order': [mean_values['Application_order']],
    'Course': [mean_values['Course']],
    'Daytime_evening_attendance': [mean_values['Daytime_evening_attendance']],
    'Previous_qualification': [mean_values['Previous_qualification']],
    'Previous_qualification_grade': [mean_values['Previous_qualification_grade']],
    'Nacionality': [mean_values['Nacionality']],
    'Mothers_qualification': [mean_values['Mothers_qualification']],
    'Fathers_qualification': [mean_values['Fathers_qualification']],
    'Mothers_occupation': [mean_values['Mothers_occupation']],
    'Fathers_occupation': [mean_values['Fathers_occupation']],
    'Admission_grade': [mean_values['Admission_grade']],
    'Displaced': [mean_values['Displaced']],
    'Educational_special_needs': [mean_values['Educational_special_needs']],
    'Debtor': [mean_values['Debtor']],
    'Tuition_fees_up_to_date': [mean_values['Tuition_fees_up_to_date']],
    'Gender': [mean_values['Gender']],
    'Scholarship_holder': [mean_values['Scholarship_holder']],
    'Age_at_enrollment': [mean_values['Age_at_enrollment']],
    'International': [mean_values['International']],
    'Curricular_units_1st_sem_credited': [mean_values['Curricular_units_1st_sem_credited']],
    'Curricular_units_1st_sem_enrolled': [mean_values['Curricular_units_1st_sem_enrolled']],
    'Curricular_units_1st_sem_evaluations': [mean_values['Curricular_units_1st_sem_evaluations']],
    'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],  # input user
    'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],  # input user
    'Curricular_units_1st_sem_without_evaluations': [mean_values['Curricular_units_1st_sem_without_evaluations']],
    'Curricular_units_2nd_sem_credited': [mean_values['Curricular_units_2nd_sem_credited']],
    'Curricular_units_2nd_sem_enrolled': [mean_values['Curricular_units_2nd_sem_enrolled']],
    'Curricular_units_2nd_sem_evaluations': [mean_values['Curricular_units_2nd_sem_evaluations']],
    'Curricular_units_2nd_sem_approved': [curricular_units_2nd_sem_approved],  # input user
    'Curricular_units_2nd_sem_grade': [curricular_units_2nd_sem_grade],  # input user
    'Curricular_units_2nd_sem_without_evaluations': [mean_values['Curricular_units_2nd_sem_without_evaluations']],
    'Unemployment_rate': [mean_values['Unemployment_rate']],
    'Inflation_rate': [mean_values['Inflation_rate']],
    'GDP': [mean_values['GDP']]
})

# Predicting the 'Status' Value by the Example Data Given
if st.button('Prediksi'):
    # Features Standardization for the new data
    data_baru_scaled = scaler.transform(data_baru)
    
    # Predicting the Value with the given data
    prediksi_baru = model_loaded.predict(data_baru_scaled)
    
    # Showing Prediction's Results
    st.write("Status Prediction Results : ", prediksi_baru[0])
