# Define the rule base
rules = [
    {
        "conditions": {"raining": "yes"},
        "decision": "Carry an umbrella"
    },
    {
        "conditions": {
            "raining": "no",
            "cloudy": "yes",
            "jacket": "no"
        },
        "decision": "Carry an umbrella"
    }
]

# Inference engine to process the rules
def make_decision(facts, rules):
    for rule in rules:
        if all(facts.get(key) == value
               for key, value in rule["conditions"].items()):
            return rule["decision"]
    return "No need to carry an umbrella"


# User interface for input/output
def main():
    print("Simple Umbrella Decision Expert System")
    print("---------------------------------------")

    # Collect input (facts) from user
    facts = {
        "raining": input("Is it raining? (yes/no): ").strip().lower(),
        "cloudy": input("Is it cloudy? (yes/no): ").strip().lower(),
        "jacket": input("Do you have a jacket? (yes/no): ").strip().lower()
    }

    # Get decision based on rules
    decision = make_decision(facts, rules)

    # Output the decision
    print(f"\nDecision: {decision}")


# Run the program
if __name__ == "__main__":
    main()