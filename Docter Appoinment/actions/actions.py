from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_greet")
        return []

class ActionShowCategories(Action):
    def name(self) -> Text:
        return "action_show_categories"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_choose_category")
        return []

class ActionShowDoctors(Action):
    def name(self) -> Text:
        return "action_show_doctors"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        category = tracker.get_slot("category")
        dispatcher.utter_button_template(response="utter_choose_doctor", category=category)
        return []

class ActionBookAppointment(Action):
    def name(self) -> Text:
        return "action_book_appointment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Implement appointment booking logic here
        return []


class ActionShowDoctors(Action):
    def name(self) -> Text:
        return "action_show_doctors"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        category = tracker.get_slot("category")

        # Retrieve the list of doctors based on the chosen category
        if category:
            for cat in domain.get("categories", []):
                if cat.get("name") == category:
                    doctors = cat.get("doctors", [])
                    if doctors:
                        button_list = []
                        for doctor in doctors:
                            button_list.append({
                                "title": f"{doctor['name']} ({doctor['role']})",
                                "payload": f"/choose_doctor{{\"doctor\": \"{doctor['name']}\"}}"
                            })
                        
                        dispatcher.utter_button_message(f"Doctors in {category}:", button_list)
                    break

        return []
