class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            'Fever': {
                'Symptoms': ['High body temperature', 'Chills', 'Sweating'],
                'Possible Diseases': ['Influenza', 'Malaria', 'Urinary Tract Infection'],
                'Treatment': ['Rest', 'Hydration', 'Antipyretics'],
                'Additional Information': 'Fever is a common symptom of various infections and diseases.'
            },
            'Cough': {
                'Symptoms': ['Persistent coughing', 'Sore throat', 'Difficulty breathing'],
                'Possible Diseases': ['Common cold', 'Bronchitis', 'Pneumonia'],
                'Treatment': ['Cough syrup', 'Warm liquids', 'Steam inhalation'],
                'Additional Information': 'Cough can be a symptom of respiratory infections or other conditions.'
            },
            'Headache': {
                'Symptoms': ['Head pain', 'Pressure or tightness around the head'],
                'Possible Diseases': ['Migraine', 'Tension headache', 'Sinusitis'],
                'Treatment': ['Pain relievers', 'Rest', 'Hydration'],
                'Additional Information': 'Headache can be caused by various factors such as stress, dehydration, or underlying health conditions.'
            },
            'Rash': {
                'Symptoms': ['Skin redness', 'Itching', 'Bumps or blisters'],
                'Possible Diseases': ['Contact dermatitis', 'Eczema', 'Allergic reaction'],
                'Treatment': ['Topical corticosteroids', 'Antihistamines', 'Moisturizers'],
                'Additional Information': 'Rash is a skin condition that may result from allergies, infections, or irritants.'
            },'Malaria': {
                'Symptoms': ['High fever', 'Chills', 'Headache', 'Muscle pain', 'Nausea'],
                'Possible Diseases': ['Malaria'],
                'Treatment': ['Antimalarial medications', 'Rest', 'Hydration'],
                'Additional Information': 'Malaria is a mosquito-borne infectious disease caused by parasites.'
            },
            'Migraine': {
                'Symptoms': ['Severe throbbing or pulsating pain', 'Sensitivity to light, sound, or smells', 'Nausea'],
                'Possible Diseases': ['Migraine'],
                'Treatment': ['Pain relievers', 'Rest in a quiet, dark room', 'Medications for nausea'],
                'Additional Information': 'Migraine is a neurological condition characterized by recurrent headaches.'
            }
        }

    def diagnose(self, symptoms):
        possible_diseases = set()
        for symptom in symptoms:
            for disease, info in self.knowledge_base.items():
                if symptom in info['Symptoms']:
                    possible_diseases.update(info['Possible Diseases'])
        return possible_diseases

    def get_disease_info(self, disease):
        return self.knowledge_base.get(disease)

# Example usage:
def main():
    expert_system = ExpertSystem()
    print("Welcome to the Medical Expert System!")

    while True:
        input_symptoms = input("\nPlease enter the symptoms (separated by commas): ").split(',')

        possible_diseases = expert_system.diagnose(input_symptoms)
        if possible_diseases:
            print("Possible diseases based on symptoms:", possible_diseases)
            choice = input("\nDo you want information about any specific disease? (yes/no): ").lower()
            if choice == 'yes':
                disease_name = input("Please enter the name of the disease: ").strip()
                disease_info = expert_system.get_disease_info(disease_name)
                if disease_info:
                    print("\nInformation about", disease_name, ":")
                    print("Symptoms:", ', '.join(disease_info['Symptoms']))
                    print("Possible Treatments:", ', '.join(disease_info['Treatment']))
                    print("Additional Information:", disease_info['Additional Information'])
                else:
                    print("Disease not found in the knowledge base.")
        else:
            print("No matching diseases found for the given symptoms. Please consult a doctor.")

        repeat = input("\nDo you want to diagnose another set of symptoms? (yes/no): ").lower()
        if repeat != 'yes':
            print("Thank you for using the Medical Expert System!")
            break

if __name__ == "__main__":
    main()
