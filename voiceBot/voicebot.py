import speech_recognition as sr
import requests
import pyttsx3

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio,language='en')
        print("You said:", recognized_text)
        return recognized_text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Error fetching results:", e)

def send_text_to_rasa(user_text):
    url = "http://192.168.0.111:5005/webhooks/rest/webhook"  # Replace with your Rasa server URL
    data = {
        "sender": "user",
        "message": user_text
    }
    response = requests.post(url, json=data)
    print(response.json())
    return response.json()

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    
    user_input = recognize_speech()
    if user_input:
        rasa_response = send_text_to_rasa(user_input)
        if rasa_response and len(rasa_response) > 0:
            print("Bot says:")
            for i in rasa_response:
                bot_message = i['text']
                print(bot_message)
                text_to_speech(bot_message)




# import speech_recognition as sr
# import requests
# from gtts import gTTS
# import os
# import subprocess
# from playsound import playsound


# def recognize_speech():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Say something...")
#         audio = recognizer.listen(source)

#     try:
#         recognized_text = recognizer.recognize_google(audio)
#         print("You said:", recognized_text)
#         return recognized_text
#     except sr.UnknownValueError:
#         print("Sorry, I could not understand what you said.")
#     except sr.RequestError as e:
#         print("Error fetching results:", e)

# def send_text_to_rasa(user_text):
#     url = "http://localhost:5005/webhooks/rest/webhook"  # Replace with your Rasa server URL
#     data = {
#         "sender": "user",
#         "message": user_text
#     }
#     response = requests.post(url, json=data)
#     print(response.json())
#     return response.json()

# def text_to_speech(text, output_file="output.mp3"):
#     tts = gTTS(text=text, lang="en")  # Assuming English language, change lang parameter if needed
#     tts.save(output_file)
#     return output_file

# if __name__ == "__main__":
#     user_input = recognize_speech()
#     if user_input:
#         rasa_response = send_text_to_rasa(user_input)
#         if rasa_response and len(rasa_response) > 0:
#             print("Bot says, ",end=' ')
#             for i in rasa_response:
#                 bot_message = i['text']
#                 print(f"{bot_message}")
#                 myobj = gTTS(text=bot_message.translate(bot_message))
#                 welcom = myobj.save("welcome.mp3")
#                 print('saved')
#                 # Playing the converted file
#                 # subprocess.call(['cvlc', "welcome.mp3", '--play-and-exit'])



#             # bot_response_text = rasa_response[0]['text']
#             # print("Rasa Bot Response:", bot_response_text)
#             # output_file = text_to_speech(bot_response_text)
#             # os.system(f'start {output_file}')  # This will play the generated audio file (Windows)
















# only speech to text 

# import speech_recognition as sr
# import requests

# def recognize_speech():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Say something...")
#         audio = recognizer.listen(source)

#     try:
#         recognized_text = recognizer.recognize_google(audio)
#         print("You said:", recognized_text)
#         return recognized_text
#     except sr.UnknownValueError:
#         print("Sorry, I could not understand what you said.")
#     except sr.RequestError as e:
#         print("Error fetching results:", e)

# def send_text_to_rasa(user_text):
#     url = "http://localhost:5005/webhooks/rest/webhook"  # Replace with your Rasa server URL
#     data = {
#         "sender": "user",
#         "message": user_text
#     }
#     response = requests.post(url, json=data)
#     print(response.json())
#     return response.json()
# if __name__ == "__main__":
#     user_input = recognize_speech()
#     if user_input:
#         rasa_response = send_text_to_rasa(user_input)
#         print("Rasa Response:", rasa_response)


# def process(self, messages: List[Message]) -> List[Message]:
#         # Initialize the recognizer
#         recognizer = sr.Recognizer()

#         for message in messages:
#             if 'voice' in message.data:
#                 audio_data = message.data['voice']['audio']
                
#                 # Perform voice recognition using the SpeechRecognition library
#                 recognized_text = self.voice_to_text(recognizer, audio_data)
                
#                 # Set the recognized text as a new message with key 'text'
#                 new_message = Message(data={'text': recognized_text})
#                 messages.append(new_message)

#                 # Set the recognized text as a slot for later use
#                 message.set(SlotSet("recognized_text", recognized_text))

#         return messages

#     def voice_to_text(self, recognizer, audio_data):
#         # Perform voice recognition using the SpeechRecognition library
#         with sr.AudioData(audio_data) as source:
#             recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#             text = recognizer.recognize_google(source)  # Perform speech recognition
        
#         return text

# from typing import Dict, Text, Any, List
# from googletrans import Translator
# from rasa_sdk import Action, Tracker
# from langdetect import detect
# from rasa_sdk.events import SlotSet
# import speech_recognition as sr
# # from typing import List, Dict
# # from rasa.shared.nlu.training_data.message import Message

# from rasa.engine.graph import GraphComponent, ExecutionContext
# from rasa.engine.recipes.default_recipe import DefaultV1Recipe
# from rasa.engine.storage.resource import Resource
# from rasa.engine.storage.storage import ModelStorage
# from rasa.shared.nlu.training_data.message import Message
# from rasa.shared.nlu.training_data.training_data import TrainingData

# # TODO: Correctly register your component with its type
# @DefaultV1Recipe.register(
#     [DefaultV1Recipe.ComponentType.MESSAGE_TOKENIZER], is_trainable=False
# )
# class Preprocess(GraphComponent):
#     @classmethod
#     def create(
#         cls,
#         config: Dict[Text, Any],
#         model_storage: ModelStorage,
#         resource: Resource,
#         execution_context: ExecutionContext,
#     ) -> GraphComponent:
#         # TODO: Implement this
#         ...

#     def train(self, training_data: TrainingData) -> Resource:
#         # TODO: Implement this if your component requires training
#         ...

#     def process_training_data(self, training_data: TrainingData) -> TrainingData:
#         # TODO: Implement this if your component augments the training data with
#         #       tokens or message features which are used by other components
#         #       during training.
#         ...

#         return training_data

#     def process(self, messages: List[Message]) -> List[Message]:
#         # Initialize the recognizer
#         recognizer = sr.Recognizer()

#         for message in messages:
#             if 'voice' in message.data:
#                 audio_data = message.data['voice']['audio']
                
#                 # Perform voice recognition using the SpeechRecognition library
#                 recognized_text = self.voice_to_text(recognizer, audio_data)
                
#                 # Set the recognized text as a new message with key 'text'
#                 new_message = Message(data={'text': recognized_text})
#                 messages.append(new_message)

#                 # Set the recognized text as a slot for later use
#                 # message.set(SlotSet("recognized_text", recognized_text))

#         return messages

#     def voice_to_text(self, recognizer, audio_data):
#         # Perform voice recognition using the SpeechRecognition library
#         with sr.AudioData(audio_data) as source:
#             recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#             text = recognizer.recognize_google(source)  # Perform speech recognition
        
#         return text

    

