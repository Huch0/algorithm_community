import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Define the regex pattern to match "DIAB1" at the start of a word
    diabetes_type1_pattern = r'\bDIAB1'
    # Filter rows where the 'conditions' column starts with "DIAB1"
    type1_diabetes_patients = patients[patients['conditions'].str.contains(diabetes_type1_pattern, na=False)]
    # Select the desired columns
    result = type1_diabetes_patients[['patient_id', 'patient_name', 'conditions']]
    return result