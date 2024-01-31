# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import json
import re
import datetime
from datetime import datetime
from typing import Any, Text, Dict, List
import MySQLdb
import mysql.connector

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from dateutil import parser



class ActionShowDoctors(Action):
    def name(self) -> Text:
        return "action_show_doctors"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        # Retrieve the selected category from the slot
        category = tracker.get_slot("category")
        print(category)


        # Read the doctor names from the JSON file
        with open('./doctors.json', 'r') as file:
            doctors_data = json.load(file)
            print(doctors_data)
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..",doctors_data)
        # Use the category to fetch the list of doctors
        doctors = doctors_data.get(category, [])
        print(doctors)
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",doctors)

        if doctors:
            # Create a message with the list of doctors and buttons
            message = f"Here are the doctors in the {category} category:\n\n"
            buttons = []
            for doctor in doctors:
                buttons.append({"title": doctor, "payload": f"{doctor}"})

            dispatcher.utter_message(message, buttons=buttons)
        else:
            dispatcher.utter_message("I couldn't find any doctors in that category.")

        return []
    
class ActionShowDetails(Action):

    def name(self) -> Text:
        return "action_show_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        category = tracker.get_slot("category")
        doctor = tracker.get_slot("doctor")
        data_time = tracker.get_slot("time")
        number = tracker.get_slot("number")
        name = tracker.get_slot('person')
        # Input date and time string
 # Convert the input string to a datetime object
        time = datetime.fromisoformat(data_time)

        # Format the date and time as per your requirements
        formatted_date = time.strftime("%d/%m/%Y")
        formatted_time = time.strftime("%H.%M")
        # mysql_connection = None
        # cursor = None

        try:
            # Establish a connection to MySQL server
            mysql_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Developer@22",
                database="Appointment"  # Specify the database you created
            )

            # Create a cursor to execute SQL commands
            cursor = mysql_connection.cursor()

            # Insert data into the "appointments" table
            insert_query = """
            INSERT INTO appointments (name, number, doctor, time, category)
            VALUES (%s, %s, %s, %s, %s)
            """
            data = (name,number, doctor, time, category)
            cursor.execute(insert_query, data)

            # Commit the changes
            mysql_connection.commit()

            # Provide a response to the user
            dispatcher.utter_message("Data has been saved to the database.")

        except Exception as e:
            dispatcher.utter_message(f"Error: {str(e)}")

        finally:
            cursor.close()
            mysql_connection.close()




        result = f"Hello {name}, Thank you for your successful booking. You are now scheduled with {doctor} under the {category} category at {formatted_date} {formatted_time}. Your mobile number is {number}."
        dispatcher.utter_message(result)


        return []
    
class ActionExtractDate(Action):
    def name(self) -> Text:
        return "action_extract_date"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Check if the date slot is already set
        text = tracker.latest_message['text']
        print(text)

            # Identify the date patterns in the user input
        date_patterns = [
            r"\d{2}/\d{2}/\d{4}",  # mm/dd/yyyy
            r"\d{4}-\d{2}-\d{2}",  # yyyy-mm-dd
        ]
        dates = []
        for pattern in date_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                # Validate the extracted dates to make sure that they are real dates
                try:
                    date = datetime.date.fromisoformat(match)
                    dates.append(date)
                except ValueError:
                    pass
        # user_input = tracker.latest_message['text']
        # print(user_input)
        # extracted_date = parser.parse(user_input, fuzzy=True)
        # print("extracted Data", extracted_date)

        # if extracted_date:
        #     return [SlotSet("date", extracted_date.strftime("%Y-%m-%d"))]
        # else:
        #     dispatcher.utter_message("I couldn't understand the date. Please specify it in a different format.")
        #     return [SlotSet("date", None)]
        

# Using the method of looping, write a program to print the table of 9 till N in the format as follows:
# (N is input by the user)

# 9 18 27...

# Print NULL if 0 is input

# Input Description:
# A positive integer is provided as an input.

# Output Description:
# Print the table of nine with single space between the elements till the number that is input.

# Sample Input :
# 3
# Sample Output :
# 9 18 27

n = int(input())
result = ""
if n==0:
    print("NULL")
else:
    for i in range(n,n+4):
        result += i
        result += " "
print(result)
        


