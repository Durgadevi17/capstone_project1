
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
#import contractions
from bs4 import BeautifulSoup
import re
import unicodedata


def strip_html_tags(text):
  soup = BeautifulSoup(text, "html.parser")
  [s.extract() for s in soup(['iframe', 'script'])]
  stripped_text = soup.get_text()
  stripped_text = re.sub(r'[\r|\n|\r\n]+', '\n', stripped_text)
  return stripped_text

def remove_accented_chars(text):
  text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
  return text

def remove_http(url):
  p= re.compile('(http(s)?|www)')
  url = p.sub('',url)
  return url
  return text

#stop_words = nltk.corpus.stopwords.words('english')
def remove_stopwords(text, is_lower_case=False, stopwords=None):
    if not stopwords:
        stopwords = nltk.corpus.stopwords.words('english')
    tokens = nltk.word_tokenize(text)
    tokens = [token.strip() for token in tokens]
    
    if is_lower_case:
        filtered_tokens = [token for token in tokens if token not in stopwords]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stopwords]
    
    filtered_text = ' '.join(filtered_tokens)    
    return filtered_text
    
def preprocessor(doc):
  doc = strip_html_tags(doc)
  doc = doc.translate(doc.maketrans("\n\t\r", "   "))
  doc = doc.lower()
  doc = remove_accented_chars(doc)
  # lower case and remove special characters\whitespaces
  doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc, re.I|re.A)
  doc = re.sub(' +', ' ', doc)
  doc = doc.strip()  
  doc = remove_http(doc)
  doc = remove_stopwords(doc,is_lower_case=False)

  return doc
 