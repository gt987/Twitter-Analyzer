import re
def my_tok(text):
    return re.sub(r'[^\x00-\x7F]+', '', text).split()
