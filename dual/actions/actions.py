# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from language_utils import detect_language_and_translate

# class ActionProcessMessage(Action):
#     def name(self) -> Text:
#         return "action_process_message"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Get the user's original message
#         user_message = tracker.latest_message.get('text')

#         # Detect language and translate the message to English if needed
#         translated_message = detect_language_and_translate(user_message)

#         # Set the translated message in the latest user message
#         tracker.latest_message['text'] = translated_message

#         # Process the translated message as needed (intent recognition, entity extraction, etc.)
#         # Your regular Rasa NLU pipeline will handle this part

#         return []
