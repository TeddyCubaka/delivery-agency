import re

class Utils :
    def is_number(string):
        return string.isnumeric()
    
    def is_valid_email(email):
        pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        return bool(pattern.match(email))