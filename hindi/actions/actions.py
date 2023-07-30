# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="Hello World!")
#         return []
# from typing import Any, Dict, List, Text
# from iso639 import languages
# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet
# from rasa_sdk.executor import CollectingDispatcher
# from textblob import TextBlob
# class ActionDetectLanguage(Action):
#     def name(self) -> Text:
#         return "action_detect_language"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:

#         text = tracker.latest_message.get("text")
#         langcode = TextBlob(text).detect_language()

#         langname = languages.get(alpha2=langcode).name
#         langname = langname if "(" not in langname else langname.split(" ")[0]

#         return [SlotSet("langcode", langcode), SlotSet("langname", langname)]

# actions.py
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from langdetect import detect

# class ActionDetectLanguage(Action):
#     def name(self) -> Text:
#         return "action_detect_language"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:

#         text = tracker.latest_message.get("text")
#         langcode = detect(text)

#         return [SlotSet("langcode", langcode)]

import spacy

class ActionDetectLanguage(Action):
    def __init__(self):
        self.nlp = spacy.load("xx_ent_wiki_sm")  # Load multilingual language model

    def name(self) -> Text:
        return "action_detect_language"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        text = tracker.latest_message.get("text")
        langcode = self.detect_language(text)

        return [SlotSet("langcode", langcode)]

    def detect_language(self, text):
        doc = self.nlp(text)
        langcode = doc._.language["language"]
        return langcode

