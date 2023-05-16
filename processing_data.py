import re
import data_checker as dc
import round_trip as rt
import data_extracter as de

def split_line(line):
      word = ""
      line = line.strip()
      splitted_line = line.split(" ")
      checker = dc.DataChecker()
      # remove any value in the list with ( "" , . , digit. )
      splitted_line = [x  for x in splitted_line if x != "" and x != '.' and not checker.check_for_digit_dot(x)]
      
      # check for digit only      
      if splitted_line[0].isdigit():
            splitted_line.pop(0)
    
            
      return splitted_line



def pre_processing_data(data : str) -> list[str] | str | str :
      founded_lines = []
      APM = "" ; APE = "" ; line = "" ; trip_number = ""
      checker = dc.DataChecker()
      for character in data:
            if character == '\n' and len(line) > 0:
                  # check for important two line of the trip (MS)
                  if checker.check_properity_of_ms_line(line):
                        # call function to split the line into list 
                        splitted_line =  split_line(line)  
                        # save this line
                        founded_lines.append(splitted_line)
                  # check this line is the first line that conatin (0.):
                  elif checker.check_for_zero_dot(line):
                        # call function to split the line into list 
                        splitted_line = split_line(line)
                        # save this line
                        founded_lines.append(splitted_line)
                  # check this line is contains e-mail
                  elif checker.check_for_ape(line):
                        # call function to split the line into list 
                        splitted_line = split_line(line )
                        APE = splitted_line[-1]
                  # check this line is contains phone number
                  elif checker.check_for_apm(line):
                        splitted_line = split_line(line)
                        if splitted_line[-1].isdigit() and len(splitted_line) == 2 and len(splitted_line[-1]) > 6:
                              APM = splitted_line[-1]
                  # check this line is contains trip number
                  elif checker.check_for_trip_number(line):
                        splitted_line = split_line(line)
                        trip_number = splitted_line[-1]
                  line = ""
                  continue
            line += character 
      return founded_lines, APE , APM , trip_number


def main(text):
      founded_lines , APE , APM , trip_number = pre_processing_data(text)
      
      print("founded_lines : " , founded_lines)
      # extract data
      extracter = de.DataExtracter()
      name_of_company , occupied_seats  = extracter.extract_data_company(founded_lines[0])
      go_trip , avaliable_seats , back_trip  = extracter.extract_data_MS(founded_lines[1] , founded_lines[2])   
      
      free_seats = ''
      if len(avaliable_seats) != 0 : free_seats = int(avaliable_seats) - int(occupied_seats) 

      data = [ trip_number , name_of_company , occupied_seats , go_trip.number_of_trip , go_trip.character , go_trip.date , go_trip.from_to_city ,
      avaliable_seats ,  back_trip.number_of_trip , back_trip.from_to_city , back_trip.date , APM , APE , free_seats ]
      
           

      print(go_trip)
      print(back_trip)
      print("name of company : " , name_of_company , "NM : " , occupied_seats)
      print("hk:" , avaliable_seats)
      print("APE : " , APE)
      print("APM : " , APM)
      print("trip_number : " , trip_number)
      
      return data

