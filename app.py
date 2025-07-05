import streamlit as st
import pandas as pd

# Load your cancer data (ensure your Excel/CSV is cleaned and saved as 'cancer_data.csv')
df = pd.read_excel("cancer_data.xlsx")

# Clean column names (remove whitespace)
df.columns = df.columns.str.strip().str.lower()

# Set up Streamlit UI
st.set_page_config(page_title="Cancer Data Chatbot", layout="centered")
st.title("🩺 Cancer Data Chatbot")
st.markdown("Ask questions by selecting one from below:")

# ✅ Updated list of questions (removed broken ones and added new ones)
questions = [
    "What is the total number of patients?",
    "How many male patients are there?",
    "List all cancer types in the dataset.",
    "Number of patients in stage 3?",
    "Average age of all patients?",
    "How many patients are from India?",
    "Number of female patients above age 50?",
    "Which countries have more than 100 patients?",
    "List all unique smoking statuses.",
    "Show count of patients by cancer stage."
]

# Dropdown for user to select a question
selected_question = None
for question in questions:
    if st.button(question):
        selected_question = question

# 💡 Function to answer selected question
def answer_query(question):
    try:
        if question == "What is the total number of patients?":
            return f"Total number of patients: {len(df)}"

        elif question == "How many male patients are there?":
            return f"Male patients: {len(df[df['gender'].str.lower() == 'male'])}"

        elif question == "List all cancer types in the dataset.":
            return f"Cancer types: {df['cancer type'].dropna().unique().tolist()}"

        elif question == "Number of patients in stage 3?":
            return f"Stage 3 patients: {len(df[df['cancer stage'].astype(str).str.lower() == 'stage 3'])}"

        elif question == "Average age of all patients?":
            return f"Average age: {df['age'].mean():.2f} years"

        elif question == "How many patients are from India?":
            return f"Patients from India: {len(df[df['country'].str.lower() == 'india'])}"

        elif question == "Number of female patients above age 50?":
            condition = (df['gender'].str.lower() == 'female') & (df['age'] > 50)
            return f"Female patients above 50: {len(df[condition])}"

        elif question == "Which countries have more than 100 patients?":
            country_counts = df['country'].value_counts()
            filtered = country_counts[country_counts > 100]
            return f"Countries with >100 patients: {filtered.to_dict()}"

        elif question == "List all unique smoking statuses.":
            return f"Smoking statuses: {df['smoking status'].dropna().unique().tolist()}"

        elif question == "Show count of patients by cancer stage.":
            counts = df['cancer stage'].value_counts()
            return f"Patients by stage: {counts.to_dict()}"

        else:
            return "❓ Sorry, I couldn't understand the question."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Display answer on button click
if selected_question:
    response = answer_query(selected_question)
    st.markdown(f"**💬 {response}**")
