import data_checker as dc
import round_trip as rt

class DataExtracter:
      def extract_digit(self , text : str) -> str:
            digit = ""
            for x in text:
                  if x.isdigit():
                        digit += x
            return digit

      def extract_go_trip_data(self , data : list[str]) -> rt.RoundTrip | str:
            checker = dc.DataChecker()
            index = 0 
            # try to get index of the date 
            for i in range(len(data)):
                  if checker.check_for_date(data[i]):
                        index = i
                        break
            
            go_trip = rt.RoundTrip(" ".join(data[:index - 1]) , data[index - 1] , data[index] , data[index + 2])
            avaliable_seats = self.extract_digit(data[index + 3])
            return go_trip , avaliable_seats

      def extract_back_trip_data(self , data : list[str]) -> rt.RoundTrip:
            checker = dc.DataChecker()
            index = 0 
            # try to get index of the date 
            for i in range(len(data)):
                  if checker.check_for_date(data[i]):
                        index = i
                        break
            back_trip = rt.RoundTrip(" ".join(data[:index - 1]) , data[index - 1] , data[index] , data[index + 2])
            return back_trip 

      def extract_data_MS(self , line1 : list[str] , line2 : list[str]) -> rt.RoundTrip | str | rt.RoundTrip:
            go_trip ,  avaliable_seats_go_trip = self.extract_go_trip_data(line1)
            back_trip  = self.extract_back_trip_data(line2)
            return go_trip , avaliable_seats_go_trip , back_trip 

      def extract_data_company(self , line : str) -> str | int :
            name_of_company = ""
            seats = 0
            # the name of the company it may be one word or multiple word so this line try to get name of the company when reach the NM
            for word in line:
                  if "NM" in word :
                        break
                  name_of_company +=  word + " "
            
            # it may be 'NM:10' or 'NM : 10' or 'NM: 10' or 'NM :10'
            if line[-1].isdigit():
                  seats = int(line[-1])
            else:
                  seats = self.extract_digit(line[-1])
                  
            return name_of_company , seats