from typing import Dict, Text, Any, List
from googletrans import Translator
from rasa_sdk import Action, Tracker
from langdetect import detect
from rasa_sdk.events import SlotSet
# from typing import List, Dict
# from rasa.shared.nlu.training_data.message import Message

from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData

# TODO: Correctly register your component with its type
@DefaultV1Recipe.register(
    [DefaultV1Recipe.ComponentType.MESSAGE_TOKENIZER], is_trainable=False
)
class Preprocess(GraphComponent):
    @classmethod
    def create(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
    ) -> GraphComponent:
        # TODO: Implement this
        ...

    def train(self, training_data: TrainingData) -> Resource:
        # TODO: Implement this if your component requires training
        ...

    def process_training_data(self, training_data: TrainingData) -> TrainingData:
        # TODO: Implement this if your component augments the training data with
        #       tokens or message features which are used by other components
        #       during training.
        ...

        return training_data

    # def process(self, messages: List[Message]) -> List[Message]:
    #     print(messages)
    #     # This method is used to modify the user message and remove the () if they are included in the user test.
    #     for message in messages:
    #         if 'text' in message.data.keys():
    #             # print(message.data.items())
    #             msg = message.data['text']
    #             if "(" in msg:
    #                 msg = msg.replace("(", "")
    #             if ")" in msg:
    #                 msg = msg.replace(")", "")
    #             # Assigning the preprocess text back to rasa's message object
    #             message.data['text'] = msg
    #     return messages

    # def process(self,messages:List[Message],tracker: Tracker) -> List[Message]:
    # # # Initialize the Google Translate API client
    #     translator = Translator()
    #     for message in messages:
    #         # if 'text' in message.data.keys():
    #         msg = message.data['text']
    #         language = detect(msg)

    #         translation = translator.translate(msg, src=language, dest='en')
    #         message.data['text'] = translation.text
    #         print(translation.text)



    #     return messages
    def process(self, messages: List[Message]) -> List[Message]:
        # Initialize the Google Translate API client
        translator = Translator()

        for message in messages:
            if text in message.data:  # Check if the 'text' key is present in the message data
                text = message.data[text]
                language = detect(text)

                # Set the detected language as a slot for later use
                message.set(SlotSet("langcode", language))

                # Perform language translation if the detected language is not English ('en')
                if language != "en":
                    translation = translator.translate(text, src=language, dest='en')
                    message.data[text] = translation.text

        return messages