import json
import os

def load_existing_intents(file_path="intentsMed.json"):
    with open(file_path, "r") as file:
        return json.load(file)

def save_updated_intents(intents, file_path="intentsMed.json"):
    with open(file_path, "w") as file:
        json.dump(intents, file, indent=4)

def fetch_new_data():
    # Simulate new knowledge
    return [
        {
            "tag": "covid_update",
            "patterns": ["latest covid update", "new covid news", "corona virus update"],
            "responses": ["COVID-19 updates are available on the WHO website."]
        },
        {
            "tag": "vaccination_info",
            "patterns": ["latest vaccination news", "what's new in vaccination", "vaccination update"],
            "responses": ["Vaccination updates are available on the WHO website."]
        }
    ]

def update_knowledge_base():
    current = load_existing_intents()
    new_data = fetch_new_data()

    tags = [intent['tag'] for intent in current["intents"]]
    for entry in new_data:
        if entry["tag"] not in tags:
            current["intents"].append(entry)

    save_updated_intents(current)
    print("Knowledge base updated.")

if __name__ == "__main__":
    update_knowledge_base()
