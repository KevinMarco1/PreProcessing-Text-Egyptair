import re

months = ['JAN' , 'FEB' , 'MAR' , 'APR' , 'MAY' , 'JUN' , 'JUL' , 'AUG' , 'SEP' , 'OCT' , 'NOV' , 'DEC']

class DataChecker:
    def check_for_trip_number(self , line : str) -> bool :
        regex = r'\b' + r'(\d{1,2}(?:' + '|'.join(months) + r')\d{2}' + r'\/\d+Z\b)' + r'\b'
        return re.search(regex , line)
    
    def check_for_svc(self  , line : str) -> bool:
        # check for finding SVC only
        # Ex:  'SVC 1236456'  -> it will return SVC as a complete word  -> return true
        regex = r'\bSVC\b'
        # return true if found
        return re.search(regex, line)

    def check_for_ms(self , line : str) -> bool:
        # check for finding MS with or not digits
        # Ex:  'MS23456' or ( 'MS' only )    -> return true
        regex =  r"\bMS(?:\d+)?\b"
        # return true if found
        return re.search(regex, line)

    def check_for_date(self , line : str) -> bool:
        # check for digits wth  any abreviation of list month
        # Ex:  '12JAN'   -> return true
        regex = r'\b\d{1,2}(?:' + '|'.join(months) + r')\b'
        # return true if found
        return re.search(regex, line)

    def check_properity_of_ms_line(self , line : str) -> bool:
        # try to get the line that have  ms , date and not have svc
        if  self.check_for_ms(line) and not self.check_for_svc(line) and self.check_for_date(line):
                return True
        return False

    def check_for_digit_dot(self , line : str) -> bool:
        # check for digits with dot
        # Ex:  '10.' , '11.' as a complete word  -> return true
        regex = r"\d+\."
        # return true if found
        return re.search(regex, line)

    def check_for_zero_dot(self , line : str) -> bool:
        # check this line is the first line that conatin (0.):
        # Ex : 0. fadsfasdf  -> return true
        regex = r"\b0\.(?!\w)"
        # return true if found
        return re.search(regex, line)

    def check_for_ape(self , line : str) -> bool:
        # check for line that contains APE as a complete word
        # Ex : APE fdsafsaqwrqwe -> return true
        regex = r'\bAPE\b'
        # return true if found
        return re.search(regex , line)
    
    def check_for_apm(self , line : str) -> bool:
        # check for line that contains APM as a complete word
        # Ex : APM fdsafsaqwrqwe -> return true
        regex = r'\bAPM\b'
        # return true if found
        return re.search(regex , line)
            