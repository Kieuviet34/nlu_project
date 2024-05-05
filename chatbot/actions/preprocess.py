import string, re
import underthesea
from underthesea import word_tokenize

#làm sạch văn bản (loại bỏ kí tự không cần thiết)
def clean_text(txt):
    cleaned = re.sub(r'[^\w\s,.]', '',txt)
    return cleaned
#xử lý stopword 
class NLPtils:
    def __init__(self, stopword_path):
        self.stopword = self.load_stopword(stopword_path)
    def load_stopword(self, stopword_path):
        with open(stopword_path,'r', encoding='utf-8') as f:
            stopwords = [line.strip() for line in f]
        return stopwords
    
    def process_user_input(self,inp:str) -> str:
        inp = inp.lower()
        inp = clean_text(inp) 
        words = underthesea.word_tokenize(inp)
        
        # Loại bỏ stop words
        filter_words = [word for word in words if word not in self.stopword]
        
        # Ghép các từ lại thành câu
        processed_text = ' '.join(filter_words)
        
        return processed_text
