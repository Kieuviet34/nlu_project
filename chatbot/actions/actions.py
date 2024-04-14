# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import datetime as dt
from typing import Any, Text, Dict, List

class ActionShowTime(Action):
    def name(self)->Text:
        return "action_show_time"
    def run(self,
            dispatcher:CollectingDispatcher,
            tracker:Tracker,
            doman: Dict[Text,Any])-> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f'{dt.datetime.now()}')
        return []