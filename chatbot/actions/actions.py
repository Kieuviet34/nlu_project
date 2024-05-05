# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

#
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
import datetime as dt
from typing import Any, Text, Dict, List
import pandas as pd 
from rasa_sdk.types import DomainDict
class ActionShowTime(Action):
    def name(self)->Text:
        return "action_show_time"
    def run(self,
            dispatcher:CollectingDispatcher,
            tracker:Tracker,
            domain: Dict[Text,Any])-> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f'{dt.datetime.now()}')
        return []
    
path = 'C:\\Users\\Admin\\nlu_project\\output.xlsx'
class ShowSubjectInfor(FormValidationAction):
    def name(self)->Text:
        return "action_show_subject_info"
    @staticmethod
    def validate_subject(self,
                         slot_value: Any,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: DomainDict) -> Dict[Text,Any]:
        subject = tracker.get_slot('subject')
        df = pd.read_excel(path, index_col=0)
        subject_info = df[df['TÊN HỌC PHẦN'] == subject]
        
        if subject_info.empty:
            dispatcher.utter_message(text = f'Xin lỗi, không tìm thấy thông tin về môn học này')
            return {"subject" : None}
        else:
            subject_data = subject_info.iloc[0].to_dict()
            print(subject_data)
            dispatcher.utter_message(text = f'Thông tin về môn {subject}: {subject_data}')
            return {"subject" : subject}