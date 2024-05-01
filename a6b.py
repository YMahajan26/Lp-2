import streamlit as st

# Define the knowledge base of diseases, symptoms, and treatments
knowledge_base = {
    "cold": {
        "symptoms": ["runny nose", "sneezing", "sore throat", "fever"],
        "treatment": ["Tylenol", "Panadol", "Nasal spray", "Wear warm clothes"]
    },
    "influenza": {
        "symptoms": ["headache", "runny nose", "sneezing", "sore throat", "fever"],
        "treatment": ["Tamiflu", "Panadol", "Zanamivir", "Warm bath", "Salt gargling"]
    },
    "typhoid": {
        "symptoms": ["headache", "abdominal pain", "poor appetite", "fever"],
        "treatment": ["Chloramphenicol", "Amoxicillin", "Ciproflaxacin", "Azithromycin", "Complete bed rest", "Soft diet"]
    },
    "chicken pox": {
        "symptoms": ["rash", "fever", "headache", "chills", "body ache"],
        "treatment": ["Varicella vaccine", "Immunoglobulin", "Acetomenaphin", "Acyclovir", "Oatmeal", "Stay at home"]
    },
    "measles": {
        "symptoms": ["fever", "runny nose", "rash", "conjunctivitis"],
        "treatment": ["Tylenol", "Aleve", "Advil", "Vitamin A", "Rest", "Fluid intake"]
    },
    "malaria": {
        "symptoms": ["fever", "sweating", "headache", "nausea", "vomiting", "diarrhea"],
        "treatment": ["Aralen", "Qualaquin", "Plaquenil", "Mefloquine", "Sleep indoors", "Cover body"]
    }
}

# Function to diagnose the disease based on symptoms
def diagnose(symptoms):
    # Search for matching diseases based on symptoms
    matching_diseases = [disease for disease, info in knowledge_base.items() if set(info["symptoms"]).issubset(symptoms)]
    if matching_diseases:
        # Display diagnosis and treatment for the first matching disease
        disease = matching_diseases[0]
        st.write(f"You have {disease}!")
        st.write("Please take the following medicines and precautions:")
        for treatment in knowledge_base[disease]["treatment"]:
            st.write(treatment)
    else:
        st.write("No matching disease found. Please consult a doctor.")

# Streamlit app
st.header("Medical Diagnosis Expert System")

# Multi-select dropdown for selecting symptoms
selected_symptoms = st.multiselect(
    'Select your symptoms:',
    ["headache", "runny nose", "sneezing", "sore throat", "fever", "chills", "body ache", "abdominal pain",
     "poor appetite", "rash", "conjunctivitis", "sweating", "nausea", "vomiting", "diarrhea"]
)

# Button to diagnose
if st.button("Diagnose"):
    # Check if symptoms are selected
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        diagnose(selected_symptoms)

# Button to quit
if st.button("Quit"):
    st.write("Thank you for using the Expert system!")
