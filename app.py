import streamlit as st
import pandas as pd
import joblib

# LOAD MODEL
model = joblib.load("model/xgb_model.joblib")

# PAGE
st.set_page_config(page_title="Student Prediction", layout="wide")
st.title("🎓 Student Status Prediction")

# MAPPING
yesno = {"Yes": 1, "No": 0}
gender_map = {"Male": 1, "Female": 0}

marital_map = {
    "Single": 1,
    "Married": 2,
    "Widower": 3,
    "Divorced": 4,
    "Facto Union": 5,
    "Legally Separated": 6
}

application_mode_map = {
    "1st Phase General": 1,
    "Ordinance 612/93": 2,
    "Azores Special": 5,
    "Other Higher Course": 7,
    "Ordinance 854-B/99": 10,
    "International Student": 15,
    "Madeira Special": 16,
    "2nd Phase": 17,
    "3rd Phase": 18,
    "Over 23 Years Old": 39,
    "Transfer": 42,
    "Change Course": 43,
    "Tech Diploma": 44
}

course_map = {
    "Biofuel Production Technologies": 33,
    "Animation and Multimedia Design": 171,
    "Social Service Evening": 8014,
    "Agronomy": 9003,
    "Communication Design": 9070,
    "Veterinary Nursing": 9085,
    "Informatics Engineering": 9119,
    "Equinculture": 9130,
    "Social Service": 9238,
    "Management": 9147,
    "Tourism": 9254,
    "Nursing": 9500,
    "Oral Hygiene": 9556,
    "Advertising and Marketing Management": 9670,
    "Journalism and Communication": 9773,
    "Basic Education": 9853,
    "Management Evening": 9991
}

qualification_map = {
    "Secondary education": 1,
    "Higher education - bachelor's degree": 2,
    "Higher education - degree": 3,
    "Higher education - master's": 4,
    "Higher education - doctorate": 5,
    "Frequency of higher education": 6,
    "12th year of schooling - not completed": 9,
    "11th year of schooling - not completed": 10,
    "Other - 11th year of schooling": 12,
    "10th year of schooling": 14,
    "10th year of schooling - not completed": 15,
    "Basic education 3rd cycle (9th/10th/11th year)": 19,
    "Basic education 2nd cycle (6th/7th/8th year)": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Professional higher technical course": 42,
    "Higher education - master (2nd cycle)": 43
}

nationality_map = {
    "Portuguese": 1,
    "German": 2,
    "Spanish": 6,
    "Italian": 11,
    "Dutch": 13,
    "English": 14,
    "Lithuanian": 17,
    "Angolan": 21,
    "Cape Verdean": 22,
    "Guinean": 24,
    "Mozambican": 25,
    "Santomean": 26,
    "Turkish": 32,
    "Brazilian": 41,
    "Romanian": 62,
    "Moldova (Republic of)": 100,
    "Mexican": 101,
    "Ukrainian": 103,
    "Russian": 105,
    "Cuban": 108,
    "Colombian": 109
}

# INPUT UI
col1, col2, col3 = st.columns(3)

with col1:
    marital = marital_map[st.selectbox("Marital Status", marital_map.keys())]
    application_mode = application_mode_map[st.selectbox("Application Mode", application_mode_map.keys())]
    application_order = st.slider("Application Order", 0, 9)
    course = course_map[st.selectbox("Course", course_map.keys())]
    daytime = yesno[st.selectbox("Daytime", ["Yes", "No"])]

with col2:
    prev_qual = qualification_map[st.selectbox("Previous Qualification", qualification_map.keys())]
    prev_grade = st.slider("Previous Grade", 0, 200)
    nationality = nationality_map[st.selectbox("Nationality", nationality_map.keys())]
    admission_grade = st.slider("Admission Grade", 0, 200)
    age = st.slider("Age", 0, 100)

