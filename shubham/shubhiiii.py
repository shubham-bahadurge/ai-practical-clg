# Define the rule base for diagnosis
rules = [
    {
        "conditions": {"fever": "yes", "cough": "yes", "body_ache": "yes"},
        "diagnosis": "flu"
    },
    {
        "conditions": {"fever": "no", "cough": "yes", "sneezing": "yes"},
        "diagnosis": "cold"
    },
    {
        "conditions": {
            "fever": "no",
            "cough": "no",
            "sneezing": "yes",
            "itchy_eyes": "yes"
        },
        "diagnosis": "allergy"
    }
]


# Inference engine to process the rules
def diagnose(symptoms, rules):
    for rule in rules:
        if all(symptoms.get(key) == value
               for key, value in rule["conditions"].items()):
            return rule["diagnosis"]
    return "No diagnosis found"


# User interface for input/output
def main():
    print("Simple Medical Diagnosis Expert System")
    print("--------------------------------------")

    # Collect input (symptoms) from user
    symptoms = {
        "fever": input("Do you have a fever? (yes/no): ").strip().lower(),
        "cough": input("Do you have a cough? (yes/no): ").strip().lower(),
        "body_ache": input("Do you have body aches? (yes/no): ").strip().lower(),
        "sneezing": input("Are you sneezing? (yes/no): ").strip().lower(),
        "itchy_eyes": input("Do you have itchy eyes? (yes/no): ").strip().lower()
    }

    # Get diagnosis based on rules
    result = diagnose(symptoms, rules)

    # Output the diagnosis
    print(f"\nDiagnosis: {result.capitalize()}")


# Run the program
if __name__ == "__main__":
    main()