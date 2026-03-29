import streamlit as st
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page layout
st.set_page_config(page_title="Chennai Crime Risk Prediction", layout="wide")

# Load model and dataset
model = pickle.load(open("crime_model (1).pkl", "rb"))
data = pd.read_csv(r"C:\BDA\chennai_crime_realistic.csv")

# Title
st.title("Chennai Crime Risk Prediction System")

st.write("This system predicts crime risk level based on location, victim details and time.")

# Sidebar inputs
st.sidebar.header("Enter Crime Details")

areas = data["Area_in_Chennai"].unique()
genders = data["Gender"].unique()
crimes = data["Type_of_Crime"].unique()

area = st.sidebar.selectbox("Area", areas)
gender = st.sidebar.selectbox("Gender", genders)
crime = st.sidebar.selectbox("Crime Type", crimes)

age = st.sidebar.slider("Victim Age", 1, 80)
hour = st.sidebar.slider("Hour", 0, 23)

# Encoding
area_map = {area:i for i,area in enumerate(areas)}
gender_map = {gender:i for i,gender in enumerate(genders)}
crime_map = {crime:i for i,crime in enumerate(crimes)}

area_index = area_map[area]
gender_index = gender_map[gender]
crime_index = crime_map[crime]

# Prediction button
if st.sidebar.button("Predict Risk Level"):

    features = np.array([[area_index, gender_index, crime_index, age, hour]])

    prediction = model.predict(features)
    risk = prediction[0]

    st.subheader("Prediction Result")

    if risk == "High":
        st.error("⚠ High Crime Risk")
    elif risk == "Medium":
        st.warning("⚠ Medium Crime Risk")
    else:
        st.success("✔ Low Crime Risk")

    st.markdown("---")

# =========================
# Crime Data Analysis
# =========================

st.header("Crime Data Analysis")

# Crime by Area
st.subheader("Crime Count by Area")

area_counts = data["Area_in_Chennai"].value_counts()

fig1, ax1 = plt.subplots()
ax1.bar(area_counts.index, area_counts.values)
ax1.set_xlabel("Area")
ax1.set_ylabel("Crime Count")
plt.xticks(rotation=45)

st.pyplot(fig1)

# Crime by Hour
st.subheader("Crime Distribution by Hour")

hour_counts = data["Hour"].value_counts().sort_index()

fig2, ax2 = plt.subplots()
ax2.plot(hour_counts.index, hour_counts.values, marker='o')
ax2.set_xlabel("Hour")
ax2.set_ylabel("Number of Crimes")

st.pyplot(fig2)

# Crime Type Distribution
st.subheader("Crime Type Distribution")

crime_counts = data["Type_of_Crime"].value_counts()

fig3, ax3 = plt.subplots()
ax3.bar(crime_counts.index, crime_counts.values)
ax3.set_xlabel("Crime Type")
ax3.set_ylabel("Count")
plt.xticks(rotation=45)

st.pyplot(fig3)

# Gender vs Crime Type
st.subheader("Gender vs Crime Type Comparison")

gender_crime = data.groupby(["Gender","Type_of_Crime"]).size().unstack()

fig4, ax4 = plt.subplots()
gender_crime.plot(kind="bar", ax=ax4)

ax4.set_xlabel("Gender")
ax4.set_ylabel("Crime Count")

st.pyplot(fig4)

# Hour vs Crime Type
st.subheader("Hour vs Crime Type Analysis")

hour_crime = data.groupby(["Hour","Type_of_Crime"]).size().unstack()

fig5, ax5 = plt.subplots()
hour_crime.plot(kind="bar", ax=ax5)

ax5.set_xlabel("Hour")
ax5.set_ylabel("Crime Count")

st.pyplot(fig5)

# Area vs Crime Type
st.subheader("Area vs Crime Type Analysis")

area_crime = data.groupby(["Area_in_Chennai","Type_of_Crime"]).size().unstack()

fig6, ax6 = plt.subplots()
area_crime.plot(kind="bar", stacked=True, ax=ax6)

ax6.set_xlabel("Area")
ax6.set_ylabel("Crime Count")
ax6.set_title("Crime Types Across Chennai Areas")

plt.xticks(rotation=45)

st.pyplot(fig6)