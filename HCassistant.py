# Sample dataset of rare diseases and their symptoms
# This dictionary maps disease names to lists of associated symptoms
disease_data = {
    "Apert Syndrome": ["skull deformities", "fusion of fingers", "hearing loss"],
    "Ehlers-Danlos Syndrome": ["hyper-flexible joints", "skin that bruises easily", "chronic pain"],
    "Marfan Syndrome": ["tall stature", "long limbs", "heart problems"],
    "Kleine-Levin Syndrome": ["excessive sleep", "hyperphagia", "behavioral changes"],
    "Stiff Person Syndrome": ["muscle stiffness", "muscle spasms", "anxiety"],
}

def diagnose_disease(symptoms):
    """
    This function takes a list of symptoms as input and checks them against the
    predefined disease dataset to find matching diseases.

    Parameters:
    symptoms (list): A list of symptoms provided by the user.

    Returns:
    list: A list of diseases that match the symptoms.
    """
    matched_diseases = []  # Initialize an empty list to store matched diseases

    # Iterate over the disease data
    for disease, disease_symptoms in disease_data.items():
        # Check if any of the patient's symptoms match the disease symptoms
        if any(symptom in disease_symptoms for symptom in symptoms):
            matched_diseases.append(disease)  # Add matched disease to the list

    return matched_diseases  # Return the list of matched diseases

def main():
    """
    The main function that runs the diagnostic assistant.
    It prompts the user for symptoms and displays potential diseases.
    """
    print("Welcome to the Rare Disease Diagnostic Assistant!")
    print("Please enter your symptoms separated by commas (e.g., headache, fever):")
    
    # Get user input and split it into a list of symptoms
    user_input = input("Symptoms: ")
    symptoms = [symptom.strip() for symptom in user_input.split(",")]

    # Call the diagnose_disease function with the user's symptoms
    matched_diseases = diagnose_disease(symptoms)

    # Check if any diseases were matched and display the results
    if matched_diseases:
        print("Based on your symptoms, you may have one of the following rare diseases:")
        for disease in matched_diseases:
            print(f"- {disease}")  # Print each matched disease
    else:
        print("No matching rare diseases found based on the symptoms provided.")

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to run the assistant