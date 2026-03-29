# Chennai Crime Risk Analysis
## Introduction
Urban crime analysis is challenging due to large, complex, and inconsistent datasets.
This project uses Big Data Analytics and Machine Learning to analyze Chennai crime data and classify crime incidents into different risk levels for better decision-making and public safety.
## Problem Statement
Analyze large-scale crime data to:
* Identify crime patterns in Chennai
* Classify crime risk levels (Low, Medium, High)
* Support proactive safety measures
## Dataset Description
The dataset contains crime records from Chennai including:
* Area_in_Chennai
* Victim_Age
* Gender
* Type_of_Crime
* Date and Time
* Weapon_Used
## Data Preprocessing
* Handled missing values
* Filled numerical values using mean
* Filled categorical values using mode
* Removed duplicates
* Converted date and time features
## Feature Engineering
* Extracted Year and Month from Date
* Processed Time into Hour format
* Created Risk Level classification
## Risk Level Classification
Crimes were categorized into:
* High Risk → Murder, Kidnapping, severe weapon usage
* Medium Risk → Assault, Theft, Cheating
* Low Risk → Less severe crimes
## Data Analysis & Visualization
* Crime distribution by risk level
* Area-wise crime analysis
* Hourly crime trends
* Monthly and yearly patterns
### Insights:
* Higher crime during evening & night
* Certain areas show higher crime intensity
* Medium risk crimes are most frequent
## Machine Learning Models Used
* Logistic Regression
* Decision Tree
* Naive Bayes
* Support Vector Machine
## Model Evaluation
Models were evaluated using accuracy metric.
* Compared multiple models
* Selected best performing model for prediction
## Prediction Example
The model predicts crime risk level based on input features.
### Example Input:
Area, Age, Crime Type, Time
###  Output:
Low / Medium / High Risk
## Clustering Analysis
K-Means clustering was used to group similar crime patterns.
### Clusters identified:
* Theft & kidnapping patterns
* Robbery & cyber crimes
* Assault-related crimes
* Mixed crime patterns
## Technologies Used
* PySpark
* Python
* Machine Learning
* Plotly (Visualization)
## Conclusion
This project demonstrates how Big Data Analytics and Machine Learning can be used to analyze crime patterns, classify risk levels, and support data-driven decision-making for public safety.
