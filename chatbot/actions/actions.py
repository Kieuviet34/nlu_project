from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
import datetime as dt
from typing import Any, Text, Dict, List
import pandas as pd 
from rasa_sdk.types import DomainDict
from .preprocess import NLPtils

stopwords_path = 'C:\\Users\\Admin\\nlu_project\\chatbot\\data\\vietnamese-stopwords.txt'
nlp_tils = NLPtils(stopwords_path)
class ActionShowTime(Action):
    def name(self)->Text:
        return "action_show_time"
    def run(self,
            dispatcher:CollectingDispatcher,
            tracker:Tracker,
            domain: Dict[Text,Any])-> List[Dict[Text, Any]]:
        dispatcher.utter_message(text=f'{dt.datetime.now()}')
        return []
    
path = 'C:\\Users\\Admin\\nlu_project\\chatbot\\data\\output.xlsx'
class ShowSubjectInfor(FormValidationAction):
    def name(self)->Text:
        return "action_show_subject_info"
    def validate_subject(self,
                         slot_value: Any,
                         dispatcher: CollectingDispatcher,
                         tracker: Tracker,
                         domain: DomainDict) -> Dict[Text,Any]:
        subject_name = tracker.get_slot('subject')
        student_year = tracker.get_slot('stud_year')
        
        subject = nlp_tils.process_user_input(subject_name)
        df = pd.read_excel(path, index_col=0)
        subject_info = df[(df['TÊN HỌC PHẦN'].str.lower() == subject) 
                          & (df['Đối tượng'] == student_year)]
        if subject_info.empty:
            dispatcher.utter_message(text = f'Xin lỗi, không tìm thấy thông tin về môn học này')
            return {"subject" : None}
        else:
            subject_data = subject_info.iloc[0].to_dict()
            print(subject_data)
            dispatcher.utter_message(text = f'Thông tin về môn {subject} của khóa {student_year}: {subject_data}')
            return {"subject" : subject,
                    "stud_year": student_year}