with col3:
    gender = gender_map[st.selectbox("Gender", gender_map.keys())]
    debtor = yesno[st.selectbox("Debtor", yesno.keys())]
    tuition = yesno[st.selectbox("Tuition Paid", yesno.keys())]
    scholarship = yesno[st.selectbox("Scholarship", yesno.keys())]
    international = yesno[st.selectbox("International", yesno.keys())]

# ACADEMIC
st.subheader("📚 Academic Performance")

col4, col5 = st.columns(2)

with col4:
    cu1_credited = st.number_input("Sem1 Credited", 0, 20)
    cu1_enrolled = st.number_input("Sem1 Enrolled", 0, 20)
    cu1_eval = st.number_input("Sem1 Evaluations", 0, 20)
    cu1_approved = st.number_input("Sem1 Approved", 0, 20)
    cu1_grade = st.slider("Sem1 Grade", 0, 20)
    cu1_without = st.number_input("Sem1 Without Eval", 0, 20)

with col5:
    cu2_credited = st.number_input("Sem2 Credited", 0, 20)
    cu2_enrolled = st.number_input("Sem2 Enrolled", 0, 20)
    cu2_eval = st.number_input("Sem2 Evaluations", 0, 20)
    cu2_approved = st.number_input("Sem2 Approved", 0, 20)
    cu2_grade = st.slider("Sem2 Grade", 0, 20)
    cu2_without = st.number_input("Sem2 Without Eval", 0, 20)

# ECONOMY
st.subheader("📊 Economic Factors")

col6, col7, col8 = st.columns(3)

with col6:
    unemployment = st.number_input("Unemployment Rate", 0.0, 20.0)

with col7:
    inflation = st.number_input("Inflation Rate", 0.0, 20.0)

with col8:
    gdp = st.number_input("GDP", 0.0, 100000.0)

# PREDICT
if st.button("🔍 Predict"):

    mother_qual = 1
    father_qual = 1
    mother_job = 1
    father_job = 1
    displaced = 0
    special_needs = 0

    data = pd.DataFrame([{
        "Marital_status": marital,
        "Application_mode": application_mode,
        "Application_order": application_order,
        "Course": course,
        "Daytime_evening_attendance": daytime,
        "Previous_qualification": prev_qual,
        "Previous_qualification_grade": prev_grade,
        "Nacionality": nationality,
        "Mothers_qualification": mother_qual,
        "Fathers_qualification": father_qual,
        "Mothers_occupation": mother_job,
        "Fathers_occupation": father_job,
        "Admission_grade": admission_grade,
        "Displaced": displaced,
        "Educational_special_needs": special_needs,
        "Debtor": debtor,
        "Tuition_fees_up_to_date": tuition,
        "Gender": gender,
        "Scholarship_holder": scholarship,
        "Age_at_enrollment": age,
        "International": international,

        "Curricular_units_1st_sem_credited": cu1_credited,
        "Curricular_units_1st_sem_enrolled": cu1_enrolled,
        "Curricular_units_1st_sem_evaluations": cu1_eval,
        "Curricular_units_1st_sem_approved": cu1_approved,
        "Curricular_units_1st_sem_grade": cu1_grade,
        "Curricular_units_1st_sem_without_evaluations": cu1_without,

        "Curricular_units_2nd_sem_credited": cu2_credited,
        "Curricular_units_2nd_sem_enrolled": cu2_enrolled,
        "Curricular_units_2nd_sem_evaluations": cu2_eval,
        "Curricular_units_2nd_sem_approved": cu2_approved,
        "Curricular_units_2nd_sem_grade": cu2_grade,
        "Curricular_units_2nd_sem_without_evaluations": cu2_without,

        "Unemployment_rate": unemployment,
        "Inflation_rate": inflation,
        "GDP": gdp
    }])

    pred = model.predict(data)[0]

    label_map = {
        0: "Dropout ❌",
        1: "Enrolled 📚",
        2: "Graduate 🎓"
    }

    st.success(f"Hasil: {label_map[pred]}")