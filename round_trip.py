class RoundTrip:
    
      def __init__(self , number_of_trip = "" , character="" , date ="",from_to_city=""):
            self.number_of_trip = number_of_trip
            self.character = character
            self.date = date 
            self.from_to_city = from_to_city
            
            
      def __str__(self):
            return f"""number_of_trip : {self.number_of_trip}
character : {self.character} 
date : {self.date}
from_to_city : {self.from_to_city}
"""    